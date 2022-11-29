from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from sqlalchemy import null
from datetime import datetime
#  Custom User Manager


class UserManager(BaseUserManager):
    def create_user(self, email, name, username, phone_number, password=None, password2=None, otp=None):
        """
        Creates and saves a User with the given email, username, phone_number and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number,
            username=username

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, password=None):
        """
        Creates and saves a superuser with the given name ,phone_number,password.
        """
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            phone_number=phone_number
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#  Custom User Model


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=255, null=True, blank=True)
    phone_number = models.CharField(
        unique=False, null=True, blank=True, max_length=13)
    otp = models.CharField(max_length=6, default='')
    emailotp = models.CharField(max_length=6, default='')
    emailotptime = models.CharField(
        max_length=100, default=datetime.now().strftime("%H%M%S"))
    otptime = models.CharField(
        max_length=100, default=datetime.now().strftime("%H%M%S"))
    is_phone_verified = models.BooleanField(default=False)
    name = models.CharField(max_length=200, default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_type = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    user_type_id = models.IntegerField(default=None, null=True, blank=True)
    provider_choices = (
        ("facebook", "facebook"),
        ("google", "google"),
        ("instagram", "instagram"),
        ("twitter", "twitter"),
        ("linkedin", "linkedin"),
        ("usingemail", "usingemail")
    )
    provider = models.CharField(
        choices=provider_choices, max_length=50, default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
