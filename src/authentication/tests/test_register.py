import pytest
from authentication.forms.register import RegisterForm

@pytest.mark.django_db
@pytest.mark.parametrize(
    'username,password,confirm_password',
    [
        ('duong', 'doanh0111@', 'doanh0111@'),
    ]
)
def test_register_form_valid(username, password, confirm_password):
    form = RegisterForm(data={'username': username, 'password': password, 'password_confirm': confirm_password})
    assert form.is_valid()

@pytest.mark.django_db
@pytest.mark.parametrize(
    'username',
    [
        'alice',

        'user123',

        'user.name',

        'user@name',

        'user+name',

        'user-name',

        'user_name',
    ]
)
def test_register_form_valid_username(username):
    form = RegisterForm(data={
        'username': username,
        'password': 'alice0111@',
        'password_confirm': 'alice0111@',
        }
    )

    assert form.is_valid(), form.errors['username']


@pytest.mark.django_db
@pytest.mark.parametrize(
    'password, confirm_password, expected_errors',
    [
        ('short', 'short', ['This password is too short. It must contain at least 8 characters.']),

        ('0784253460', '0784253460', ['This password is entirely numeric.']),

        ('password', 'password', ['This password is too common.']),
    ]
)

def test_invalid_password(password, confirm_password, expected_errors):
    form = RegisterForm(data={
        'username': 'vinh',
        'password': password,
        'password_confirm': confirm_password,
    })
    assert form.is_valid() is False
    assert form.errors['password'] == expected_errors

@pytest.mark.django_db
def test_password_confirm_mismatch():
    form = RegisterForm(data={
        'username': 'vinh',
        'password': 'vinh1234',
        'password_confirm': 'vinh4321',
    })
    assert form.is_valid() is False
    assert form.errors['password_confirm'] == ['Passwords do not match']
