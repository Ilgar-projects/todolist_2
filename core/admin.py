from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'last_login', 'date_joined')
    readonly_fields = ('last_login', 'date_joined')
    exclude = ('password',)


admin.site.register(User, UserAdmin)
