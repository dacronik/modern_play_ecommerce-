from django.contrib import admin
from .models import Payment, Order, OrderProduct
# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'payment_id',
        'payment_method',
        'amount_id',
        'status',
        'created_at',
    )
    list_filter = ('user', 'created_at')
    date_hierarchy = 'created_at'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'payment',
        'order_number',
        'first_name',
        'last_name',
        'phone',
        'email',
        'addres_line_1',
        'addres_line_2',
        'state',
        'city',
        'country',
        'order_note',
        'order_total',
        'tax',
        'status',
        'ip',
        'is_ordered',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'user',
        'payment',
        'is_ordered',
        'created_at',
        'updated_at',
    )
    date_hierarchy = 'created_at'

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'payment',
        'user',
        'product',
        'variation',
        'color',
        'size',
        'quantity',
        'product_price',
        'ordered',
        'created_ad',
        'update_at',
    )
    list_filter = (
        'order',
        'payment',
        'user',
        'product',
        'variation',
        'ordered',
        'created_ad',
        'update_at',
    )