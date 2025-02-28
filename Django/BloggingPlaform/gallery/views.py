from django.shortcuts import render
from gallery.models import Product

# Create your views here.

def ProductList(request):
    products = Product.objects.all()
    return render(request, 'gallery/product_list.html', {'products': products})