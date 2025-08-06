from django.urls import path

from web import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('costs', views.cost_view, name='cost'),
    path('humansource', views.humansource_view, name='humansource'),
    path('calendar', views.calendar_view, name='calendar'),
    path('storage', views.storage_view, name='storage'),
    path('register', views.register_view,name='register'),
]
