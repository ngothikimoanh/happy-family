from django import forms
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password

from authentication.models.user import User

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=32, validators=[UnicodeUsernameValidator()])
    password = forms.CharField(min_length=6, max_length=16, validators=[validate_password])
    password_confirm = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data['username']
        username = username.lower()

        if User.objects.filter(username=username).exists:
            raise forms.ValidationError('Username already exits')

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data['password_confirm']

        if password and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return password_confirm
