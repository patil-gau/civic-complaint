from django.contrib import admin
from users.models import Users
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = Users
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    search_fields = ('email', 'name', 'phone',)
    list_filter = ('email', 'name', 'phone', 'is_active','is_staff','role')
    list_display = ('email', 'name', 'is_active','is_staff','role')
    fieldsets = (
        (None, {'fields': ('email', 'name','phone','state_id','city_id','role','password','country')}),
        ('Permissions', {'fields': ('is_active','is_staff')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone','state_id', 'city_id' ,'role' ,'country', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
    ordering = ('role',)


admin.site.register(Users, UserAdminConfig)