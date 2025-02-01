from django.contrib import admin
from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import User


# Register your models here.

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   
    list_display = [
        "first_name",
        "last_name",
        "username",
        "email",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "username",
        "email",
    ]
    inlines = [CartTabAdmin, OrderTabulareAdmin, ]
    
    actions = ["published", ]
    
    