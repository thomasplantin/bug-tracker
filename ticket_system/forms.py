from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        priorities = [
            ('low', 'Moderate'),
            ('medium', 'Important'),
            ('high', 'Critical')
        ]
        states = [
            ('open', 'Open'),
            ('closed', 'Closed'),
            ('staged', 'Staging')
        ]
        widgets = {
            'priority': forms.Select(choices=priorities),
            'state': forms.Select(choices=states),
            'deadline': forms.TextInput(attrs={'type':'date'}),
        }
        fields = [
            'title', 
            'description', 
            'assignee', 
            'priority', 
            'state',
            'deadline'
        ]
