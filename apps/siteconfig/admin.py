from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import display
from .models import SiteConfiguration, Announcement


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(ModelAdmin):
    list_display = ['site_name', 'phone', 'email']
    fieldsets = [
        ("Identity", {
            "fields": ["site_name", "site_tagline", "site_description"],
        }),
        ("Contact Information", {
            "fields": ["phone", "whatsapp", "email", "address"],
        }),
        ("Social Media", {
            "fields": ["facebook_url", "instagram_url", "tiktok_url"],
        }),
        ("Google Maps", {
            "fields": ["google_maps_url", "google_maps_embed"],
        }),
        ("SEO", {
            "fields": ["meta_title", "meta_description"],
        }),
        ("Footer", {
            "fields": ["footer_about", "footer_tagline"],
        }),
        ("Features", {
            "fields": ["show_prayer_times", "online_ordering_enabled"],
        }),
    ]

    def has_add_permission(self, request):
        return not SiteConfiguration.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Announcement)
class AnnouncementAdmin(ModelAdmin):
    list_display = ['text', 'is_active', 'ordering', 'created_at']
    list_filter = ['is_active']
    list_editable = ['is_active', 'ordering']
    search_fields = ['text']
    ordering = ['ordering']
