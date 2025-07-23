from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    firm = models.ForeignKey('Firm', models.PROTECT)
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    name = models.CharField(db_column='name_', max_length=255)
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True, null=True)
    tax_office = models.ForeignKey('TaxOffice', on_delete=models.PROTECT, blank=True, null=True)
    nace = models.ForeignKey('Nace', on_delete=models.PROTECT, blank=True, null=True)
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
    logo_media = models.ForeignKey('Media', on_delete=models.SET_NULL, null=True, blank=True, null=True)
    active = models.BooleanField(db_column='active_')

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
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True, null=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    tckno = models.CharField(db_column='tckno_', max_length=11, blank=True, null=True)
    certificate_number = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(db_column='title_', max_length=255, blank=True, null=True)
    email = models.CharField(db_column='email_', max_length=255, blank=True, null=True)
    #pasword = models.CharField(db_column='pasword_', max_length=32, blank=True, null=True)
    logo_media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True, null=True)
    active = models.BooleanField(db_column='active_')

    class Meta:
        managed = False
        db_table = 'user_'

    def __str__(self):
        return f"{self.name} ({self.tckno})"


class UserFirm(models.Model):
    pk = models.CompositePrimaryKey('user_id', 'firm_id')
    user = models.ForeignKey(User, models.PROTECT)
    firm = models.ForeignKey(Firm, models.PROTECT)
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