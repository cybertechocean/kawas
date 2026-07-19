from .models import SiteConfiguration, Announcement


def site_config(request):
    """Inject site configuration and active announcements into all templates."""
    try:
        config = SiteConfiguration.objects.first()
        if not config:
            config = SiteConfiguration.objects.create()
    except Exception:
        config = None

    try:
        announcements = Announcement.objects.filter(is_active=True)
    except Exception:
        announcements = []

    return {
        'site_config': config,
        'announcements': announcements,
    }
