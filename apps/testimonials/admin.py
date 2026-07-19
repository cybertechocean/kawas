from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ['name', 'title', 'rating', 'source', 'is_featured', 'is_active', 'ordering']
    list_editable = ['is_featured', 'is_active', 'ordering']
    list_filter = ['rating', 'is_featured', 'is_active', 'source']
    search_fields = ['name', 'title', 'review']
    ordering = ['ordering', '-created_at']
