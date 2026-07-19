from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display
from .models import HeroSlide


@admin.register(HeroSlide)
class HeroSlideAdmin(ModelAdmin):
    list_display = ['slide_preview', 'title', 'badge', 'is_active', 'ordering']
    list_filter = ['is_active']
    list_editable = ['is_active', 'ordering']
    search_fields = ['title', 'subtitle', 'badge']
    ordering = ['ordering']
    readonly_fields = ['created_at']

    fieldsets = [
        ("Slide Content", {
            "fields": ["title", "subtitle", "badge", "description"],
            "description": "Enter the main headline in 'Title'. The 'Subtitle' appears in gold italic beneath it. The 'Badge' is the small pill shown above the headline (e.g. 'Halal Certified · 100% Alcohol-Free').",
        }),
        ("Background Image", {
            "fields": ["image"],
            "description": "Upload a high-quality landscape photo (recommended: 1920×1080 px). Leave blank to use the elegant geometric pattern background.",
        }),
        ("Call-to-Action Buttons", {
            "fields": ["cta_primary_text", "cta_primary_url", "cta_secondary_text", "cta_secondary_url"],
            "description": "Primary button appears in gold. Secondary button appears in WhatsApp green. Leave secondary text blank to hide it.",
        }),
        ("Visibility & Order", {
            "fields": ["is_active", "ordering", "created_at"],
            "description": "Lower ordering number = shown first. Only active slides are displayed on the website.",
        }),
    ]

    @display(description="Preview")
    def slide_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:40px;width:70px;object-fit:cover;border-radius:4px;">',
                obj.image.url
            )
        return format_html('<span style="opacity:0.4;font-size:11px;">No image</span>')
