from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'pages:home', 'pages:menu', 'pages:gallery', 'pages:about',
            'pages:visit', 'pages:contact', 'pages:faqs',
            'pages:privacy_policy', 'pages:breakfast',
        ]

    def location(self, item):
        return reverse(item)
