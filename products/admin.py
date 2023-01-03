from django.contrib import admin
from django.utils.safestring import mark_safe

from products.models import *


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'slug']
    list_display_links = ['title']
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'description')
    search_fields = ['title', 'description']
    list_filter = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_photo', 'description', 'short_description', 'price', 'quantity', 'category', 'slug']
    list_display_links = ['title', 'category']
    list_filter = ['title', 'price', 'category']
    search_fields = ['title', 'description', 'short_description']
    fields = ('title', 'slug', 'get_photo', 'image', 'description',
              'short_description', 'price', 'quantity', 'category')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('get_photo',)

    def get_photo(self, object):
        return mark_safe(f"<img src='{object.image.url}' width=100")

    get_photo.short_description = 'Installed photo'


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('product', 'quantity', 'created_timestamp')
    extra = 0


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Basket)
