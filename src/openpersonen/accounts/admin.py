from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from hijack_admin.admin import HijackUserAdminMixin
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token

from .models import User


@admin.register(User)
class _UserAdmin(UserAdmin, HijackUserAdminMixin):
    list_display = UserAdmin.list_display + ("hijack_field",)


admin.site.unregister(Token)


@admin.register(Token)
class _TokenAdmin(TokenAdmin):
    raw_id_fields = ("user",)
    fields = (
        "key",
        "user",
    )
    readonly_fields = ("key",)
