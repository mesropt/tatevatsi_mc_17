from django.contrib import admin
from users.models import User


class UserAdminClass(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')


admin.site.register(User, UserAdminClass)
