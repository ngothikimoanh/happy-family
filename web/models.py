from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator


username_validator = RegexValidator(
    regex = r'^\w+$',
    message="Username can only contain letters, numbers, and underscores.."
)

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
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        USER = 'USER', 'User'

    
    username = models.CharField(
        max_length=16,
        unique=True,
        validators=[username_validator]
    )

    is_staff= models.BooleanField(default=False)
    name = models.CharField(max_length=16)
    birthday_year = models.PositiveSmallIntegerField()
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER
    )

    objects = UserManager()

    USERNAME_FIELD = "username"

    class Meta:
        db_table = "users"
