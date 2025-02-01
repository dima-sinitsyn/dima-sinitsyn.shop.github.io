from django.db import models
from django.http import request


from goods1.models import products
from users.models import User

# Create your models here.


class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0
    


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=products, on_delete=models.CASCADE, verbose_name='Товар магазина')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество товара')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления товара')

    class Meta: 
        db_table = 'cart'
        verbose_name = "Корзину"
        verbose_name_plural = "Корзины товаров"
        ordering = ("id",)
        
    objects = CartQueryset().as_manager()

    def products_price(self):
        return round(self.product.sell_disc_price() * self.quantity, 2)



    def __str__(self):
        if self.user:
            return f'Корзина товаров: Пользователя   {self.user.first_name} {self.user.last_name} | Товар {self.product.name} | Количество {self.quantity}'
            
        return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'
    