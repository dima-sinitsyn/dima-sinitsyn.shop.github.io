
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods1.models import categories

# Create your views here.


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Robot 😎-главная"
        context['content']='Robot - магазин продажи оргтехники'
        return context
# def index(request):

#     # Categories = categories.objects.all()

#     context = {
#         "title": "Robot 😎",
#         "content": "Robot - главная страница сайта",
#         # 'Categories': Categories
#     }

#     return render(request, "main/index.html", context)



class AboutView(TemplateView):
    template_name = "main/about.html"

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Robot - О магазине "
        context['content']="О магазине Robot"
        context['text_page']="Магазин Robot очень классный и очень уютный магазин по продаже оргтехники"
        return context


   

class ContactsView(TemplateView):
    template_name = "main/contacts.html"

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Robot - Контакты магазина "
        context['content']="Контактная информация"
        context['text_on_page']="Наши контакты 105094, Россия, г.Москва, Семёновская набережная, д. 2/1, стр. 1, офис № 118 8 (800) 500-82-27 info@orgtehnics.ru Skype:Robot ICQ: 26302335 График работы: Пн.-Пт. с 10:00 до 18:00"
        return context




# def contacts(request):
#     context = {
#         "title": "Robot - Контакты магазина ",
#         "content": "Контактная информация  ",
#         # "text_page": "Наши контакты 105094, Россия, г.Москва, Семёновская набережная, д. 2/1, стр. 1, офис № 118 8 (800) 500-82-27 info@orgtehnics.ru Skype:Robot ICQ: 26302335 График работы: Пн.-Пт. с 10:00 до 18:00",
#     }
#     return render(request, "main/contacts.html", context)



class PaymentView(TemplateView):
    template_name = "main/payment.html"

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Способы оплаты  и доставки товара магазины Robot"
        context['content']="Способы оплаты  и доставки товара магазины Robot"
        context['text_page']="Доставка осуществляется разными способами"
        return context


# def payment(request):
#     context = {
#         "title": "Robot - Способы оплаты  и доставки товара ",
#         "content": "Способы оплаты  и доставки товара магазины Robot",
#         "text_page": "Доставка осуществляется разными способами",
#     }

#     return render(request, "main/payment.html", context)



class NewsView(TemplateView):
    template_name = "main/news.html"
    

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Robot - Контакты магазина "
        context['content']="Новости из сферы продаж/рекламные акции"
        context['text_page']="Новости магазина продаж постоянно меняются. Для просмотра видео с магазина, пожалуйста перейдите по ссылке ниже ⏬⏬⏬ "
        return context


# def news(request):
#     context = {
#         "title": "Robot - Новости магазина",
#         "content": "Новости из сферы продаж/рекламные акции",
#         "text_page": "Новости разные",
#     }

#     return render(request, "main/news.html", context)



class ReviewsView(TemplateView):
    template_name = "main/reviews.html"

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Robot - Отзывы о магазине"
        context['content']="Отзывы наших клиентов"
        context['text_page']="Список отзывов "
        return context



class TelegrambotView(TemplateView):
    template_name = "main/telegrambot.html"

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Robot - telegrambot"
        context['content']="Свяжись со мной по ссылки  https://yandex.ru/search?text=магазин+оргтехники+москва&lr=66&src=suggest_Pers"
        context['text_page']="Привет я телеграмм бот компании Robot"
        return context


# def reviews(request):
#     context = {
#         "title": "Robot - Отзывы о магазине",
#         "content": "Отзывы наших клиентов",
#         "text_page": "Список отзывов  ",
#     }

#     return render(request, "main/reviews.html", context)
