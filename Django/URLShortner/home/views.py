from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'index1.html')

def index_form(request):
    if(request.method == 'POST'):
        long_url = request.POST['long_url']
        new_url = shorten_url(long_url)
        print(f"Post url : {request.POST}")
    return render(request, 'index.html')

# function to shorten url 
def shorten_url(url):
    # define access token in headers 
    headers = { 
        'Authorization': 'Bearer 59b93ed08a4f98d26557814ec2434f4b5436ea1b', 
        # 'Authorization': 'Bearer {TOKEN}', 
        'Content-Type': 'application/json', 
    } 
  
    data_dict = {"long_url": url, "domain": "bit.ly"} 
  
    # convert data_dict to json 
    data = json.dumps(data_dict) 
  
    # getting response which will be in json string 
    response = requests.post( 
        'https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data) 
  
    # convert json string to dict 
    response_dict = json.loads(response.text) 
  
    print(f"Short url response : {response_dict}") 
    return response_dict['link'] 