from django.urls import path
from . import views

app_name = 'oral'

urlpatterns = [
    path('home/', views.home, name = 'home'),
    
]