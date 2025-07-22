# core/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Bu decorator'ı import ediyoruz

# @login_required decorator'ı bu view'ı çalıştırmadan önce kullanıcının giriş yapmış olup olmadığını kontrol eder.
# Eğer kullanıcı giriş yapmamışsa onu otomatik olarak login sayfasına yönlendirir.
@login_required
def portal_view(request):
    # Şimdilik sadece portal.html şablonunu render ediyoruz.
    # İleride bu view'a şablona veri göndermek için mantık ekleyebiliriz.
    context = {} # Şimdilik boş bir context
    return render(request, 'portal.html', context)


from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Basit bir HTML yanıtı döndür
    return HttpResponse("<h1>Hoşgeldin! Bu benim özelleştirilmiş ana sayfam.</h1>")