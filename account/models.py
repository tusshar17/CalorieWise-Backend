from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Custome User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, otp, password=None, confirm_password=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(email=self.normalize_email(email), name=name)

        user.set_password(password)
        user.otp = otp
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, name, password=None, confirm_password=None, otp=1000
    ):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(email, password=password, name=name, otp=otp)
        user.is_admin = True
        user.otp = otp
        user.save(using=self._db)
        return user


# Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    otp = models.IntegerField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "otp"]

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


# class UserOTP(models.Model):
#     email = models.EmailField()
#     otp = models.IntegerField()
