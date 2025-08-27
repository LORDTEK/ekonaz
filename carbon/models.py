# carbon/models.py

from django.db import models
from core.models import Firm # Katsayıları firmalara bağlamak için Firm modelini import ediyoruz

class EmissionFactor(models.Model):
    """
    Karbon emisyonu hesaplamalarında kullanılacak katsayıları (Emisyon Faktörlerini)
    ve bu katsayıların geçerlilik tarihlerini tutan model.
    """
    CATEGORY_CHOICES = [
        ('KAPSAM_1', 'Kapsam 1'),
        ('KAPSAM_2', 'Kapsam 2'),
        ('KAPSAM_3', 'Kapsam 3'),
        ('KAPSAM_4', 'Kapsam 4'),
        ('KAPSAM_5', 'Kapsam 5'),
        ('KAPSAM_6', 'Kapsam 6'),
    ]

    name = models.CharField(max_length=255, verbose_name="Faktör Adı") # Örn: Motorin, Elektrik, Pik Döküm
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Kategori/Kapsam")
    value = models.FloatField(verbose_name="Değer (Katsayı)") # Örn: 74100, 0.442
    unit = models.CharField(max_length=50, verbose_name="Birim") # Örn: kgCO2/TJ, tCO2/mwh

    # Bu katsayının hangi tarihten itibaren geçerli olduğunu belirtir.
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    # Bu katsayının hangi tarihe kadar geçerli olduğunu belirtir. Boş ise, hala geçerli demektir.
    valid_to = models.DateField(verbose_name="Geçerlilik Bitişi", null=True, blank=True)

    class Meta:
        verbose_name = "Emisyon Faktörü"
        verbose_name_plural = "Emisyon Faktörleri"
        ordering = ['-valid_from', 'name'] # En yeni tarihli olanlar üstte görünsün

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.value} {self.unit}"