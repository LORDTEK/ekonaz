# core/forms.py
from django.utils import timezone
from django import forms
from .models import Firm, City, Personnel, Department, Education, Blood

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

class PersonnelForm(forms.ModelForm):
    previous_tckno = forms.CharField(
        label="Önceki Kaydı Bul (TCKNO ile)",
        required=False,
        help_text="Eğer bu personel daha önce başka bir firmada kayıtlıysa, TCKNO'sunu buraya yazarak iki kaydı bağlayabilirsiniz."
    )

    class Meta:
        model = Personnel
        # Formdan 'delete' ve 'related_personnel' alanlarını hariç tutuyoruz
        fields = [
        'name', 'surname', 'tckno', 'address', 'cell', 'birthday', 'driving_license', 'status', 'education', 'department', 'children', 'email', 'blood', 'military', 'gender', 'firm', 'department', 'commencement', 'termination', 'marital', 'picture', 'related_personnel'
        ]
        exclude = ['delete']
        #exclude = ['delete', 'related_personnel']
        widgets = {
            # Tüm tarih alanları için takvim widget'ı
            'birthday': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'commencement': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'termination': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),

            # Cinsiyet ve Askerlik için radyo butonları
            'gender': forms.RadioSelect,
            'military': forms.RadioSelect,
            'marital': forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seçim listelerini sırala
        self.fields['firm'].queryset = Firm.objects.filter(delete__isnull=True).order_by('name')
        self.fields['department'].queryset = Department.objects.order_by('name')
        self.fields['education'].queryset = Education.objects.order_by('id')
        self.fields['blood'].queryset = Blood.objects.order_by('id')

        instance = kwargs.get('instance')
        # Eğer bu yeni bir personel kaydı ise
        if not instance or not instance.pk:
            self.fields.pop('termination')

        # Eğer personel "soft delete" yapılmışsa
        if instance and instance.delete:
            self.fields['delete'] = forms.DateTimeField(
                label="Silinme Tarihi ve Saati",
                initial=instance.delete,
                widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
                required=False
            )

    # Form kaydedilirken TCKNO ile bulduğumuz personeli `related_personnel` alanına atayacağız.
    def save(self, commit=True):
        # ... (Bu metot aynı kalabilir) ...
        instance = super().save(commit=False)
        previous_tckno = self.cleaned_data.get('previous_tckno')
        if previous_tckno:
            try:
                previous_personnel = Personnel.objects.get(tckno=previous_tckno)
                instance.related_personnel = previous_personnel
            except Personnel.DoesNotExist:
                pass
        if commit:
            instance.save()
        return instance


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'firm']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Firma listesinde sadece aktif olanları gösterelim
        self.fields['firm'].queryset = Firm.objects.filter(delete__isnull=True).order_by('name')