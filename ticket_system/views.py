from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Ticket
from .forms import TicketForm

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
    form_class = TicketForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    form_class = TicketForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.author:
            return True
        return False


class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    success_url = '/'

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.author:
            return True
        return False


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'ticket_system/about.html', context)
