from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
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
    paginate_by = 5


class UserTicketListView(ListView):
    model = Ticket
    template_name = 'ticket_system/user_tickets.html'
    context_object_name = 'tickets'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Ticket.objects.filter(author=user).order_by('-date_posted')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        email = User.objects.get(username=user).email
        queryset = queryset.filter(author=user).order_by('-date_posted')
        context['user'] = user
        context['email'] = email
        return context


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
