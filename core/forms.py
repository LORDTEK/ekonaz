# core/forms.py
from django.utils import timezone
from django import forms
from .models import Firm, City

class FirmForm(forms.ModelForm):
    class Meta:
        model = Firm
        fields = [
            'name', 'city', 'district', 'tax_office', 'nace', 'create', 'address', 'telephone', 'fax', 'email', 'type_firm', 'tax', 'web', 'sgk_sicil', 'payment', 'ceo_name', 'ceo_email', 'ceo_cell', 'logo_media', 'active'
        ]
        widgets = {
            'create': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.order_by('name')

        instance = kwargs.get('instance')
        if instance and instance.delete:
            self.fields['delete'] = forms.DateTimeField(
                label="Silinme Tarihi ve Saati",
                initial=instance.delete,
                widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
                required=False
            )

class FirmSoftDeleteForm(forms.Form):
    delete_date = forms.DateTimeField(
        initial=timezone.now,
        label="Silinme Tarihi ve Saati",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
    )