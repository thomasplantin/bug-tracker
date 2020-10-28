from django.shortcuts import render
from datetime import datetime

# Dummy Data
issues = [
    {
        'title': 'Bug Post 1',
        'description': 'First post content',
        'ticket_id': '13698',
        'author': 'CoreyMS',
        'assignee': 'Jane Doe',
        'date_posted': '1567399723',
        'deadline': '1568476800',
        'priority': 'low',
        'state': 'open',
    }, 
    {
        'title': 'Bug Post 2',
        'description': 'Second post content',
        'ticket_id': '13697',
        'author': 'Jane Doe',
        'assignee': '',
        'date_posted': '1567299943',
        'deadline': '1568476800',
        'priority': 'high',
        'state': 'closed',
    }, 
    {
        'title': 'Bug Post 3',
        'description': 'Third post content',
        'ticket_id': '13696',
        'author': 'Thomas Plantin',
        'assignee': 'Rodrigo Zurita',
        'date_posted': '1567345932',
        'deadline': '',
        'priority': 'med',
        'state': 'under development',
    }
]

# Sort the posts by date_posted and convert timestamp
issues.sort(key=lambda item:item['date_posted'], reverse=True)
for issue in issues:
    issue['date_posted'] = datetime.fromtimestamp(int(issue['date_posted']))
    if issue['deadline'] != '': # if there is a specified deadline
        issue['deadline'] = datetime.fromtimestamp(int(issue['deadline']))

# Create your views here.
def home(request):
    context = {
        'issues': issues,
    }
    return render(request, 'ticket_system/home.html', context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'ticket_system/about.html', context)


def login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'ticket_system/login.html', context)


def register(request):
    context = {
        'title': 'Register',
    }
    return render(request, 'ticket_system/register.html', context)
