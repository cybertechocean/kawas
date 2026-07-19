import uuid
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class SiteConfiguration(models.Model):
    """Global site settings — only one instance should exist."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Identity
    site_name = models.CharField(max_length=100, default="KAWA'S Café")
    site_tagline = models.CharField(max_length=255, default="Crafted With Love")
    site_description = models.TextField(default="Premium Specialty Coffee, Artisan Desserts & Halal Dining in Nyali, Mombasa")

    # Contact
    phone = models.CharField(max_length=20, default="+254 119 000 999")
    whatsapp = models.CharField(max_length=20, default="254119000999")
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, default="Mount Kenya Road, Nyali, Mombasa, Kenya")

    # Social Media
    facebook_url = models.URLField(blank=True, default="https://facebook.com/kawa_ske")
    instagram_url = models.URLField(blank=True, default="https://instagram.com/kawa_ske")
    tiktok_url = models.URLField(blank=True, default="https://tiktok.com/@kawa_ske")
    google_maps_url = models.URLField(blank=True, default="https://maps.google.com/?q=Kawa%27s+Nyali+Mombasa")
    google_maps_embed = models.TextField(blank=True, help_text="Google Maps iframe embed code")

    # SEO
    meta_title = models.CharField(max_length=70, default="KAWA'S Café — Premium Coffee & Desserts in Nyali, Mombasa")
    meta_description = models.CharField(max_length=160, default="KAWA'S Café offers premium specialty coffee, artisan matcha, halal desserts, and a luxury café experience in Nyali, Mombasa, Kenya.")

    # Footer
    footer_about = CKEditor5Field(config_name='default', blank=True)
    footer_tagline = models.CharField(max_length=255, default="Crafted With Love. Served With Excellence.")

    # Feature flags
    show_prayer_times = models.BooleanField(default=False)
    online_ordering_enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return "Site Configuration"

    @classmethod
    def get_config(cls):
        obj, _ = cls.objects.get_or_create(pk=cls.objects.first().pk if cls.objects.exists() else uuid.uuid4())
        return obj


class Announcement(models.Model):
    """Top-bar announcements / banners."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    link_text = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    bg_color = models.CharField(max_length=20, default="#3E2723", help_text="CSS color for background")
    ordering = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordering', '-created_at']
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"

    def __str__(self):
        return self.text[:60]
