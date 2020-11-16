from django.urls import path
from .views import (
    TicketListView, 
    TicketDetailView, 
    TicketCreateView
)
from . import views


urlpatterns = [
    path('', TicketListView.as_view(), name='ticket-system-home'), # Calling the home function from the views.py file
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('ticket/new/', TicketCreateView.as_view(), name='ticket-create'),
    path('about/', views.about, name='ticket-system-about'), # Calling the about function from the views.py file
]