from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect


def require_login(view_func):
    def wrapped_view(request: HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "Bạn cần đăng nhập")
            return redirect("login")
        return view_func(request, *args, **kwargs)
    return wrapped_view
