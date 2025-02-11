import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    return HttpResponse("Hello, Django!")

def HelloThere(request, name):
    now  = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    #fileter the name argument to letters only using regular expressions. url arguments
    #can contain arbitrary text, so we can restrct to safe characters only.

    match_obj = re.match("[a-zA-z]+", name)

    if match_obj:
        clean_name = match_obj.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! it's " + formatted_now

    return HttpResponse(content);    

def HelloTemplate(request, name):
    print("Debug url : ",request.build_absolute_uri()) #optional

    return render(
        request,
        'hello/HelloTemplate.html',
        {
            'name':name,
            'date':datetime.now()
        }
    )

def HelloDispatch(request, name):
    type = request.GET.get("type")

    if(type == "template"):
        return HelloTemplate(request, name)
    else:
        return HelloThere(request, name)
    