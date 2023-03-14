from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.


@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'username',
        'date_joined',
        'last_login',
        'is_admin',
        'is_staff',
        'is_active',
        'is_superadmin',
    )
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    fieldsets = ()
    list_filter = (
        'date_joined',
        'last_login',
        'is_admin',
        'is_staff',
        'is_active',
        'is_superadmin',
    )
