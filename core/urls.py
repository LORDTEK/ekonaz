# core/urls.py

from django.urls import path
from . import views # core uygulamasının içindeki views.py dosyasını import et

urlpatterns = [
    # /portal/ adresine gelen istekleri, views.py dosyasındaki portal_view fonksiyonuna yönlendir.
    path('portal/', views.portal_view, name='portal'),
]