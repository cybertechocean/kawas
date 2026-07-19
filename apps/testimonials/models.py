import uuid
from django.db import models
from cloudinary.models import CloudinaryField


class Testimonial(models.Model):
    RATING_CHOICES = [(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, help_text="e.g. Coffee Enthusiast, Regular Customer")
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    avatar = CloudinaryField('image', folder='kawas/testimonials', blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, default="Google Reviews")
    is_featured = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordering', '-created_at']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} — {'⭐' * self.rating}"

    @property
    def avatar_url(self):
        """Full Cloudinary URL for the avatar."""
        if self.avatar:
            return self.avatar.url
        return ''
