from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='ticket-system-home'), # Calling the home function from the views.py file
    path('about/', views.about, name='ticket-system-about'), # Calling the about function from the views.py file
    path('login/', views.login, name='ticket-system-login'),
    path('register/', views.register, name='ticket-system-register'),
]