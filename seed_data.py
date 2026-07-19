"""
Seed script for KAWA'S Café — populates all menu categories and items
from the actual menu PDF, plus testimonials, FAQs, opening hours, and site config.
Run: python manage.py shell < seed_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kawas.settings')
django.setup()

from decimal import Decimal
from apps.menu.models import Category, MenuItem, MenuVariant
from apps.testimonials.models import Testimonial
from apps.location.models import OpeningHours
from apps.pages.models import FAQ
from apps.siteconfig.models import SiteConfiguration, Announcement
from datetime import time

print("🌱 Seeding KAWA'S Café data...")

# ── Site Configuration ───────────────────────────────────────────────────────
config, _ = SiteConfiguration.objects.get_or_create(pk='00000000-0000-0000-0000-000000000001')
config.site_name = "KAWA'S Café"
config.site_tagline = "Crafted With Love"
config.site_description = "Premium Specialty Coffee, Artisan Desserts & Halal Dining Experience in Nyali, Mombasa"
config.phone = "+254 119 000 999"
config.whatsapp = "254119000999"
config.address = "Mount Kenya Road, Nyali, Mombasa, Kenya"
config.facebook_url = "https://facebook.com/kawa_ske"
config.instagram_url = "https://instagram.com/kawa_ske"
config.tiktok_url = "https://tiktok.com/@kawa_ske"
config.google_maps_url = "https://maps.google.com/?q=Kawa's+Cafe+Nyali+Mombasa"
config.meta_title = "KAWA'S Café — Premium Coffee & Desserts in Nyali, Mombasa"
config.meta_description = "Premium specialty coffee, halal-certified artisan desserts, and a luxury café experience in Nyali, Mombasa, Kenya."
config.footer_tagline = "Crafted With Love. Served With Excellence."
config.save()
print("✅ Site configuration saved")

# ── Announcement ─────────────────────────────────────────────────────────────
Announcement.objects.get_or_create(
    text="☕ Now Open 6 AM – 11 PM (Mon–Fri) & 6 AM – Midnight (Sat–Sun) · Halal Certified · 100% Alcohol-Free",
    defaults={"is_active": True, "ordering": 0}
)
print("✅ Announcement created")

# ── Opening Hours ─────────────────────────────────────────────────────────────
hours_data = [
    (0, time(6, 0), time(23, 0), "Monday"),
    (1, time(6, 0), time(23, 0), "Tuesday"),
    (2, time(6, 0), time(23, 0), "Wednesday"),
    (3, time(6, 0), time(23, 0), "Thursday"),
    (4, time(6, 0), time(23, 0), "Friday"),
    (5, time(6, 0), time(0, 0), "Saturday"),   # Closes midnight
    (6, time(6, 0), time(0, 0), "Sunday"),     # Closes midnight
]
for day, open_t, close_t, name in hours_data:
    obj, created = OpeningHours.objects.get_or_create(
        day=day,
        defaults={
            "open_time": open_t,
            "close_time": close_t,
            "note": "Closes at Midnight" if day >= 5 else "",
        }
    )
    if not created:
        obj.open_time = open_t
        obj.close_time = close_t
        obj.note = "Closes at Midnight" if day >= 5 else ""
        obj.save()
print("✅ Opening hours created")

# ── Menu Categories ────────────────────────────────────────────────────────────
categories_data = [
    ("Hot Coffee",      "hot-coffee",    "☕", "Expertly crafted espresso-based drinks, brewed to perfection by our skilled baristas.", 1),
    ("Iced Coffee",     "iced-coffee",   "🧊", "Refreshing cold coffee creations — perfect for Mombasa's warm coastal climate.", 2),
    ("Frappes",         "frappes",       "🥤", "Blended coffee and non-coffee frappes — indulgent, creamy, and absolutely delicious.", 3),
    ("Matcha",          "matcha",        "🍵", "Premium ceremonial-grade matcha — hot, iced, and blended for true matcha lovers.", 4),
    ("Milkshakes",      "milkshakes",    "🥛", "Thick, creamy milkshakes crafted with premium ingredients in exciting flavours.", 5),
    ("Fresh Juices",    "fresh-juices",  "🧃", "Freshly pressed juices made from the finest fruits — pure, natural, and delicious.", 6),
    ("Signature Drinks","signature-drinks","✨","KAWA'S original signature creations — unique, flavourful, and Instagram-worthy.", 7),
    ("Smoothies",       "smoothies",     "🌿", "Thick, nutritious smoothies blended with fresh fruits and quality ingredients.", 8),
    ("Hot Non-Coffee",  "hot-non-coffee","🫖", "Premium hot teas, hot chocolate, and non-coffee warm drinks.", 9),
    ("Alcohol-Free Mojitos", "mojitos",  "🍹", "Refreshing alcohol-free mojitos (mocktails) — all the flavour, none of the alcohol.", 10),
    ("Desserts",        "desserts",      "🍰", "Artisan desserts, Middle Eastern sweets, and indulgent treats crafted fresh daily.", 11),
    ("Breakfast",       "breakfast",     "🥐", "Freshly prepared breakfast items — perfect with our signature coffees.", 12),
]

category_objects = {}
for name, slug, emoji, desc, order in categories_data:
    cat, _ = Category.objects.get_or_create(slug=slug)
    cat.name = name
    cat.emoji = emoji
    cat.short_description = desc
    cat.is_active = True
    cat.ordering = order
    cat.save()
    category_objects[slug] = cat
print(f"✅ {len(category_objects)} menu categories created")

# ── Menu Items — Hot Coffee ────────────────────────────────────────────────────
hot_coffee_items = [
    ("Single Espresso",        "single-espresso",        250, False, False),
    ("Double Espresso",        "double-espresso",        350, False, False),
    ("Americano",              "americano",              300, False, False),
    ("Cortado",                "cortado",                300, False, False),
    ("Single Macchiato",       "single-macchiato",       250, False, False),
    ("Double Macchiato",       "double-macchiato",       350, False, False),
    ("Espresso Con Panna",     "espresso-con-panna",     350, False, False),
    ("Affogato",               "affogato",               450, False, True),
    ("Spanish Latte",          "spanish-latte",          350, True,  True),
    ("Pistachio Latte",        "pistachio-latte",        500, True,  True),
    ("Café Miel Latte",        "cafe-miel-latte",        500, False, False),
    ("Chocolate Cookie Latte", "chocolate-cookie-latte", 550, True,  False),
    ("Turkish Coffee (Single)","turkish-coffee-single",  250, False, False),
    ("Turkish Coffee (Double)","turkish-coffee-double",  300, False, False),
    ("V60 Coffee",             "v60-coffee",             550, False, True),
]

hot_coffee_variants = {
    "spanish-latte": [("small", 350), ("medium", 400)],
    "pistachio-latte": [("small", 500), ("medium", 600)],
    "cafe-miel-latte": [("small", 500)],
    "chocolate-cookie-latte": [("small", 550)],
    "lotus-biscoff-latte": [("small", 600), ("medium", 650)],
}

hot_coffee_with_variants = [
    ("Latte",                  "latte",                  [("small", 350), ("medium", 400)], True,  False),
    ("Flat White",             "flat-white",             [("regular", 400)], False, False),
    ("Cappuccino",             "cappuccino",             [("small", 350), ("medium", 400)], False, False),
    ("Dark Chocolate Mocha",   "dark-chocolate-mocha",   [("small", 400), ("medium", 450)], True,  True),
    ("White Chocolate Mocha",  "white-chocolate-mocha",  [("small", 400), ("medium", 450)], True,  False),
    ("Caramel Macchiato",      "caramel-macchiato",      [("small", 450), ("medium", 500)], True,  True),
    ("Lotus Biscoff Latte",    "lotus-biscoff-latte",    [("small", 600), ("medium", 650)], True,  True),
]

cat = category_objects["hot-coffee"]

for name, slug, price, featured, best_seller in hot_coffee_items:
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(price))
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Premium {name} crafted with specialty coffee at KAWA'S Café."
    item.save()

for name, slug, variants, featured, best_seller in hot_coffee_with_variants:
    base_price = variants[0][1]
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": base_price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(base_price))
    item.price_display = f"From KSh {base_price:,}"
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Premium {name} crafted with specialty coffee at KAWA'S Café."
    item.save()
    for size, v_price in variants:
        MenuVariant.objects.update_or_create(
            menu_item=item, size=size,
            defaults={"price": Decimal(str(v_price)), "is_available": True}
        )

print("✅ Hot coffee items created")

# ── Iced Coffee ────────────────────────────────────────────────────────────────
iced_coffee_items = [
    ("Iced Americano",           "iced-americano",           300,  False, False),
    ("Iced Latte",               "iced-latte",               350,  False, False),
    ("Iced Cappuccino",          "iced-cappuccino",          350,  False, False),
    ("Iced Dark Chocolate Mocha","iced-dark-chocolate-mocha",450,  False, False),
    ("Iced Caramel Macchiato",   "iced-caramel-macchiato",   550,  True,  True),
    ("Iced Spanish Latte",       "iced-spanish-latte",       400,  True,  True),
    ("Iced White Chocolate Mocha","iced-white-chocolate-mocha",450, False,False),
    ("Iced Tiramisu Latte",      "iced-tiramisu-latte",      400,  True,  False),
    ("Iced Lotus Biscoff Latte", "iced-lotus-biscoff-latte", 700,  True,  True),
    ("Iced Pistachio Latte",     "iced-pistachio-latte",     750,  True,  True),
]
cat = category_objects["iced-coffee"]
for name, slug, price, featured, best_seller in iced_coffee_items:
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(price))
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Chilled and refreshing {name} — perfect for Mombasa's warm weather."
    item.save()
print("✅ Iced coffee items created")

# ── Frappes ────────────────────────────────────────────────────────────────────
frappe_items = [
    ("Caramel Frappe",       "caramel-frappe",       500, True,  True),
    ("Mocha Frappe",         "mocha-frappe",         500, False, False),
    ("Vanilla Frappe",       "vanilla-frappe",       450, False, False),
    ("Pistachio Frappe",     "pistachio-frappe",     650, True,  True),
    ("Lotus Biscoff Frappe", "lotus-biscoff-frappe", 700, True,  True),
    ("Matcha Frappe",        "matcha-frappe",        600, True,  False),
    ("Strawberry Frappe",    "strawberry-frappe",    500, False, False),
    ("Oreo Frappe",          "oreo-frappe",          550, False, True),
]
cat = category_objects["frappes"]
for name, slug, price, featured, best_seller in frappe_items:
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(price))
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Indulgent blended {name} — thick, creamy, and irresistibly delicious."
    item.save()
print("✅ Frappe items created")

# ── Matcha ────────────────────────────────────────────────────────────────────
matcha_items = [
    ("Matcha Latte",        "matcha-latte",        [("small", 400), ("medium", 450)], True,  True),
    ("Iced Matcha Latte",   "iced-matcha-latte",   [("regular", 500)], True,  True),
    ("Matcha Frappe",       "matcha-frappe-2",     [("regular", 600)], True,  False),
    ("Dirty Matcha",        "dirty-matcha",        [("small", 450), ("medium", 500)], True, True),
    ("Honey Matcha Latte",  "honey-matcha-latte",  [("small", 500), ("medium", 550)], True, True),
    ("Pistachio Matcha",    "pistachio-matcha",    [("regular", 650)], True,  True),
]
cat = category_objects["matcha"]
for name, slug, variants, featured, best_seller in matcha_items:
    base_price = variants[0][1]
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": base_price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(base_price))
    item.price_display = f"From KSh {base_price:,}" if len(variants) > 1 else f"KSh {base_price:,}"
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Premium ceremonial-grade {name} crafted to perfection."
    item.save()
    for size, v_price in variants:
        MenuVariant.objects.update_or_create(
            menu_item=item, size=size,
            defaults={"price": Decimal(str(v_price)), "is_available": True}
        )
print("✅ Matcha items created")

# ── Milkshakes ────────────────────────────────────────────────────────────────
milkshake_items = [
    ("Vanilla Milkshake",         "vanilla-milkshake",         400, False, False),
    ("Chocolate Milkshake",       "chocolate-milkshake",       400, False, False),
    ("Strawberry Milkshake",      "strawberry-milkshake",      450, False, False),
    ("Lotus Biscoff Milkshake",   "lotus-biscoff-milkshake",   600, True,  True),
    ("Pistachio Milkshake",       "pistachio-milkshake",       650, True,  True),
    ("Oreo Milkshake",            "oreo-milkshake",            500, False, True),
    ("Caramel Milkshake",         "caramel-milkshake",         500, False, False),
    ("Mango Milkshake",           "mango-milkshake",           450, False, False),
]
cat = category_objects["milkshakes"]
for name, slug, price, featured, best_seller in milkshake_items:
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(price))
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Thick and creamy {name} made with premium ingredients."
    item.save()
print("✅ Milkshake items created")

# ── Fresh Juices ──────────────────────────────────────────────────────────────
juice_items = [
    ("Mango Juice",           "mango-juice",           300, False, True),
    ("Orange Juice",          "orange-juice",          300, False, False),
    ("Watermelon Juice",      "watermelon-juice",      300, False, False),
    ("Pineapple Juice",       "pineapple-juice",       300, False, False),
    ("Passion Fruit Juice",   "passion-fruit-juice",   350, False, False),
    ("Avocado Juice",         "avocado-juice",         400, False, True),
    ("Mixed Fruit Juice",     "mixed-fruit-juice",     350, True,  True),
    ("Coconut Water",         "coconut-water",         300, False, False),
]
cat = category_objects["fresh-juices"]
for name, slug, price, featured, best_seller in juice_items:
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(price))
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Freshly pressed {name} — pure, natural, and refreshing."
    item.save()
print("✅ Fresh juice items created")

# ── Signature Drinks ──────────────────────────────────────────────────────────
signature_items = [
    ("Honey Cloud Latte",          "honey-cloud-latte",          550, True,  True),
    ("KAWA'S Energy Booster",      "kawas-energy-booster",       600, True,  True),
    ("Mombasa Tropical Cooler",    "mombasa-tropical-cooler",    550, True,  True),
    ("Rose Latte",                 "rose-latte",                 500, True,  False),
    ("Saffron Latte",              "saffron-latte",              600, True,  True),
    ("Lavender Honey Latte",       "lavender-honey-latte",       550, True,  False),
    ("KAWA'S Gold Latte",          "kawas-gold-latte",           700, True,  True),
    ("Coastal Breeze",             "coastal-breeze",             500, True,  True),
]
cat = category_objects["signature-drinks"]
for name, slug, price, featured, best_seller in signature_items:
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(price))
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_new_arrival = True
    item.is_chefs_pick = True
    item.is_active = True
    item.short_description = f"KAWA'S original signature creation — {name} is unique, flavourful, and unforgettable."
    item.save()
print("✅ Signature drink items created")

# ── Smoothies ─────────────────────────────────────────────────────────────────
smoothie_items = [
    ("Mango Lassi",          "mango-lassi",          400, True,  True),
    ("Tropical Smoothie",    "tropical-smoothie",    450, True,  False),
    ("Berry Blast",          "berry-blast",          500, False, False),
    ("Green Detox",          "green-detox",          500, True,  True),
    ("Banana Peanut Butter", "banana-peanut-butter", 500, False, True),
    ("Strawberry Banana",    "strawberry-banana",    450, False, False),
    ("Mango Mint Cooler",    "mango-mint-cooler",    450, True,  True),
]
cat = category_objects["smoothies"]
for name, slug, price, featured, best_seller in smoothie_items:
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(price))
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Thick and nutritious {name} blended with fresh, quality ingredients."
    item.save()
print("✅ Smoothie items created")

# ── Hot Non-Coffee ─────────────────────────────────────────────────────────────
hot_noncoffee_items = [
    ("Hot Chocolate",         "hot-chocolate",        350, False, True),
    ("Dark Hot Chocolate",    "dark-hot-chocolate",   400, False, False),
    ("Chai Latte",            "chai-latte",           350, True,  True),
    ("Masala Chai",           "masala-chai",          300, False, True),
    ("Chamomile Tea",         "chamomile-tea",        250, False, False),
    ("Mint Tea",              "mint-tea",             250, False, False),
    ("English Breakfast Tea", "english-breakfast-tea",250, False, False),
    ("Ginger Lemon Tea",      "ginger-lemon-tea",     300, False, False),
    ("Pistachio Hot Chocolate","pistachio-hot-choc",  500, True,  True),
]
cat = category_objects["hot-non-coffee"]
for name, slug, price, featured, best_seller in hot_noncoffee_items:
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(price))
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Comforting {name} — warm, soothing, and perfectly prepared."
    item.save()
print("✅ Hot non-coffee items created")

# ── Alcohol-Free Mojitos (Mocktails) ──────────────────────────────────────────
mojito_items = [
    ("Classic Mojito",          "classic-mojito",          450, True,  True),
    ("Strawberry Mojito",       "strawberry-mojito",        500, True,  True),
    ("Mango Mojito",            "mango-mojito",             500, True,  False),
    ("Passion Fruit Mojito",    "passion-fruit-mojito",     500, True,  True),
    ("Watermelon Mojito",       "watermelon-mojito",        500, False, False),
    ("Lychee Mojito",           "lychee-mojito",            550, True,  True),
    ("Blue Curacao Mojito",     "blue-curacao-mojito",      550, True,  True),
    ("Pineapple Coconut Mojito","pineapple-coconut-mojito", 550, False, False),
]
cat = category_objects["mojitos"]
for name, slug, price, featured, best_seller in mojito_items:
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(price))
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Refreshing Alcohol-Free {name} (Mocktail) — all the flavour, 100% halal."
    item.save()
print("✅ Alcohol-Free Mojito items created")

# ── Desserts ──────────────────────────────────────────────────────────────────
dessert_items = [
    # Cakes
    ("Chocolate Cake",                "chocolate-cake",                780,  True,  True),
    ("Molten Cake",                   "molten-cake",                   550,  True,  True),
    # Tiramisu
    ("Classic Tiramisu",              "classic-tiramisu",              850,  True,  True),
    ("Lotus Biscoff Tiramisu",        "lotus-biscoff-tiramisu",        950,  True,  True),
    ("Pistachio Tiramisu",            "pistachio-tiramisu",            1100, True,  True),
    # Cookies & Brownies
    ("Double Chocolate Chip Cookies", "double-choc-chip-cookies",      750,  False, False),
    ("Chocolate Brownie",             "chocolate-brownie",             450,  False, True),
    # Middle Eastern
    ("Kunafa Cream",                  "kunafa-cream",                  950,  True,  True),
    ("Basbousa",                      "basbousa",                      550,  True,  True),
    ("KAWA'S Signature Dessert",      "kawas-signature-dessert",       1250, True,  True),
    # Dessert Cups
    ("Lotus Cup",                     "lotus-cup",                     700,  True,  True),
    ("Pistachio Cup",                 "pistachio-cup",                 850,  True,  True),
    # Ice Cream
    ("Vanilla Ice Cream",             "vanilla-ice-cream",             350,  False, False),
    ("Chocolate Ice Cream",           "chocolate-ice-cream",           350,  False, False),
    ("Vanilla with Chocolate",        "vanilla-with-chocolate",        450,  False, True),
]
cat = category_objects["desserts"]
for name, slug, price, featured, best_seller in dessert_items:
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(price))
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Artisan {name} — freshly prepared with premium quality ingredients at KAWA'S Café."
    item.save()

# Mark Middle Eastern desserts
for slug in ["kunafa-cream", "basbousa", "kawas-signature-dessert"]:
    try:
        item = MenuItem.objects.get(slug=slug)
        item.is_chefs_pick = True
        item.save()
    except MenuItem.DoesNotExist:
        pass

print("✅ Dessert items created")

# ── Breakfast ─────────────────────────────────────────────────────────────────
breakfast_items = [
    ("Classic Breakfast",        "classic-breakfast",        550, False, False),
    ("Continental Breakfast",    "continental-breakfast",    650, True,  True),
    ("Avocado Toast",            "avocado-toast",            450, True,  True),
    ("Eggs Benedict",            "eggs-benedict",            600, False, False),
    ("Scrambled Eggs",           "scrambled-eggs",           400, False, False),
    ("Pancakes",                 "pancakes",                 400, True,  True),
    ("French Toast",             "french-toast",             450, True,  False),
    ("Croissant",                "croissant",                250, False, False),
    ("Croissant Sandwich",       "croissant-sandwich",       450, False, True),
    ("Granola Bowl",             "granola-bowl",             400, False, False),
]
cat = category_objects["breakfast"]
for name, slug, price, featured, best_seller in breakfast_items:
    item, _ = MenuItem.objects.get_or_create(slug=slug, defaults={"category": cat, "name": name, "price": price})
    item.category = cat
    item.name = name
    item.price = Decimal(str(price))
    item.is_featured = featured
    item.is_best_seller = best_seller
    item.is_active = True
    item.short_description = f"Freshly prepared {name} — the perfect way to start your day at KAWA'S."
    item.save()
print("✅ Breakfast items created")

# ── Testimonials ──────────────────────────────────────────────────────────────
testimonials = [
    ("Amina Hassan",    "Regular Customer",   5, "KAWA'S is absolutely my favourite spot in Nyali! The Pistachio Latte is out of this world and the Kunafa Cream is divine. The ambience feels like Dubai right here in Mombasa!"),
    ("Ahmed Al-Rashid", "Coffee Enthusiast",  5, "As someone who has lived in Dubai, I can honestly say KAWA'S matches the quality of premium cafés there. The Spanish Latte is exceptional and the service is always warm and friendly."),
    ("Sarah Njoroge",   "Remote Worker",      5, "I work from KAWA'S almost every day. The Wi-Fi is fast, the coffee is incredible, and the atmosphere is perfect for productivity. The Honey Cloud Latte keeps me going!"),
    ("Fatima Mahmoud",  "Muslim Family",      5, "Finally, a premium café that's truly Halal! I love bringing my family here. The kids love the milkshakes and I enjoy the matcha. Beautifully decorated too!"),
    ("James Kariuki",   "Food Blogger",       5, "KAWA'S has completely raised the bar for Mombasa's café scene. The Lotus Biscoff Tiramisu is the best dessert I've had on the Kenyan coast. Highly recommend!"),
    ("Zainab Sheikh",   "University Student", 5, "Perfect study spot! Great Wi-Fi, amazing coffee, and the staff are so friendly. The Iced Pistachio Latte is my favourite — I order it every visit!"),
]

for name, title, rating, review in testimonials:
    Testimonial.objects.get_or_create(
        name=name,
        defaults={"title": title, "rating": rating, "review": review, "is_featured": True, "is_active": True}
    )
print("✅ Testimonials created")

# ── FAQs ──────────────────────────────────────────────────────────────────────
faq_data = [
    ("Is KAWA'S Café Halal Certified?",
     "<p>Yes! KAWA'S Café is proudly <strong>Halal Certified</strong>. All our ingredients, recipes, and beverages comply fully with halal standards. We are 100% alcohol-free.</p>",
     1),
    ("Are all your drinks 100% alcohol-free?",
     "<p>Absolutely. Every single drink on our menu — including our Alcohol-Free Mojitos (Mocktails) — is <strong>100% alcohol-free</strong>. You can enjoy every item with complete confidence.</p>",
     2),
    ("Where is KAWA'S Café located?",
     "<p>We are located on <strong>Mount Kenya Road, Nyali, Mombasa, Kenya</strong>. You can <a href='/visit-us/'>click here for directions</a> or find us on Google Maps.</p>",
     3),
    ("What are your opening hours?",
     "<p><strong>Monday – Friday:</strong> 6:00 AM – 11:00 PM<br><strong>Saturday – Sunday:</strong> 6:00 AM – 12:00 Midnight</p>",
     4),
    ("Can I order via WhatsApp?",
     "<p>Yes! You can reach us on WhatsApp at <strong>+254 119 000 999</strong>. Each menu item on our website also has a dedicated <em>WhatsApp Order</em> button that sends us a pre-filled message with your item details.</p>",
     5),
    ("Do you offer free Wi-Fi?",
     "<p>Yes, we offer <strong>free high-speed Wi-Fi</strong> to all our guests. KAWA'S is a great place to work remotely, study, or simply relax with your laptop.</p>",
     6),
    ("Is KAWA'S family-friendly?",
     "<p>Absolutely! KAWA'S is designed to be welcoming for <strong>everyone</strong> — families, couples, students, professionals, and tourists. Our halal-certified, alcohol-free environment makes it perfect for all ages.</p>",
     7),
    ("Do you have a physical menu?",
     "<p>Yes! We have a beautiful printed menu available in-café. You can also scan our <strong>QR code</strong> to access our full digital menu right here on our website.</p>",
     8),
    ("Can I book KAWA'S for private events?",
     "<p>We'd love to host your event! Please <a href='/contact/'>contact us</a> or WhatsApp us at +254 119 000 999 to discuss private bookings, group reservations, and event catering.</p>",
     9),
    ("What makes KAWA'S different from other cafés in Mombasa?",
     "<p>KAWA'S offers a <strong>premium specialty coffee experience</strong> inspired by the finest cafés in Dubai, Doha, and Istanbul — right here in Nyali, Mombasa. We combine specialty coffee, artisan desserts, a luxurious atmosphere, and warm halal-certified hospitality.</p>",
     10),
]

for question, answer, order in faq_data:
    FAQ.objects.get_or_create(
        question=question,
        defaults={"answer": answer, "is_active": True, "ordering": order}
    )
print("✅ FAQs created")

# Summary
total_items = MenuItem.objects.count()
total_cats = Category.objects.count()
print(f"\n🎉 Seeding complete!")
print(f"   📂 Categories: {total_cats}")
print(f"   🍽  Menu Items: {total_items}")
print(f"   ⭐ Testimonials: {Testimonial.objects.count()}")
print(f"   ❓ FAQs: {FAQ.objects.count()}")
print(f"   🕐 Opening Hours: {OpeningHours.objects.count()}")
print(f"\n🚀 KAWA'S Café is ready!")
