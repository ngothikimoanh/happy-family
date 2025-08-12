from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from constants.roles import Roles

class _UserManager(BaseUserManager):
    def create_user(self, username: str, password: str, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(raw_password = password)
        user.save()
        return user

    def create_superuser(self, username:str, password:str, **extra_fields):
        extra_fields['is_staff']= True
        extra_fields['role'] = Roles.ADMIN
        return self.create_user(username=username, password=password, **extra_fields)

class User(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True, db_index=True)

    is_staff = models.BooleanField(default=False)
    role = models.CharField(null=True, blank= True)

    objects = _UserManager()

    USERNAME_FIELD = "username"

    def has_module_perms(self, _):
        return self.is_staff is True and self.role == Roles.ADMIN

    def has_perm(self, _, __=None):
        return self.has_module_perms(None)

    class Meta:
        db_table = 'users'
