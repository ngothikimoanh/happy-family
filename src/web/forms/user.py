
from django import forms

from web.models.user import User


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    password = forms.CharField(max_length=128)
    user: User | None = None
