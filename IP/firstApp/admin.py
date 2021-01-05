from django.contrib import admin
from .models import CarSpecs, CarPlan, Categories, Manufacturers, Products, Providers, Supplies, Accounts, Sellers, \
    Customers


class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ('category_name',)


class ProductsAdmin(admin.ModelAdmin):
    search_fields = ('product_name',)
    list_display = ['product_name', 'product_price']


class CustomersAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class ManufacturersAdmin(admin.ModelAdmin):
    search_fields = ('manufacturer_name',)


class ProvidersAdmin(admin.ModelAdmin):
    search_fields = ('provider_name',)


class SellersAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'position']
    list_filter = ['position']


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Manufacturers, ManufacturersAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Providers, ProvidersAdmin)
admin.site.register(Supplies)
admin.site.register(Accounts)
admin.site.register(Customers, CustomersAdmin)
admin.site.register(Sellers, SellersAdmin)
