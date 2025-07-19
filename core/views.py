from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Basit bir HTML yanıtı döndür
    return HttpResponse("<h1>Hoşgeldin! Bu benim özelleştirilmiş ana sayfam.</h1>")