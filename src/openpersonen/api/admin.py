from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import StufBGClient


@admin.register(StufBGClient)
class StufBGClientAdmin(SingletonModelAdmin):
    pass
