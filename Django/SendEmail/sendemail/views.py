from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    context = {}
    if(request.method == "POST"):
        address = request.POST['address']
        subject = request.POST['subject']
        message = request.POST['message']
        print(address, subject, message)
        if(address and subject and message):
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = "Email sent successfully"
            except Exception as e:
                context['result'] = f"Email could not be sent : {e}"
        else:
            context['result'] = "Please fill all the fields"

    return render(request, 'sendemail/index.html', context)