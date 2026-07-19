from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import HeroSlide


@admin.register(HeroSlide)
class HeroSlideAdmin(ModelAdmin):
    list_display = ['title', 'subtitle', 'is_active', 'ordering']
    list_filter = ['is_active']
    list_editable = ['is_active', 'ordering']
    search_fields = ['title', 'subtitle']
    ordering = ['ordering']
