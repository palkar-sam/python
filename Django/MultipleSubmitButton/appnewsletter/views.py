from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import newslatteremail

# Create your views here.
def index(request):
    if 'subscribe' in request.POST:
        email = newslatteremail()
        email.userEmail = request.POST['email']
        email.save()
        messages.info(request, "You have successfully subscribed to our newsletter.")
    
    if 'unsubscribe' in request.POST:
        email = newslatteremail.objects.get(userEmail=request.POST.get('email'))
        email.delete()
        messages.info(request, "Sorry to see you!!!")

    return render(request, 'news.html')

