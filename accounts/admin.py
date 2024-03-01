from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'phone', 'is_admin')
    list_filter = ('is_active', 'is_admin')
    list_per_page = 30

    fieldsets = (
        (_('مشخصات شخصی'), {'fields': ('phone', 'username', 'fullname', 'email', 'password')}),
        (_('درسترسی'), {'fields': ('is_active', 'is_admin', 'is_superuser', 'groups', 'user_permissions')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'email', 'username', 'password1', 'password2')
        }),
    )

    search_fields = ('phone', 'email', 'username', 'fullname')
    ordering = ('phone', 'username')
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_field['is_superuser'].disabled = True
        return form


admin.site.register(User, UserAdmin)
