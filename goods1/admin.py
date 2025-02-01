from django.contrib import admin
from goods1.models import categories, products

# from goods1.views import reviews
# Register your models here.

# admin.site.register(categories)  один из спсосбов регитсрации приложения который не позволяет вносить изменения в приложении
# admin.site.register(products)

# admin.site.register(reviews)


@admin.register(categories)
class categoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",]

@admin.register(products)
class productsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
        
        "price",
        "discount",
        "super_discount",
        "quantity",
        "country",
        "product_brand",
        "manufacturer",
    ]
    list_editable = [
        "price",
        "discount",
        "super_discount",
        "quantity",
    ]
    search_fields = [
        "name",
        "description",
        
    ]
    list_filter = [
        "price",
        "discount",
        "super_discount",
        "category",
    ]
    fields = [
        ("name",
        "slug"),
        "category",
        
        "description",
        ("price",
        "quantity"),
        ("discount",
        "super_discount"),
       
        ("country",
        "manufacturer",
        "product_brand"),
        ("rating_product",
        "article"),
        "image",
       
    ]
