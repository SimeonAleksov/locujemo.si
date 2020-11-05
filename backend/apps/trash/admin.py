from django.contrib import admin

from .models import Product, RecycleGroup


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'product_name', 'recycle_group_id')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'


@admin.register(RecycleGroup)
class RecycleGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'group_name', 'group_description')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
