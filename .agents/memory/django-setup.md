---
name: Django project setup decisions
description: Key architectural and config decisions for KAWA'S Café Django project
---

# KAWA'S Café Django Setup

## Key decisions

- **Database:** SQLite for dev; user plans PostgreSQL on own hosting later
- **SECRET_KEY:** sourced from `SESSION_SECRET` Replit secret via python-decouple
- **CSS/JS:** Tailwind CSS v4 CDN + Alpine.js CDN + HTMX CDN (no build step)
- **Admin:** Django Unfold at `/kawas_admin/` (not `/admin/`)
- **Apps:** placed under `apps/` subdirectory (e.g. `apps.menu`, `apps.core`)
- **Static:** WhiteNoise serves static files; logo at `static/img/kawas-logo.png`
- **Server:** Gunicorn on port 5000 via `gunicorn.conf.py`
- **Rich text:** django-ckeditor-5 for all description/answer fields
- **Images:** django-imagekit + Pillow for thumbnails

**Why:** User explicitly chose SQLite + CDN approach for simplicity on Replit, with plan to migrate to own server later.

## Social icons in footer
Lucide CDN does not include `facebook` or `instagram` icons — replaced with inline SVGs in `templates/partials/footer.html`.

## Template filter
`urllib_tags` custom template tag in `apps/menu/templatetags/urllib_tags.py` — must `{% load urllib_tags %}` in any template using the `wa_url` filter. The filter returns the FULL WhatsApp URL (not just the query param).

## Django template filters
`split` is NOT a built-in Django filter — never use `|split:","` in templates.
