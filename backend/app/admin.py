from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class AdminCustomUser(UserAdmin):
    model = CustomUser
    list_display = ['id','email','is_active']
    list_display_links = ('id','email', 'is_active',)
    fieldsets = (
        (None, {'fields':('email','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions',)
        }),
    )
    search_fields = ['email',]
    ordering = ['email']

admin.site.register(CustomUser,AdminCustomUser)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Loan)