# ekonaz/urls.py

from django.contrib import admin
from django.urls import path, include
from core import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path ('admin/', admin.site.urls),

    # Ana sayfaya gelen istekleri login view'a yönlendir
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Geri kalan tüm istekleri core.urls'e yönlendir
    path('', include('core.urls')),
]