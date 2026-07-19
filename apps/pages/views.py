import urllib.parse
from django.shortcuts import render
from apps.menu.models import Category, MenuItem
from apps.gallery.models import GalleryImage
from apps.testimonials.models import Testimonial
from apps.location.models import OpeningHours
from apps.core.models import HeroSlide
from .models import FAQ, PrivacyPolicy, TermsOfService


def home(request):
    hero_slides = HeroSlide.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    featured_items = MenuItem.objects.filter(is_active=True, is_featured=True)[:8]
    gallery_images = GalleryImage.objects.filter(is_active=True, is_featured=True)[:8]
    testimonials = Testimonial.objects.filter(is_active=True, is_featured=True)[:6]
    opening_hours = OpeningHours.objects.all()

    context = {
        'hero_slides': hero_slides,
        'categories': categories,
        'featured_items': featured_items,
        'gallery_images': gallery_images,
        'testimonials': testimonials,
        'opening_hours': opening_hours,
        'page_title': "Home",
    }
    return render(request, 'pages/home.html', context)


def menu_page(request):
    categories = Category.objects.filter(is_active=True)
    items = MenuItem.objects.filter(is_active=True).select_related('category').prefetch_related('variants')
    context = {
        'categories': categories,
        'items': items,
        'page_title': "Our Menu",
        'meta_description': "Explore KAWA'S full menu — specialty coffees, matcha, frappes, fresh juices, milkshakes, Alcohol-Free Mojitos, and artisan desserts in Nyali, Mombasa.",
    }
    return render(request, 'menu/menu.html', context)


def gallery_page(request):
    images = GalleryImage.objects.filter(is_active=True)
    context = {
        'images': images,
        'page_title': "Gallery",
        'meta_description': "Explore KAWA'S Café through our gallery — premium coffee, artisan desserts, and beautiful café moments in Nyali, Mombasa.",
    }
    return render(request, 'gallery/gallery.html', context)


def about(request):
    context = {
        'page_title': "Our Story",
        'meta_description': "Discover the story behind KAWA'S Café — a premium halal specialty coffee house inspired by Dubai and Istanbul, rooted in the coastal charm of Nyali, Mombasa.",
    }
    return render(request, 'pages/about.html', context)


def visit(request):
    opening_hours = OpeningHours.objects.all()
    context = {
        'opening_hours': opening_hours,
        'page_title': "Visit Us",
        'meta_description': "Find KAWA'S Café at Mount Kenya Road, Nyali, Mombasa. Get directions, opening hours, phone number, and WhatsApp contact.",
    }
    return render(request, 'pages/visit.html', context)


def contact(request):
    context = {
        'page_title': "Contact Us",
        'meta_description': "Get in touch with KAWA'S Café. Call us, WhatsApp us, or visit us at Mount Kenya Road, Nyali, Mombasa, Kenya.",
    }
    return render(request, 'pages/contact.html', context)


def faqs(request):
    faqs_list = FAQ.objects.filter(is_active=True)
    context = {
        'faqs': faqs_list,
        'page_title': "Frequently Asked Questions",
        'meta_description': "Find answers to common questions about KAWA'S Café — our halal certification, menu, opening hours, location, and more.",
    }
    return render(request, 'pages/faqs.html', context)


def privacy_policy(request):
    policy = PrivacyPolicy.objects.first()
    context = {
        'policy': policy,
        'page_title': "Privacy Policy",
    }
    return render(request, 'pages/privacy_policy.html', context)


def terms(request):
    terms_obj = TermsOfService.objects.first()
    context = {
        'terms': terms_obj,
        'page_title': "Terms of Service",
    }
    return render(request, 'pages/terms.html', context)


def breakfast(request):
    try:
        category = Category.objects.get(slug='breakfast', is_active=True)
        items = MenuItem.objects.filter(category=category, is_active=True).prefetch_related('variants')
    except Category.DoesNotExist:
        category = None
        items = []

    context = {
        'category': category,
        'items': items,
        'page_title': "Breakfast Menu",
        'meta_description': "Start your morning right at KAWA'S Café with our freshly prepared breakfast menu in Nyali, Mombasa.",
    }
    return render(request, 'pages/breakfast.html', context)
