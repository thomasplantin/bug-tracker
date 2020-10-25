from django.forms import ModelForm, Textarea
from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Meta:
    db_table = "users"
