from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_page, name='menu'),
    path('gallery/', views.gallery_page, name='gallery'),
    path('about/', views.about, name='about'),
    path('our-story/', views.about, name='our_story'),
    path('visit-us/', views.visit, name='visit'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms, name='terms'),
    path('breakfast/', views.breakfast, name='breakfast'),
]
