from django.shortcuts import render

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
