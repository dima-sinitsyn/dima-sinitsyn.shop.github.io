from urllib import request
from django.contrib import auth, messages, sessions
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch, QuerySet
from django.db.models.base import Model as Model
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView

# from orders.models import Order, OrderItem

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import ProfileForm, UserLoginForm, UserRegistartionForm

# Create your views here.

 
class UserloginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy('main:index')

    def get_success_url(self) -> str:
        redirect_page = self.request.POST.get("next", None)
        if redirect_page and redirect_page != reverse("user:logout"):
            return redirect_page
        return reverse_lazy("main:index")

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.get_user()
        if user:
            auth.login(self.request, user)

            if session_key:
                forgot_carts = Cart.objects.filter(user=user)
                if forgot_carts.exists():
                    forgot_carts.delete()
                Cart.objects.filter(session_key=session_key).update(user=user)

                messages.success(
                    self.request,
                    f" Уважаемый пользователь {self.request.user.first_name} {self.request.user.last_name}!!! С ником {self.request.user.username} вы вошли в свой аккаунт пользователя",
                )

                return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Robot -авторизация"

        return context


# def login(request):
#     if request.method == "POST":
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST["username"]
#             password = request.POST["password"]
#             user = auth.authenticate(username=username, password=password)


#             session_key = request.session.session_key


#             if user:
#                 auth.login(request, user)
#                 messages.success(
#                     request,
#                     f" Уважаемый пользователь {request.user.first_name} {request.user.last_name}!!! С ником {request.user.username} вы вошли в свой аккаунт пользователя",
#                 )

#                 if session_key:
#                     Cart.objects.filter(session_key= session_key).update(user=user)

#                 redirect_page = request.POST.get('next', None)
#                 if redirect_page and redirect_page != reverse('user:logout'):
#                     return HttpResponseRedirect(request.POST.get('next'))
#                 if request.POST.get("next", None):
#                     return HttpResponseRedirect(request.POST.get("next"))

#                 return HttpResponseRedirect(reverse("main:index"))
#     else:
#         form = UserLoginForm()
#     # form = UserLoginForm()

#     context = {
#         "title": "Robot -авторизация",
#         "form": form,
#     }

#     return render(request, "users/login.html", context)


class UserRegisrationView(CreateView):
    template_name = "users/registration.html"
    form_class = UserRegistartionForm
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user)

        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=user)

        messages.success(
            self.request,
            f" Пользователь  {user.first_name} {user.last_name} вы успешно зарегистрировались и создали  свой аккаунт пользователя",
        )

        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Robot - регистрация пользователя"
        return context


# def registration(request):
#     if request.method == "POST":
#         form = UserRegistartionForm(data=request.POST)
#         if form.is_valid():
#             form.save()

#             session_key = request.session.session_key

#             user = form.instance
#             auth.login(request, user)

#             if session_key:
#                 Cart.objects.filter(session_key= session_key).update(user=user)

#             messages.success(
#                 request,
#                 f"Пользователь  {user.first_name} {user.last_name} вы успешно зарегистрировались и создали  свой аккаунт пользователя ",
#             )

#             return HttpResponseRedirect(reverse("main:index"))

#     else:
#         form = UserRegistartionForm()
#     context = {
#         "title": "Robot - регистрация пользователя",
#         "form": form,
#     }

#     return render(request, "users/registration.html", context)


# class UserProfileView(LoginRequiredMixin, UpdateView):
#     template_name = "users/profile.html"
#     form_class = ProfileForm
#     success_url = reverse_lazy("users:profile")

#     def get_object(self, queryset=None):
#         return self.request.user

#     def form_valid(self, form):
#         messages.success(
#             self.request,
#             f" Пользователь {self.request.user.username} вы успешно обновили профиль ",
#         )
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Robot - профиль "
#         context["orders"] = (
#             Order.objects.filter(user=self.request.user)
#             .prefetch_related(
#                 Prefetch("orderitem_set"), queryset=OrderItem.object.selrct_related
#             )
#             .order_by("id")
#         )
#         return context


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f" Пользователь {request.user.username} вы успешно обновили профиль ",
            )
            return HttpResponseRedirect(reverse("user:profile"))

    else:
        form = ProfileForm(instance=request.user)

    orders = (
        Order.objects.filter(user=request.user)
        .prefetch_related(
            Prefetch(
                "orderitem_set",
                queryset=OrderItem.objects.select_related("product"),
            )
        )
        .order_by("-id")
    )

    context = {"title": "Robot - профиль ", "form": form, "orders": orders}
    return render(request, "users/profile.html", context)


def users_cart(request):
    return render(request, "users/users_cart.html")


@login_required
def logout(request):
    messages.success(
        request,
        f"{request.user.first_name} {request.user.last_name}  вы вышли из аккаунта пользователя {request.user.username} !!!",
    )
    auth.logout(request)

    return redirect(reverse("main:index"))
