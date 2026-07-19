import uuid
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from django_ckeditor_5.fields import CKEditor5Field


class HeroSlide(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hero/')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1920, 1080)],
        format='WEBP',
        options={'quality': 85}
    )
    cta_primary_text = models.CharField(max_length=50, default="Explore Our Menu")
    cta_primary_url = models.CharField(max_length=200, default="/menu/")
    cta_secondary_text = models.CharField(max_length=50, default="Order on WhatsApp")
    cta_secondary_url = models.CharField(max_length=200, default="https://wa.me/254119000999")
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordering', 'created_at']
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Slides"

    def __str__(self):
        return self.title
