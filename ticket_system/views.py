from django.shortcuts import render
from .models import Ticket

# Create your views here.
def home(request):
    context = {
        'tickets': Ticket.objects.all(),
    }
    return render(request, 'ticket_system/home.html', context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'ticket_system/about.html', context)
