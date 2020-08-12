from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'name', 'class_number', 'grade',
                    'address', 'telephone', 'wx', 'qq', 'photo', 'role']
    list_filter = ['class_number', 'grade']
    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1] = (_('Personal info'),
                    {'fields': ('name', 'email', 'class_number', 'grade',
                                'address', 'telephone', 'wx', 'qq', 'photo', 'role')})

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role_id == 3:
            return qs
        elif request.user.role_id == 1:
            return qs.filter(role_id=2)
        else:
            return qs.filter(id=request.user.id)
