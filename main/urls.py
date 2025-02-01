
from django.urls import path
from main import views 

app_name ='main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('reviews/', views.ReviewsView.as_view(), name='reviews'),
    path('telegrambot/', views.TelegrambotView.as_view(), name='telegrambot'),
]
 