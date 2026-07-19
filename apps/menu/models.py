import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=120)
    description = CKEditor5Field(config_name='default', blank=True)
    short_description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(800, 600)],
        format='WEBP',
        options={'quality': 85}
    )
    emoji = models.CharField(max_length=10, blank=True, help_text="Category emoji icon")
    icon = models.CharField(max_length=50, blank=True, help_text="Lucide icon name")
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ordering', 'name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('menu:category', kwargs={'slug': self.slug})


class MenuItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=220)
    short_description = models.CharField(max_length=255, blank=True)
    description = CKEditor5Field(config_name='extends', blank=True)
    ingredients = models.TextField(blank=True)
    allergens = models.TextField(blank=True)
    preparation_notes = models.TextField(blank=True)

    # Pricing
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Base price in KSh")
    price_display = models.CharField(max_length=50, blank=True, help_text="Override price display e.g. 'From KSh 400'")

    # Images
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    image_thumb = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 600)],
        format='WEBP',
        options={'quality': 85}
    )
    image_large = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200, 800)],
        format='WEBP',
        options={'quality': 90}
    )

    # Badges
    is_featured = models.BooleanField(default=False)
    is_best_seller = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    is_chefs_pick = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    # SEO
    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    ordering = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ordering', 'name']
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('menu:item_detail', kwargs={'slug': self.slug})

    def get_price_display(self):
        if self.price_display:
            return self.price_display
        return f"KSh {int(self.price):,}"

    def get_whatsapp_message(self):
        return f"👋 Hello KAWA'S Café!\n\nI am interested in your *{self.name}*.\n\nMenu Link: https://kawas.co.ke/menu/{self.slug}/\n\nThank you! 🙏"


class MenuVariant(models.Model):
    """Size/variant options for menu items (e.g. Small/Medium/Large)."""
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('single', 'Single'),
        ('double', 'Double'),
        ('regular', 'Regular'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='variants')
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering', 'size']
        verbose_name = "Menu Variant"
        verbose_name_plural = "Menu Variants"
        unique_together = [['menu_item', 'size']]

    def __str__(self):
        return f"{self.menu_item.name} — {self.get_size_display()} (KSh {int(self.price):,})"
