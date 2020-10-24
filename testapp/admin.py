from django.contrib import admin
from django.contrib import admin
from django.contrib import messages
from .models import *


@admin.register(System)
class PlatformAdmin(admin.ModelAdmin):
    class Meta:
        model = System