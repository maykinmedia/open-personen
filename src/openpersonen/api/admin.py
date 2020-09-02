from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .client import StufBGClient


@admin.register(StufBGClient)
class StufBGClientAdmin(SingletonModelAdmin):
    pass
