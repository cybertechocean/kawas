from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_home, name='home'),
    path('search/', views.search_ajax, name='search'),
    path('category/<slug:slug>/', views.category_detail, name='category'),
    path('<slug:slug>/', views.item_detail, name='item_detail'),
]
