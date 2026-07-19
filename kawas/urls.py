from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

# Sitemap imports
from apps.core.sitemaps import StaticViewSitemap
from apps.menu.sitemaps import MenuItemSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'menu': MenuItemSitemap,
}

urlpatterns = [
    path('kawas_admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('', include('apps.pages.urls')),
    path('menu/', include('apps.menu.urls')),
    path('gallery/', include('apps.gallery.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error handlers
handler404 = 'apps.core.views.error_404'
handler500 = 'apps.core.views.error_500'
