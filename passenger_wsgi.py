"""
Passenger WSGI entry point for cPanel / LiteSpeed hosting.

Place this file in the same directory as manage.py (your domain root, e.g.
/home/<cpanelusername>/kawas.co.ke/).

cPanel's "Setup Python App" activates the virtual environment automatically
before Passenger loads this file, so no manual venv activation is needed here.
"""

import sys
import os

# ── Project root (same folder as this file) ──────────────────────────────────
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# ── Environment variables ─────────────────────────────────────────────────────
# Override these in cPanel → Python App → "Environment variables" section.
# They MUST be set there for production; these are safe fallback defaults only.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kawas.settings')
os.environ.setdefault('DEBUG', 'False')
os.environ.setdefault('ALLOWED_HOSTS', 'kawas.co.ke,www.kawas.co.ke')

# ── WSGI application ──────────────────────────────────────────────────────────
from django.core.wsgi import get_wsgi_application  # noqa: E402
application = get_wsgi_application()
