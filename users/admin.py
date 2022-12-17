from django.contrib import admin
from users.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'user_photo', 'date_joined',
                    'is_staff']
    list_display_links = ['username', 'email']
    search_fields = ['username', 'email']
    list_filter = ['date_joined', 'is_staff']
    fields = ('username', 'email', 'first_name', 'last_name', 'user_photo',
              'is_staff', 'is_active', 'is_superuser')


admin.site.register(User, UserAdmin)
