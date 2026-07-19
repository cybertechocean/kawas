# KAWA'S Café Website

## Project Overview

A **production-ready, premium, mobile-first Django website** for KAWA'S Café — a Halal Certified specialty coffee house located at Mount Kenya Road, Nyali, Mombasa, Kenya.

The website is inspired by luxury cafés in Dubai, Doha, and Istanbul while embracing the relaxed coastal charm of Nyali, Mombasa.

## Tech Stack

- **Backend:** Python 3.12 + Django 6.0.7
- **Database:** SQLite (development) → PostgreSQL (production)
- **Frontend:** Tailwind CSS v4 (CDN), Alpine.js, HTMX, Lucide Icons
- **Admin:** Django Unfold (beautiful admin at `/kawas_admin/`)
- **Rich Content:** django-ckeditor-5
- **Static Files:** WhiteNoise
- **Server:** Gunicorn (port 5000)

## Running the Project

```bash
python manage.py runserver 0.0.0.0:5000
# OR
gunicorn kawas.wsgi:application --config gunicorn.conf.py
```

## Admin Access

URL: `/kawas_admin/`

Create a superuser:
```bash
python manage.py createsuperuser
```

## Seed Data

To populate the database with all menu items and sample data:
```bash
python seed_data.py
```

## Django Apps

| App | Purpose |
|-----|---------|
| `apps.siteconfig` | Global site configuration, announcements |
| `apps.core` | Hero slides, shared utilities |
| `apps.menu` | Menu categories, items, variants |
| `apps.pages` | All website pages (home, about, FAQs, etc.) |
| `apps.gallery` | Photo gallery |
| `apps.testimonials` | Customer reviews |
| `apps.location` | Opening hours |

## Website Pages

- `/` — Home
- `/menu/` — Full menu with search & category filters
- `/menu/<slug>/` — Individual item detail pages
- `/gallery/` — Photo gallery
- `/about/` — Our Story
- `/visit-us/` — Location & opening hours
- `/contact/` — Contact
- `/faqs/` — FAQs
- `/breakfast/` — Breakfast menu
- `/privacy-policy/` — Privacy Policy
- `/terms/` — Terms of Service
- `/sitemap.xml` — SEO sitemap
- `/robots.txt` — Robots file

## Brand Colors

- **Primary (Espresso Brown):** `#3E2723`
- **Secondary (Latte Sand):** `#F5E6D3`
- **Accent (Honey Gold):** `#D4A94A`
- **Sage (Halal badges):** `#8A9A5B`

## Environment Variables

| Variable | Value |
|----------|-------|
| `SESSION_SECRET` | Django SECRET_KEY (Replit Secret) |
| `DEBUG` | `True` (development) |
| `ALLOWED_HOSTS` | Replit hosts + localhost |
| `DJANGO_SETTINGS_MODULE` | `kawas.settings` |

## Static Files

- Logo: `static/img/kawas-logo.png`
- Menu QR Code: `static/img/kawas-menu-qr.png`

## Key Features

- Premium luxury design inspired by Dubai/Istanbul cafés
- Halal Certified branding throughout
- Dynamic menu with 14+ categories and 100+ items from actual PDF menu
- Individual item detail pages with WhatsApp ordering
- 4 action buttons per item: Order, WhatsApp, View Details, Wishlist
- Live search with HTMX
- Dark mode toggle
- Mobile-first with sticky bottom navigation
- Gallery with lightbox
- FAQs accordion
- Opening hours management
- SEO optimized (sitemap, robots, meta tags, Open Graph)
- WhiteNoise for static files
- Django Unfold admin

## User Preferences

- Use SQLite for development; user will switch to PostgreSQL on their own hosting provider
- Admin URL is `/kawas_admin/` (not `/admin/`)
- All Mojitos must be labeled "Alcohol-Free Mojitos (Mocktails)"
- Keep the existing Django project structure
