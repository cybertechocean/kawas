"""
Django settings for KAWA'S Café website.
"""

from pathlib import Path
from decouple import config
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SESSION_SECRET', default='django-insecure-kawas-dev-key-change-in-production')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# CSRF trusted origins for Replit preview
CSRF_TRUSTED_ORIGINS = [
    'https://*.replit.dev',
    'https://*.replit.app',
    'https://*.repl.co',
    'http://localhost:5000',
    'http://127.0.0.1:5000',
]

INSTALLED_APPS = [
    # Django Unfold (must be before django.contrib.admin)
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'unfold.contrib.inlines',
    'unfold.contrib.simple_history',
    # Django built-ins
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Cloudinary must come before django.contrib.staticfiles
    'cloudinary',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # Third-party
    'imagekit',
    'django_ckeditor_5',
    'django_extensions',
    # Local apps
    'apps.siteconfig',
    'apps.core',
    'apps.menu',
    'apps.pages',
    'apps.gallery',
    'apps.testimonials',
    'apps.location',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kawas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.siteconfig.context_processors.site_config',
            ],
        },
    },
]

WSGI_APPLICATION = 'kawas.wsgi.application'

# Database — SQLite for development, switch to PostgreSQL in production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# Static files (served locally by WhiteNoise — not Cloudinary)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files — uploaded to Cloudinary
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Storage backends
STORAGES = {
    # All ImageField / FileField uploads go to Cloudinary
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    # Static files stay on local disk, served by WhiteNoise
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Cloudinary credentials (stored as Replit Secrets)
cloudinary.config(
    cloud_name=config('CLOUDINARY_CLOUD_NAME'),
    api_key=config('CLOUDINARY_API_KEY'),
    api_secret=config('CLOUDINARY_API_SECRET'),
    secure=True,
)

# Cloudinary folder organisation per upload_to paths already defined in models:
#   hero/ · gallery/ · menu/ · categories/ · testimonials/
CLOUDINARY_STORAGE = {
    'MEDIA_TAG': 'kawas',          # tags every upload with "kawas" for easy filtering
    'INVALID_VIDEO_ERROR_MESSAGE': 'Please upload a valid image.',
    'EXCLUDE_DELETE_ORPHANED_MEDIA_PATHS': (),
    'STATIC_TAG': 'kawas-static',
    'STATICFILES_MANIFEST_ROOT': BASE_DIR / 'staticfiles',
}

# django-imagekit: keep generated thumbnail cache files on local filesystem
# so imagekit doesn't push every resized variant to Cloudinary
IMAGEKIT_DEFAULT_CACHEFILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
IMAGEKIT_CACHEFILE_DIR = 'CACHE/images'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Unfold Admin Configuration
UNFOLD = {
    "SITE_TITLE": "KAWA'S Admin",
    "SITE_HEADER": "KAWA'S Café",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: "/static/img/kawas-logo.png",
        "dark": lambda request: "/static/img/kawas-logo.png",
    },
    "SITE_LOGO": {
        "light": lambda request: "/static/img/kawas-logo.png",
        "dark": lambda request: "/static/img/kawas-logo.png",
    },
    "SITE_SYMBOL": "coffee",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "THEME": "dark",
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Website Content",
                "separator": True,
                "items": [
                    {
                        "title": "Site Configuration",
                        "icon": "settings",
                        "link": "/kawas_admin/siteconfig/siteconfiguration/",
                    },
                    {
                        "title": "Announcements",
                        "icon": "campaign",
                        "link": "/kawas_admin/siteconfig/announcement/",
                    },
                ],
            },
            {
                "title": "Menu",
                "separator": True,
                "items": [
                    {
                        "title": "Categories",
                        "icon": "category",
                        "link": "/kawas_admin/menu/category/",
                    },
                    {
                        "title": "Menu Items",
                        "icon": "restaurant_menu",
                        "link": "/kawas_admin/menu/menuitem/",
                    },
                    {
                        "title": "Variants",
                        "icon": "tune",
                        "link": "/kawas_admin/menu/menuvariant/",
                    },
                ],
            },
            {
                "title": "Content",
                "separator": True,
                "items": [
                    {
                        "title": "Gallery",
                        "icon": "photo_library",
                        "link": "/kawas_admin/gallery/galleryimage/",
                    },
                    {
                        "title": "Testimonials",
                        "icon": "star",
                        "link": "/kawas_admin/testimonials/testimonial/",
                    },
                    {
                        "title": "FAQ",
                        "icon": "help",
                        "link": "/kawas_admin/pages/faq/",
                    },
                    {
                        "title": "Hero Slides",
                        "icon": "slideshow",
                        "link": "/kawas_admin/core/heroslide/",
                    },
                ],
            },
            {
                "title": "Location & Hours",
                "separator": True,
                "items": [
                    {
                        "title": "Opening Hours",
                        "icon": "schedule",
                        "link": "/kawas_admin/location/openinghours/",
                    },
                ],
            },
            {
                "title": "Users",
                "separator": True,
                "items": [
                    {
                        "title": "Users",
                        "icon": "people",
                        "link": "/kawas_admin/auth/user/",
                    },
                ],
            },
        ],
    },
}

# CKEditor 5 Configuration
customColorPalette = [
    {'color': 'hsl(4, 90%, 58%)', 'label': 'Red'},
    {'color': 'hsl(340, 82%, 52%)', 'label': 'Pink'},
    {'color': 'hsl(291, 64%, 42%)', 'label': 'Purple'},
    {'color': 'hsl(262, 52%, 47%)', 'label': 'Deep Purple'},
    {'color': 'hsl(231, 48%, 48%)', 'label': 'Indigo'},
    {'color': 'hsl(207, 90%, 54%)', 'label': 'Blue'},
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload'],
    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|', 'bulletedList', 'numberedList',
            '|', 'blockQuote',
        ],
        'toolbar': {
            'items': [
                'heading', '|', 'outdent', 'indent', '|',
                'bold', 'italic', 'link', 'underline', 'strikethrough',
                'code', 'subscript', 'superscript', 'highlight', '|',
                'codeBlock', 'sourceEditing', 'insertImage',
                'bulletedList', 'numberedList', 'todoList', '|',
                'blockQuote', 'imageUpload', '|',
                'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor',
                'mediaEmbed', 'removeFormat', 'insertTable',
            ],
            'shouldNotGroupWhenFull': True,
        },
        'image': {
            'toolbar': [
                'imageTextAlternative', '|', 'imageStyle:alignLeft',
                'imageStyle:alignRight', 'imageStyle:alignCenter',
                'imageStyle:side', '|'
            ],
            'styles': [
                'full', 'side', 'alignLeft', 'alignRight', 'alignCenter',
            ],
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells',
                               'tableProperties', 'tableCellProperties'],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette,
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette,
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'},
            ]
        }
    },
}

CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
