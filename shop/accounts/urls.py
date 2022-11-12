from django.conf.urls.static import static
from django.urls import path

from . import views
from shop import settings
app_name = "accounts"
urlpatterns = [
    path('', views.signup, name='signup'),
    

]