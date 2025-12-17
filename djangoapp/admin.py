from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'category',
        'stock',
        'created_at',
    )
    list_filter = ('category',)
    search_fields = ('name',)
