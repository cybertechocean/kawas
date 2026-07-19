---
name: Cloudinary image storage setup
description: How Cloudinary is wired into Django for media uploads; imagekit interaction.
---

# Cloudinary Setup for KAWA'S Café

## Rule
All `ImageField` uploads go to Cloudinary via `django-cloudinary-storage`. Static files stay on local WhiteNoise. Never change the `staticfiles` backend to Cloudinary.

**Why:** User has high-volume café photos to manage. Cloudinary provides CDN delivery and the admin upload flow works automatically.

## How to apply
- Credentials live in Replit Secrets: `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`
- Configured in `kawas/settings.py` via `cloudinary.config()` using `python-decouple`
- `STORAGES["default"]` = `cloudinary_storage.storage.MediaCloudinaryStorage`
- `STORAGES["staticfiles"]` = `whitenoise.storage.CompressedManifestStaticFilesStorage`
- `IMAGEKIT_DEFAULT_CACHEFILE_STORAGE = 'django.core.files.storage.FileSystemStorage'` keeps imagekit thumbnail caches local

## Folder structure (upload_to paths in models)
- `hero/` — HeroSlide.image
- `gallery/` — GalleryImage.image
- `menu/` — MenuItem.image
- `categories/` — Category.image
- `testimonials/` — Testimonial.avatar

## INSTALLED_APPS order (critical)
`cloudinary` and `cloudinary_storage` must appear **before** `django.contrib.staticfiles`.
