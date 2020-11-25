from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Client(models.Model):
    client_id = models.IntegerField()
    client_name = models.CharField(max_length=50)
    client_type = models.CharField(max_length=30)

    def __str__(self):
        return self.client_name


class UserManager(BaseUserManager):
    def create_user(self, first_name, middle_name, last_name,  company, job_title, office_phone, cell_phone, appellation, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            email=self.normalize_email(email),
            username=username,
            company=company,
            job_title=job_title,
            office_phone=office_phone,
            cell_phone=cell_phone,
            appellation=appellation
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, first_name, middle_name, last_name, email, username, password, company, job_title, office_phone, cell_phone, appellation):
        user = self.create_user(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password,
            username=username,
            company=company,
            job_title=job_title,
            office_phone=office_phone,
            cell_phone=cell_phone,
            appellation=appellation
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    office_phone = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20)
    appellation = models.CharField(max_length=10)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', ]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class Location(models.Model):
    location_id = models.IntegerField()
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=50)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.address1


class TestStandard(models.Model):
    standard_id = models.IntegerField()
    standard_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    published_date = models.CharField(max_length=30)


    def __str__(self):
        return self.standard_name


class Certificate(models.Model):
    certificate_number = models.IntegerField()
    certificate_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    report_number = models.IntegerField()
    issue_date = models.CharField(max_length=50)
    standard_id = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    model_number = models.IntegerField()


    def __str__(self):
        return self.certificate_number


class Product(models.Model):
    model_number = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    cell_technology = models.CharField(max_length=50)
    cell_manufacturer = models.CharField(max_length=50)
    number_cells = models.IntegerField()
    number_cells_series = models.IntegerField()
    number_cells_strings = models.IntegerField()
    number_diodes = models.IntegerField()
    product_length = models.CharField(max_length=30)
    product_width = models.CharField(max_length=30)
    product_weight = models.CharField(max_length=30)
    superstate_type = models.CharField(max_length=50)
    superstate_manufacturer = models.CharField(max_length=50)
    substrate_type = models.CharField(max_length=50)
    substrate_manufacturer = models.CharField(max_length=50)
    frame_type = models.CharField(max_length=50)
    frame_adhesive = models.CharField(max_length=30)
    encapsulate_type = models.CharField(max_length=30)
    encapsulate_manufacturer = models.CharField(max_length=50)
    junction_box_type = models.CharField(max_length=50)
    junction_box_manufacturer = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
