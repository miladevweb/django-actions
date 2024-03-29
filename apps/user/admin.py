from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'id',)
    ordering = ('-id',)

admin.site.register(User, UserAdmin)


