from datetime import datetime

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    UserManager,
)
from django.db import models
from model_utils import Choices

from utilities.image_validation import validate_image


def upload_path(instance, filename):
    """Storing an image with directory post_image with custom file name"""
    now = datetime.now()
    now_string = now.strftime("%d-%m-%Y %H:%M:%S")
    new_filename = now_string + filename
    return "/".join(["post_image", new_filename])


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and Save a new User"""
        if not email:
            raise ValueError("User must have email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """Creates and save a new superuser"""
        if not email:
            raise ValueError("User must have email address")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Create your models here.
class Contactinfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    category = models.CharField(max_length=30)
    date = models.DateTimeField(unique=True)
    phoneNumber = models.CharField(max_length=30)
    location = models.CharField(max_length=40)
    description = models.TextField()


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instade of the default username"""

    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=60, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.name

