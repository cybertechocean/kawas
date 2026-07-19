---
name: Database seeding for KAWA'S Café
description: How to seed menu data and what the seeded data contains
---

# Seeding

Run: `python seed_data.py` from the project root.

## What it creates
- 12 menu categories (Hot Coffee, Iced Coffee, Frappes, Matcha, Milkshakes, Fresh Juices, Signature Drinks, Smoothies, Hot Non-Coffee, Alcohol-Free Mojitos, Desserts, Breakfast)
- 119 menu items with real prices from the KAWAS_MENU.pdf
- 6 featured testimonials
- 10 FAQs
- 7 opening hours rows (Mon–Fri 6AM–11PM, Sat–Sun 6AM–midnight)
- SiteConfiguration singleton
- 1 Announcement banner

## Admin superuser
Created via `python manage.py createsuperuser` or the shell one-liner in `seed_data.py` comments. Use the Django admin at `/kawas_admin/`.

**Why:** get_or_create for OpeningHours requires all NOT NULL fields in `defaults={}` dict, not set after the fact.
