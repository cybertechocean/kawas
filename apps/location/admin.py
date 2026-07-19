from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import OpeningHours


@admin.register(OpeningHours)
class OpeningHoursAdmin(ModelAdmin):
    list_display = ['get_day_display', 'open_time', 'close_time', 'is_closed', 'note']
    list_editable = ['open_time', 'close_time', 'is_closed']
    ordering = ['day']
