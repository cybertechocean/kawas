import urllib.parse
from django import template

register = template.Library()


@register.simple_tag
def url_encode_whatsapp(item):
    """Generate a URL-encoded WhatsApp message for a menu item."""
    msg = item.get_whatsapp_message()
    return urllib.parse.quote(msg)


@register.filter
def wa_url(item, phone="254119000999"):
    """Return a full WhatsApp URL for the given menu item."""
    msg = urllib.parse.quote(item.get_whatsapp_message())
    return f"https://wa.me/{phone}?text={msg}"
