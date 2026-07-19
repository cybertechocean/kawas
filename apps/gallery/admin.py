from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(ModelAdmin):
    list_display = ['preview', 'title', 'is_featured', 'is_active', 'ordering']
    list_editable = ['is_featured', 'is_active', 'ordering']
    list_filter = ['is_featured', 'is_active']
    search_fields = ['title', 'caption']
    ordering = ['ordering', '-created_at']

    @display(description="Preview")
    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;width:60px;object-fit:cover;border-radius:8px;">', obj.image.url)
        return "—"
