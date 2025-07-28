# core/forms.py
from django.utils import timezone
from django import forms
from .models import Firm, City

class FirmForm(forms.ModelForm):
    class Meta:
        model = Firm
        exclude = ['delete']
        widgets = {
            'create': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    # Form başlatıldığında çalışacak özel fonksiyon
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # city alanının veri setini (queryset) alfabetik olarak sırala
        self.fields['city'].queryset = City.objects.order_by('name')
        # fields = [
        #     'name', 'city', 'district', 'tax_office', 'nace', 'address', 
        #     'telephone', 'fax', 'email', 'type_firm', 'tax', 'web', 
        #     'sgk_sicil', 'payment', 'ceo_name', 'ceo_email', 'ceo_cell', 'active'
        # ]

class FirmSoftDeleteForm(forms.Form):
    delete_date = forms.DateTimeField(
        initial=timezone.now,
        label="Silinme Tarihi ve Saati",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
    )