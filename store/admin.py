from django.contrib import admin
from .models import Product, Variation

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

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'variation_category',
        'variation_value',
        'is_active',
        'created_date',
    )
    list_filter = ('product','variation_category', 'variation_value', 'is_active', )
    list_editable = ('is_active',)
    