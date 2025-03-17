from django.shortcuts import render, HttpResponse
import wikipedia

# Create your views here.
def index(request):
    if(request.method == 'POST'):

        search = request.POST['search']
        try:
            result = wikipedia.summary(search, sentences = 3)
        except:
            return HttpResponse("Wrong input")
        return render(request, "main/index.html", {'result':result})
    else:
        return render(request, "main/index.html")
