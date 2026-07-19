from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from unfold.decorators import display
from .models import Category, MenuItem, MenuVariant


class MenuVariantInline(TabularInline):
    model = MenuVariant
    extra = 1
    fields = ['size', 'price', 'is_available', 'ordering']


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'slug', 'item_count', 'is_active', 'ordering']
    list_filter = ['is_active']
    list_editable = ['is_active', 'ordering']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['ordering', 'name']
    fieldsets = [
        ("Category Details", {
            "fields": ["name", "slug", "short_description", "description", "emoji", "icon"],
        }),
        ("Image", {
            "fields": ["image"],
        }),
        ("Settings", {
            "fields": ["is_active", "ordering"],
        }),
    ]

    @display(description="Items")
    def item_count(self, obj):
        return obj.items.filter(is_active=True).count()


@admin.register(MenuItem)
class MenuItemAdmin(ModelAdmin):
    list_display = ['name', 'category', 'price_formatted', 'is_featured', 'is_best_seller', 'is_available', 'is_active', 'ordering']
    list_filter = ['category', 'is_featured', 'is_best_seller', 'is_new_arrival', 'is_available', 'is_active']
    list_editable = ['is_featured', 'is_best_seller', 'is_available', 'is_active', 'ordering']
    search_fields = ['name', 'slug', 'short_description']
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ['category']
    ordering = ['category', 'ordering', 'name']
    inlines = [MenuVariantInline]
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ("Item Details", {
            "fields": ["category", "name", "slug", "short_description", "description"],
        }),
        ("Pricing", {
            "fields": ["price", "price_display"],
        }),
        ("Image", {
            "fields": ["image"],
        }),
        ("Badges & Status", {
            "fields": ["is_featured", "is_best_seller", "is_new_arrival", "is_chefs_pick", "is_available", "is_active", "ordering"],
        }),
        ("Recipe Details", {
            "fields": ["ingredients", "allergens", "preparation_notes"],
        }),
        ("SEO", {
            "fields": ["meta_title", "meta_description"],
        }),
        ("Timestamps", {
            "fields": ["created_at", "updated_at"],
        }),
    ]

    @display(description="Price")
    def price_formatted(self, obj):
        return f"KSh {int(obj.price):,}"


@admin.register(MenuVariant)
class MenuVariantAdmin(ModelAdmin):
    list_display = ['menu_item', 'size', 'price', 'is_available']
    list_filter = ['size', 'is_available']
    search_fields = ['menu_item__name']
    autocomplete_fields = ['menu_item']
