
from itertools import product



from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from carts.models import Cart
from orders.forms import CreateOrderform
from orders.models import Order, OrderItem

# Create your views here.


@login_required
def create_order(request):
    if request.method == 'POST':
       form = CreateOrderform(data=request.POST)
       if form.is_valid():
           try:
               with transaction.atomic():
                    user =request.user  # создаем пользователя
                    cart_items = Cart.objects.filter(user=user)  # проверяем все корзины пользователя
                   
                    if cart_items.exists():   # создаем заказ через проверку
                        order = Order.objects.create(
                            user=user,
                            phone_number = form.cleaned_data['phone_number'],  # используем метод clened data
                            requires_delivery = form.cleaned_data['requires_delivery'],
                            delivery_address = form.cleaned_data['delivery_address'],
                            payment_on_get =  form.cleaned_data['payment_on_get'],
                              
                        )
                        # создаем заказы товаров записывая данные в таблицу заказов
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name     
                            price = cart_item.product.sell_disc_price()   # используем метод для цены товара со скидко или нет
                            quantity = cart_item.quantity
                            
                            if product.quantity < quantity :   # проверяем есть ли товары на складе количество нужное и если нет то исключение срабатывает
                                raise ValidationError(f'Недостаточное количество товара {name} на складе | В наличии - {product.quantity}')
                            
                            # создаем заказ 
                            OrderItem.objects.create(
                                order=order,
                                price=price,
                                quantity=quantity,
                                product=product,
                                name=name,  
                            )
                            product.quantity -= quantity  # проверяем есть ли товары на складе количество нужное
                            product.save()  # записываем транзакцию
                            
                        # очисткка корзины пользователя  полсе заказа
                        cart_items.delete()
                        
                        
                        messages.success(request, 'Ваш заказ оформлен') # выводится сообщение после формипррования заказа
                        return redirect('user:profile') # перенаправляем на профиль пользователя
           except ValidationError as e:
               messages.warning(request, str(e))
               return redirect('cart:order')
                        
    else:
        initial = {
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        
        form =  CreateOrderform(initial=initial)
        
    context = {
        'title': 'Robot оформление заказа',
        'form': form,
        'order': True,        
    }
        
             
    return render(request, 'orders/create_order.html', context=context)

