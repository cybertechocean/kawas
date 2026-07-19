import uuid
from django.db import models
from cloudinary.models import CloudinaryField
from django_ckeditor_5.fields import CKEditor5Field


class HeroSlide(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, help_text="Main headline — e.g. 'Crafted With Love.'")
    subtitle = models.CharField(max_length=255, blank=True, help_text="Gold italic sub-headline — e.g. 'Served With Excellence.'")
    badge = models.CharField(max_length=150, blank=True, help_text="Small badge above headline — e.g. 'Halal Certified · 100%% Alcohol-Free'")
    description = models.TextField(blank=True, help_text="Optional body text shown beneath the headline.")
    image = CloudinaryField('image', folder='kawas/hero', blank=True, null=True, help_text="Background photo. Leave blank for the elegant pattern background.")
    cta_primary_text = models.CharField(max_length=50, default="Explore Our Menu")
    cta_primary_url = models.CharField(max_length=200, default="/menu/")
    cta_secondary_text = models.CharField(max_length=50, blank=True, default="Order on WhatsApp")
    cta_secondary_url = models.CharField(max_length=200, blank=True, default="https://wa.me/254119000999")
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordering', 'created_at']
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Slides"

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        """Full Cloudinary URL for the hero image."""
        if self.image:
            return self.image.url
        return ''
