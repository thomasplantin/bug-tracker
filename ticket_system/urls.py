from django.urls import path
from .views import (
    TicketListView, 
    TicketDetailView, 
    TicketCreateView,
    TicketUpdateView,
    TicketDeleteView
)
from . import views


urlpatterns = [
    path('', TicketListView.as_view(), name='ticket-system-home'), # Calling the home function from the views.py file
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('ticket/new/', TicketCreateView.as_view(), name='ticket-create'),
    path('ticket/<int:pk>/update/', TicketUpdateView.as_view(), name='ticket-update'),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket-delete'),
    path('about/', views.about, name='ticket-system-about'), # Calling the about function from the views.py file
]