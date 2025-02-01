
from django.db import models

from goods1.models import products
from users.models import User

# Create your models here.


class OrderItemQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0
    
  

class Order(models.Model): # таблица заказов
    user = models.ForeignKey(to=User, null=True, default=None, on_delete=models.SET_DEFAULT, verbose_name='Пользователь сайта')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    requires_delivery =models.BooleanField(default=False, verbose_name='Требуется доставка товара')
    delivery_address = models.TextField(max_length=25,  blank=True, null=True, verbose_name="Адрес доставки покупателя товара")
    phone_number = models.CharField(max_length=25, verbose_name="Номер телефона покупателя")
    payment_on_get = models.BooleanField(default=False, verbose_name='Оплата при получении товара')
    is_paid = models.BooleanField(default=False, verbose_name="Товар оплачен")
    status = models.CharField(max_length=70, default="Заказ находится в обработке", verbose_name="Статус заказа")
    
    class Meta:
        db_table ='order'
        verbose_name = 'Заказ' 
        verbose_name_plural = 'Заказы'
        ordering = ("id",)
    
    def __str__(self):
        return f"Заказ покупателя под № {self.pk} | Покупатель товара {self.user.first_name}{self.user.last_name} с ником {self.user.username}"
    
class OrderItem(models.Model): # таблица заказанных товаров
    order = models.ForeignKey(to=Order, null=True, on_delete=models.CASCADE, verbose_name='Заказ покупателя')
    product = models.ForeignKey(to=products, null=True, on_delete=models.SET_DEFAULT, verbose_name='Товар', default=None)
    name = models.CharField(max_length=170, verbose_name="Название товара")
    price = models.DecimalField( max_digits=7, decimal_places=2, verbose_name='Цена товара(рубль)')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество товара(шт.)')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи товара')
    
    
    class Meta: # класс meta
        db_table ='order_item'
        verbose_name = 'Проданный товар магазина'
        verbose_name_plural = 'Проданные товары магазина'
        ordering =('id',)
        
    objects = OrderItemQueryset().as_manager()  # создание обьетка пользователя заказа c обращением queryset.
        
        
    
    def products_price(self):  # просичтать какие заказы сделанны пользователем
        return round(self.product.sell_disc_price() * self.quantity, 2)
    
    
    def __str__(self): # создание обьетка пользователя заказа
        return f'Товар {self.name} | Заказ под № {self.order.pk}'