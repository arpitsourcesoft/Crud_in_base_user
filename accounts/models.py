from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from accounts.manager import UserManager


# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=14)
    password = models.CharField(max_length=4)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

