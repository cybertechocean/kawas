import uuid
from django.db import models
from cloudinary.models import CloudinaryField


class GalleryImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=True)
    caption = models.TextField(blank=True)
    image = CloudinaryField('image', folder='kawas/gallery', blank=True, null=True)
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

    @property
    def image_url(self):
        """Full Cloudinary URL for the gallery image."""
        if self.image:
            return self.image.url
        return ''
