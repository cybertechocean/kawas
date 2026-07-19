import uuid
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit


class GalleryImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=True)
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')
    image_thumb = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 600)],
        format='WEBP',
        options={'quality': 85}
    )
    image_large = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1400, 1000)],
        format='WEBP',
        options={'quality': 90}
    )
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordering', '-created_at']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.title or f"Gallery Image {self.pk}"
