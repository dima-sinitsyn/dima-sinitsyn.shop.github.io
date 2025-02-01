

from django.db import models
from django.urls import reverse

# Create your models here.

class categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название товара')
    slug =models.SlugField(max_length=250, blank=True, null=True, verbose_name='Url товара')
    
    
    class Meta():
        db_table = 'category'
        verbose_name = 'категорию товара'
        verbose_name_plural = 'категории товара'
        
    def __str__(self):
        return self.name
    
        
        
        

class products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название товара')
    slug =models.SlugField(max_length=250, blank=True, null=True, verbose_name='Url товара')
    description = models.TextField(blank=True, null=True, verbose_name='Описание товара')
    country = models.TextField(max_length=150, blank=True, null=True, verbose_name='Страна, где проиведен данный товар')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена товара(рубль)')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Цена товара со скидкой')
    super_discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Супер скидка на товар')
    image = models.ImageField(upload_to='goods1_images', blank=True, null=True, verbose_name='Изображение товара')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество товара(шт.)')
    manufacturer = models.TextField(max_length=150, blank=True, null=True, verbose_name='Производитель товара')
    product_brand = models.TextField(max_length=150, blank=True, null=True, verbose_name='Бренд товара')
    published = models.DateTimeField(max_length=150, auto_now_add=True, verbose_name='Дата добавления товара', db_index=True)
    rating_product = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, verbose_name='Рейтинг товара от 1 ⭐ до 5 ⭐')
    article = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, verbose_name='Артикул товара')
    category = models.ForeignKey(to=categories, on_delete=models.CASCADE, verbose_name='категория товара')
    
    
    class Meta():
        db_table = 'product'
        verbose_name = 'Товар '
        verbose_name_plural = 'Товары '
        ordering = ('id', )
        
        
    def __str__(self):
        return f'{self.name} Количество товара - {self.quantity}'
    
    def display_id(self):
        return f"{self.id:04}"
    
    def sell_disc_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        elif self.super_discount:
            return round(self.price - self.price*self.super_discount/100, 2)
        return self.price
     
    def number_aricle(self):
        if self.article:
            return self.id*1000
        
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    
    


# class reviews(models.Model):
#     name = models.CharField(max_length=150, unique=True, verbose_name='Отзыв')
#     description = models.TextField(blank=True, null=True, verbose_name='Описание отзыва')
#     published = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления товара', db_index=True)
#     number = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, verbose_name='номер отзыва')


#     class Meta():
#         db_table = 'reviews'
#         verbose_name = 'Отзыв'
#         verbose_name_plural = 'Отзывы '
#         ordering = ('number', )