from django.contrib import admin
from products.models import *


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'slug']
    list_display_links = ['title']
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'description')
    search_fields = ['title', 'description']
    list_filter = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'description', 'short_description', 'price', 'quantity', 'category', 'slug']
    list_display_links = ['title', 'category']
    list_filter = ['title', 'price', 'category']
    search_fields = ['title', 'description', 'short_description']
    fields = ('title', 'slug', 'image', 'description', 'short_description', 'price', 'quantity', 'category')
    prepopulated_fields = {"slug": ("title",)}


class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'created_timestamp']
    list_display_links = ['user', 'product', ]


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
