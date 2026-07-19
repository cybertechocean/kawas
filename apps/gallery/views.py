from django.shortcuts import render
from .models import GalleryImage


def gallery(request):
    images = GalleryImage.objects.filter(is_active=True)
    context = {
        'images': images,
        'page_title': "Gallery",
        'meta_description': "Experience KAWA'S Café through our gallery — premium coffee, artisan desserts, and the beautiful coastal café ambience in Nyali, Mombasa.",
    }
    return render(request, 'gallery/gallery.html', context)
