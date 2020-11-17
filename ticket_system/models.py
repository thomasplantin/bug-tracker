from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
class Ticket(models.Model):
    
    def no_past_date(value):
        if value.date() < date.today():
            raise ValidationError('Deadline cannot be in the past.')

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assignee', null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(null=True, blank=True, validators=[no_past_date])
    priority = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return "Title = {} written by {} on {}.".format(self.title, self.author, self.date_posted)

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.pk})
