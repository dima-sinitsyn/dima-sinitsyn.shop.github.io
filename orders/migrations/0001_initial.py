# Generated by Django 5.1 on 2024-09-26 08:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods1', '0002_alter_products_country_alter_products_manufacturer_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('requires_delivery', models.BooleanField(default=False, verbose_name='Требуется доставка товара')),
                ('delivery_address', models.TextField(blank=True, max_length=25, null=True, verbose_name='Адрес доставки покупателя товара')),
                ('phone_number', models.CharField(max_length=25, verbose_name='Номер телефона покупателя')),
                ('payment_on_get', models.BooleanField(default=False, verbose_name='Оплата при получении товара')),
                ('is_paid', models.CharField(default=False, verbose_name='Товар оплачен')),
                ('status', models.CharField(default='Заказ находится в обработке', max_length=70, verbose_name='Статус заказа')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь сайта')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=170, verbose_name='Название товара')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена товара(рубль)')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество товара(шт.)')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, db_index=True, max_length=150, verbose_name='Дата продажи товара')),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='orders.order', verbose_name='Заказ покупателя')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods1.products', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Проданный товар магазина',
                'verbose_name_plural': 'Проданные товары магазина',
                'db_table': 'order_item',
            },
        ),
    ]
