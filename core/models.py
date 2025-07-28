from datetime import timezone
import os
from django.conf import settings
from django.db import models


class Blood(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=15)

    class Meta:
        managed = False
        db_table = 'blood_'

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)

    class Meta:
        managed = False
        db_table = 'city_'

    def __str__(self):
        return f"{self.name}"


class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    firm = models.ForeignKey('Firm', models.PROTECT, related_name='departments')
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_'

    def __str__(self):
        return f"{self.name} ({self.firm.name})"


class District(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)
    city = models.ForeignKey(City, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'district_'

    def __str__(self):
        return f"{self.name} ({self.city.name})"


class Education(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=15)

    class Meta:
        managed = False
        db_table = 'education_'

    def __str__(self):
        return f"{self.name}"


class Firm(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, verbose_name="Firma Adı")
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Şehir")
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True, null=True, verbose_name="İlçe")
    tax_office = models.ForeignKey('TaxOffice', on_delete=models.PROTECT, blank=True, null=True, verbose_name="Vergi Daire")
    nace = models.ForeignKey('Nace', on_delete=models.PROTECT, blank=True, null=True, verbose_name="NACE kodu")
    create = models.DateField(db_column='create_', blank=True, null=True, verbose_name="Oluşturma Tarihi")
    delete = models.DateTimeField(db_column='delete_', blank=True, null=True, verbose_name="Silinme Tarihi")
    address = models.CharField(db_column='address_', max_length=255, blank=True, null=True, verbose_name="Adres")
    telephone = models.CharField(db_column='telephone_', max_length=255, blank=True, null=True, verbose_name="Telefon")
    fax = models.CharField(db_column='fax_', max_length=255, blank=True, null=True, verbose_name="Faks")
    email = models.CharField(db_column='email_', max_length=255, blank=True, null=True, verbose_name="e-Posta")
    type_firm = models.CharField(max_length=255, blank=True, null=True, verbose_name="Firma Türü")
    tax = models.CharField(db_column='tax_', max_length=255, blank=True, null=True, verbose_name="Vergi Numara")
    web = models.CharField(db_column='web_', max_length=255, blank=True, null=True, verbose_name="İnternet Site")
    sgk_sicil = models.CharField(max_length=255, blank=True, null=True, verbose_name="SGK Sicil No")
    payment = models.CharField(db_column='payment_', max_length=255, blank=True, null=True, verbose_name="Ödeme Tipi")
    ceo_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Yetkili")
    ceo_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Yetkili e-Posta")
    ceo_cell = models.CharField(max_length=255, blank=True, null=True, verbose_name="Yetkili Telefon")
    #logo_media = models.ForeignKey('Media', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Firma Logo")
    logo_media = models.FileField(upload_to='logo_firm/', blank=True, null=True, verbose_name="Firma Logosu")
    active = models.BooleanField(db_column='active_')

    def save(self, *args, **kwargs):
        # Eğer bu, veritabanında zaten var olan bir kayıt ise (yani güncelleme yapılıyorsa)
        if self.pk:
            try:
                # Veritabanındaki eski halini çek
                eski_kayit = Firm.objects.get(pk=self.pk)
                # Eğer eski kaydın logosu varSA ve yeni logo ile aynı DEĞİLSE
                if eski_kayit.logo_media and eski_kayit.logo_media != self.logo_media:
                    # Eski dosyanın yolunu al ve sil
                    eski_dosya_yolu = os.path.join(settings.MEDIA_ROOT, str(eski_kayit.logo_media))
                    if os.path.isfile(eski_dosya_yolu):
                        os.remove(eski_dosya_yolu)
            except Firm.DoesNotExist:
                pass # Kayıt henüz veritabanında yok, bir şey yapma

        # Django'nun asıl save metodunu çalıştırarak kaydı tamamla
        super(Firm, self).save(*args, **kwargs)

    '''
    def delete_hard(self, *args, **kwargs):
        # Eğer silinmekte olan kaydın bir logosu varsa
        if self.logo_media:
            # Dosyanın yolunu al ve sil
            dosya_yolu = os.path.join(settings.MEDIA_ROOT, str(self.logo_media))
            if os.path.isfile(dosya_yolu):
                os.remove(dosya_yolu)

        # Django'nun asıl delete metodunu çalıştırarak kaydı veritabanından sil
        super(Firm, self).delete(*args, **kwargs)
    '''

    def delete_soft(self, *args, **kwargs):
        self.delete = timezone.now()
        self.save()

    class Meta:
        managed = False
        db_table = 'firm_'

    def __str__(self):
        return f"{self.name}"


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    short = models.CharField(db_column='short_', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language_'

    def __str__(self):
        return f"{self.name} ({self.short})"


class Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    create = models.DateTimeField(db_column='create_', blank=True, null=True)
    media_type = models.ForeignKey('MediaType', models.PROTECT, blank=True, null=True)
    path = models.ForeignKey('Path', models.PROTECT, blank=True, null=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    delete = models.DateTimeField(db_column='delete_', blank=True, null=True)
    active = models.BooleanField(db_column='active_')

    class Meta:
        managed = False
        db_table = 'media_'

    def __str__(self):
        path_name = self.path.name if self.path else 'Yol Yok'
        media_type_name = self.media_type.name if self.media_type else 'Tip Yok'
        return f"{self.name} ({path_name} {media_type_name})"


class MediaType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media_type'

    def __str__(self):
        return f"{self.name}"


class Nace(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)
    code = models.CharField(db_column='code_', max_length=15)
    description = models.CharField(db_column='description_', max_length=511)

    class Meta:
        managed = False
        db_table = 'nace_'

    def __str__(self):
        return f"{self.code} ({self.name})"


class Path(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)

    class Meta:
        managed = False
        db_table = 'path_'

    def __str__(self):
        return f"{self.name}"


class Personnel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    surname = models.CharField(db_column='surname_', max_length=255, blank=True, null=True)
    tckno = models.CharField(db_column='tckno_', max_length=11, blank=True, null=True)
    address = models.CharField(db_column='address_', max_length=255, blank=True, null=True)
    cell = models.CharField(db_column='cell_', max_length=15, blank=True, null=True)
    birthday = models.DateTimeField(db_column='birthday_', blank=True, null=True)
    driving_license = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(db_column='status_', max_length=255, blank=True, null=True)
    education = models.ForeignKey(Education, on_delete=models.PROTECT, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True)
    children = models.IntegerField(db_column='children_')
    email = models.CharField(db_column='email_', max_length=255, blank=True, null=True)
    blood = models.ForeignKey(Blood, on_delete=models.PROTECT, blank=True, null=True)
    military = models.BooleanField(db_column='military_')
    gender = models.BooleanField(db_column='gender_')
    marital = models.BooleanField(db_column='marital_')

    class Meta:
        managed = False
        db_table = 'personnel_'

    def __str__(self):
        return f"{self.name} ({self.tckno})"


class TaxOffice(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)
    city = models.ForeignKey(City, models.PROTECT)
    district = models.ForeignKey(District, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'tax_office'

    def __str__(self):
        return f"{self.name} ({self.city.name} {self.district.name})"


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_group = models.ForeignKey('UserGroup', models.PROTECT)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    tckno = models.CharField(db_column='tckno_', max_length=11, blank=True, null=True)
    certificate_number = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(db_column='title_', max_length=255, blank=True, null=True)
    email = models.CharField(db_column='email_', max_length=255, blank=True, null=True)
    #pasword = models.CharField(db_column='pasword_', max_length=32, blank=True, null=True)
    logo_media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(db_column='active_')

    class Meta:
        managed = False
        db_table = 'user_'

    def __str__(self):
        return f"{self.name} ({self.tckno})"


class UserFirm(models.Model):
    pk = models.CompositePrimaryKey('user_id', 'firm_id')
    user = models.ForeignKey(User, models.PROTECT, related_name='firm_associations')
    firm = models.ForeignKey(Firm, models.PROTECT, related_name='user_associations')
    create = models.DateTimeField(db_column='create_')

    class Meta:
        managed = False
        db_table = 'user_firm'

    def __str__(self):
        return f"{self.user.name} ({self.firm.name})"


class UserGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    description = models.CharField(db_column='description_', max_length=511, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group'

    def __str__(self):
        return f"{self.name} ({self.description})"