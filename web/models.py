from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    username= models.CharField(max_length=16, unique= True)
    is_staff= models.BooleanField(default=False)
    name = models.CharField(max_length=16)

    objects = UserManager()

    USERNAME_FIELD = "username"

    class Meta:
        db_table = "users"
