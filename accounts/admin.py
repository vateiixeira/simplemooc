from django.contrib import admin
from .models import User

class UsersAdmin(admin.ModelAdmin):
    list_display=['username', 'email', 'name', 'is_staff']
    search_fields= ['username', 'name', 'email']

admin.site.register(User, UsersAdmin)
# Register your models here.
