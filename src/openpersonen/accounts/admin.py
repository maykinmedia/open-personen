from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin

from hijack_admin.admin import HijackUserAdminMixin
from rest_framework.authtoken.admin import TokenAdmin as _TokenAdmin
from rest_framework.authtoken.models import Token

from .models import User


@admin.register(User)
class UserAdmin(_UserAdmin, HijackUserAdminMixin):
    list_display = _UserAdmin.list_display + ("hijack_field",)


admin.site.unregister(Token)


@admin.register(Token)
class TokenAdmin(_TokenAdmin):
    raw_id_fields = ("user",)
    fields = (
        "key",
        "user",
    )
    readonly_fields = ("key",)
