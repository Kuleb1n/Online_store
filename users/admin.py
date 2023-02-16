from django.contrib import admin
from django.utils.safestring import mark_safe

from users.models import *
from products.admin import BasketAdminInline


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'get_photo', 'date_joined',
                    'is_staff', 'is_the_email_confirmed']
    list_display_links = ['username', 'email']
    search_fields = ['username', 'email']
    list_filter = ['date_joined', 'is_staff']
    fields = ('username', 'email', 'first_name', 'last_name', 'get_photo', 'user_photo',
              'is_staff', 'is_active', 'is_superuser')
    inlines = (BasketAdminInline,)
    readonly_fields = ('get_photo',)

    def get_photo(self, object):
        if object.user_photo:
            return mark_safe(f"<img src='{object.user_photo.url}' width=100")
        else:
            return 'The user is missing a photo'

    get_photo.short_description = "User's installed photo"


admin.site.register(User, UserAdmin)


@admin.register(EmailConfirmation)
class EmailConfirmationAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'expiration')
    fields = ('code', 'user', 'expiration')
    readonly_fields = ('code',)
