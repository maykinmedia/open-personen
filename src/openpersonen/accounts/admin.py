from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from hijack_admin.admin import HijackUserAdminMixin
from rest_framework.authtoken.admin import TokenAdmin

from .models import User


@admin.register(User)
class _UserAdmin(UserAdmin, HijackUserAdminMixin):
    list_display = UserAdmin.list_display + ("hijack_field",)


TokenAdmin.raw_id_fields = ['user']
