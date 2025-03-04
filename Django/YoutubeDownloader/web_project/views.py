from django.shortcuts import render
from pytube import YouTube

def youtube(request):
    if(request.method == "POST"):
        link = request.POST['link']
        print(f"link url : {link}")
        video = YouTube(link)
        
        stream = video.streams.get_lowest_resolution()
        stream.download()

        return render(request, 'youtube.html', {'video': video})
    
    return render(request, 'youtube.html')
                            