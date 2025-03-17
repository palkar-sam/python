from django.shortcuts import render
from django.http import HttpResponse
from translate import Translator

# Create your views here.

def home(request):
    if(request.method == 'POST'):
        text = request.POST["translateTxt"];
        language = request.POST["lang"]
        trans = Translator(to_lang=language)
        translation = trans.translate(text)
        return HttpResponse(translation)
    return render(request, 'main/index.html')