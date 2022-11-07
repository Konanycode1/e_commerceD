from django.urls import path
from django.conf.urls.static import static

from . import views
from shop import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('produit/<str:slug>/', views.produit, name='produit'),
    path('base/', views.base, name='base'),

]