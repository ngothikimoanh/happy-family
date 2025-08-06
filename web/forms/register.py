from django import forms
from typing import Any

from web.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=16)
    display_name= forms.CharField(max_length=16)
    birthday_year = forms.IntegerField()
    password = forms.CharField(max_length=128)
    password_confirm = forms.CharField(max_length=128)

    def clean_password_confirm(self):
        password: str = self.cleaned_data.get("password", "")
        password_confirm: str = self.cleaned_data.get("password_confirm", "")

        if password and password != password_confirm:
            raise forms.ValidationError("Confirm password mismatch with password")
        return password_confirm

    def save(self) -> Any:
        user_create_args = {
            "username": self.cleaned_data.get("username"),
            "display_name": self.cleaned_data.get("display_name"),
            "birthday_year": self.cleaned_data.get("birthday_year"),
            "password": self.cleaned_data.get("password"),
        }

        if not User.objects.exists():
            user = User.objects.create_superuser(**user_create_args)  # type: ignore
        else:
            user = User.objects.create_user(**user_create_args)  # type: ignore

        return user