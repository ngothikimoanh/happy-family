from datetime import date
from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render

from web.forms.register import RegisterForm

# Create your views here.
def home_view(request):
    return render(request, "pages/home.html")

def cost_view(request):
    return render(request, "pages/cost.html")

def humansource_view(request):
    return render(request, "pages/humansource.html")

def calendar_view(request):
    return render(request, "pages/calendar.html")

def storage_view(request):
    return render(request, "pages/storage.html")


def register_view(request: HttpRequest):
    current_year = date.today().year
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, "Registration failed, please check your information.")

    return render(request, 'pages/register.html', {
        'form': form,
        'current_year': current_year
    })