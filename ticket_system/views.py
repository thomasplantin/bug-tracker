from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)
from .models import Ticket

# Create your views here.
def home(request):
    context = {
        'tickets': Ticket.objects.all(),
    }
    return render(request, 'ticket_system/home.html', context)


class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket_system/home.html'
    context_object_name = 'tickets'
    ordering = ['-date_posted']


class TicketDetailView(DetailView):
    model = Ticket


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields=['title', 'description', 'assignee', 'priority', 'deadline', 'state']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'ticket_system/about.html', context)
