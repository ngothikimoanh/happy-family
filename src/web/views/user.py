from http import HTTPMethod

from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import redirect, render

from web.forms.user import LoginForm
from web.decorators.user import require_login, require_not_login


@require_not_login
def login_view(request: HttpRequest):
    form = LoginForm(request.POST or None)

    if request.method == HTTPMethod.POST:
        if form.is_valid():
            login(request=request, user=form.user)
            return render(request, "pages/redirect.html")
        messages.error(request, "Đăng nhập thất bại, vui lòng kiểm tra lại thông tin.")

    return render(request, "pages/login.html", {"form": form})
