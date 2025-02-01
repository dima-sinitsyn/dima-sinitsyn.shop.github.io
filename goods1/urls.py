
from django.urls import path
from goods1 import views 

app_name ='goods1'

urlpatterns = [
    path('search/', views.CatalogView.as_view(), name='search'),
    path('<slug:category_slug>/', views.CatalogView.as_view(), name='index'),
    # path('<slug:category_slug>/<int:page>/', views.catalog, name='index'),
    # path('product/<int:product_id>', views.product, name='product'),
    path('product/<slug:product_slug>', views.ProductView.as_view(), name='product'),
   
]
