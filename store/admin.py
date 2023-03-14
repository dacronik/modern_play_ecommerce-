from django.contrib import admin
from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'price',
        'stock',
        'is_available',
        'category',
        'modified_date',
    )
    list_filter = (
        'product_name',
        'is_available',
        'category',
        'modified_date',
    )
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ('product_name',)}
