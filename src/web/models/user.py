from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone_number: str, password: str, **extra_fields):
        if not phone_number:
            raise ValueError("Bạn chưa nhập số điện thoại")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)

        user.save()
        return user
