from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from .models import Category, MenuItem


def menu_home(request):
    """Main menu page with all categories and featured items."""
    categories = Category.objects.filter(is_active=True).prefetch_related('items')
    active_slug = request.GET.get('cat', '')
    search_query = request.GET.get('q', '')

    if active_slug:
        active_category = get_object_or_404(Category, slug=active_slug, is_active=True)
        items = MenuItem.objects.filter(
            category=active_category,
            is_active=True,
        ).select_related('category').prefetch_related('variants')
    else:
        active_category = None
        # Only show items whose parent category is also active
        items = MenuItem.objects.filter(
            is_active=True,
            category__is_active=True,
        ).select_related('category').prefetch_related('variants')

    if search_query:
        items = items.filter(
            Q(name__icontains=search_query) |
            Q(short_description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    context = {
        'categories': categories,
        'items': items,
        'active_category': active_category,
        'search_query': search_query,
        'page_title': "Our Menu",
        'meta_description': "Explore KAWA'S Café full menu — specialty coffee, matcha, frappes, fresh juices, milkshakes, and artisan desserts in Nyali, Mombasa.",
    }
    return render(request, 'menu/menu.html', context)


def category_detail(request, slug):
    """Category-specific menu page."""
    category = get_object_or_404(Category, slug=slug, is_active=True)
    items = MenuItem.objects.filter(
        category=category,
        is_active=True,
    ).prefetch_related('variants')
    categories = Category.objects.filter(is_active=True)

    context = {
        'category': category,
        'items': items,
        'categories': categories,
        'active_category': category,
        'page_title': category.name,
        'meta_description': category.short_description or f"Explore our {category.name} menu at KAWA'S Café.",
    }
    return render(request, 'menu/category.html', context)


def item_detail(request, slug):
    """Individual menu item detail page."""
    item = get_object_or_404(MenuItem, slug=slug, is_active=True)
    related_items = MenuItem.objects.filter(
        category=item.category,
        is_active=True,
        category__is_active=True,
    ).exclude(pk=item.pk)[:6]

    import urllib.parse
    whatsapp_msg = urllib.parse.quote(item.get_whatsapp_message())
    whatsapp_url = f"https://wa.me/254119000999?text={whatsapp_msg}"

    context = {
        'item': item,
        'related_items': related_items,
        'whatsapp_url': whatsapp_url,
        'page_title': item.name,
        'meta_title': item.meta_title or f"{item.name} — KAWA'S Café",
        'meta_description': item.meta_description or item.short_description or f"Order {item.name} at KAWA'S Café, Nyali Mombasa. {item.get_price_display()}",
    }
    return render(request, 'menu/item_detail.html', context)


def search_ajax(request):
    """HTMX-powered live search."""
    q = request.GET.get('q', '').strip()
    if len(q) < 2:
        return render(request, 'menu/partials/search_results.html', {'items': [], 'query': q})

    items = MenuItem.objects.filter(
        Q(name__icontains=q) |
        Q(short_description__icontains=q) |
        Q(category__name__icontains=q),
        is_active=True,
        category__is_active=True,
    ).select_related('category')[:12]

    return render(request, 'menu/partials/search_results.html', {'items': items, 'query': q})
