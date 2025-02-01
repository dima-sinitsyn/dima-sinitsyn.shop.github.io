
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.db.models.base import Model as Model
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic import DetailView, ListView

from goods1.models import products

from goods1.utils import q_search

# Create your views here.


class CatalogView(ListView):
    model = products
    # query_set = products.objects.all().order_by("-id")
    template_name = "goods1/catalog.html"
    paginate_by = 4
    context_object_name = 'goods1'
    allow_empty = False
    
    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        on_sale = self. request.GET.get("on_sale")
        on_sale_2 = self. request.GET.get("on_sale_2")
        order_by = self. request.GET.get("order_by")
        query_set = self. request.GET.get("q")

        if category_slug == 'all': 
            goods1 =super().get_queryset()
        elif query_set:
            goods1 = q_search(query_set)
        else:
            goods1 =super().get_queryset().filter(category__slug=category_slug)
            if not goods1.exists:
                raise Http404()
    
    
        if on_sale:
            goods1= goods1.filter(discount__gt=0)
        if on_sale_2:
            goods1= goods1.filter(super_discount__gt=0)   
        if order_by and order_by != "default":
            goods1 = goods1.order_by(order_by)
        
        return goods1  
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Robot - каталог товаров"
        context['slug_url']= self.kwargs.get('category_slug')
        return context 
    
    
class ProductView(DetailView):
    template_name = "goods1/product.html"
    slug_url_kwarg = 'product_slug'
    model = products
    context_object_name = 'product'
    
    def get_object(self, queryset=None) -> Model:
        product = products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= self.object.name
        return context





# def product(request, product_slug):
#     product = products.objects.get(slug=product_slug)
    
#     context = {
#         'product' : product
#     }
    
#     return render(request, "goods1/product.html", context=context)




# def reviews(request):
#     context = {
#         "title": "Robot - Отзывы о магазине",
#         "content": "Отзывы наших клиентов",
#         "text_page": "Список отзывов  ",
#     }

#     return render(request, "main/reviews.html", context)








# def catalog(request, category_slug=None):
    
#     page =request.GET.get('page', 1)
#     on_sale =request.GET.get('on_sale', None)
#     on_sale_2 =request.GET.get('on_sale_2', None) 
#     order_by =request.GET.get('order_by', None)
#     query_set =request.GET.get('q', None)
    
#     if category_slug == 'all': 
#         goods1 =products.objects.all()
#     elif query_set:
#         goods1 = q_search(query_set)
#     else:
#         goods1 =get_list_or_404(products.objects.filter(category__slug=category_slug))
#         if not goods1.exists:
#             raise Http404()
        
    
#     if on_sale:
#         goods1= goods1.filter(discount__gt=0)
#     if on_sale_2:
#         goods1= goods1.filter(super_discount__gt=0)   
#     if order_by and order_by != "default":
#         goods1 = goods1.order_by(order_by)
        
#     return goods1

           
    
    # paginator = Paginator(goods1, 4)
    # current_page = paginator.page(int(page))    
    
    # context = {
    #     "title": "Robot - каталог товаров",
    #     "goods1": current_page,
    #     "slug_url": category_slug,
           
    # }
    # return render(request, "goods1/catalog.html", context)