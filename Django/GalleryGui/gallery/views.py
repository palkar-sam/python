from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'gallery/products_list.html', {'products' : products})

# Create your views here.
def home(request):
    return HttpResponse("Hello This is to sowcase Gallery App");