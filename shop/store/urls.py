from django.urls import path
from django.conf.urls.static import static

from . import views
from shop import settings
app_name = "shop"
urlpatterns = [
    path('index', views.index, name='index'),
    path('produit/<str:slug>/', views.produit, name='produit'),
    path('', views.base, name='base'),

]