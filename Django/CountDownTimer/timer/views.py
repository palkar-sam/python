from django.shortcuts import render
from django.utils import timezone
from .models import Event

# Create your views here.
def index(request):
    return render(request, 'timer/index.html')

def countdown_timer(request):
    event = Event.objects.first()
    if (event):
        time_remaining = event.event_date - timezone.now()
        hours = time_remaining.seconds // 3600
        seconds = time_remaining.seconds % 3600
        minutes = seconds // 60

        data = {
            'name': event.name,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds % 60
        }
    else:
        data = {
            'name': 'No Event',
            'hours': 0,
            'minutes':0,
            'seconds':0
        }
    
    return render(request, 'timer/countdown_timer.html', data)