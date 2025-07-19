from django.db import models


class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)

    class Meta:
        managed = False
        db_table = 'city_'

    def __str__(self):
        return self.name


class District(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'district_'

    def __str__(self):
        return self.name


class Firm(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, blank=True, null=True)
    tax_office = models.ForeignKey('TaxOffice', models.DO_NOTHING, blank=True, null=True)
    nace = models.ForeignKey('Nace', models.DO_NOTHING, blank=True, null=True)
    create = models.DateTimeField(db_column='create_', blank=True, null=True)
    delete = models.DateTimeField(db_column='delete_', blank=True, null=True)
    address = models.CharField(db_column='address_', max_length=255, blank=True, null=True)
    telephone = models.CharField(db_column='telephone_', max_length=255, blank=True, null=True)
    fax = models.CharField(db_column='fax_', max_length=255, blank=True, null=True)
    email = models.CharField(db_column='email_', max_length=255, blank=True, null=True)
    type_firm = models.CharField(max_length=255, blank=True, null=True)
    tax = models.CharField(db_column='tax_', max_length=255, blank=True, null=True)
    web = models.CharField(db_column='web_', max_length=255, blank=True, null=True)
    sgk_sicil = models.CharField(max_length=255, blank=True, null=True)
    payment = models.CharField(db_column='payment_', max_length=255, blank=True, null=True)
    ceo_name = models.CharField(max_length=255, blank=True, null=True)
    ceo_email = models.CharField(max_length=255, blank=True, null=True)
    ceo_cell = models.CharField(max_length=255, blank=True, null=True)
    logo_media = models.ForeignKey('Media', on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField(db_column='active_')

    class Meta:
        managed = False
        db_table = 'firm_'

    def __str__(self):
        return self.name


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    short = models.CharField(db_column='short_', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language_'

    def __str__(self):
        return self.name


class Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    create = models.DateTimeField(db_column='create_', blank=True, null=True)
    media_type = models.ForeignKey('MediaType', on_delete=models.PROTECT, blank=True, null=True)
    path = models.ForeignKey('Path', on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    delete = models.DateTimeField(db_column='delete_', blank=True, null=True)
    active = models.BooleanField(db_column='active_')

    class Meta:
        managed = False
        db_table = 'media_'

    def __str__(self):
        return f"{self.path} {self.name}"


class MediaType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media_type'

    def __str__(self):
        return self.name


class Nace(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)
    code = models.CharField(db_column='code_', max_length=15)
    description = models.CharField(db_column='description_', max_length=511)

    class Meta:
        managed = False
        db_table = 'nace_'

    def __str__(self):
        return f"Name: {self.name} - Code: {self.code}"


class Path(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)

    class Meta:
        managed = False
        db_table = 'path_'

    def __str__(self):
        return self.name


class TaxOffice(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'tax_office'

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_group = models.ForeignKey('UserGroup', on_delete=models.PROTECT)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    tckno = models.CharField(db_column='tckno_', max_length=11, blank=True, null=True)
    certificate_number = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(db_column='title_', max_length=255, blank=True, null=True)
    email = models.CharField(db_column='email_', max_length=255, blank=True, null=True)
    #pasword_field = models.CharField(db_column='pasword_', max_length=32, blank=True, null=True)  # Field renamed because it ended with '_'.
    logo_media = models.ForeignKey(Media, on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField(db_column='active_')

    class Meta:
        managed = False
        db_table = 'user_'

    def __str__(self):
        return f"Name: {self.name} - TCKN: {self.tckno}"


class UserFirm(models.Model):
    pk = models.CompositePrimaryKey('user_id', 'firm_id')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    firm = models.ForeignKey(Firm, on_delete=models.PROTECT)
    create = models.DateTimeField(db_column='create_')

    class Meta:
        managed = False
        db_table = 'user_firm'

    def __str__(self):
        return f"User: {self.user} - Firm: {self.firm}"


class UserGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    description = models.CharField(db_column='description_', max_length=511, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group'

    def __str__(self):
        return self.name