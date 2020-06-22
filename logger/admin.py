from django.contrib import admin

from .models import LogGroup, Log

admin.site.register(Log)
admin.site.register(LogGroup)
