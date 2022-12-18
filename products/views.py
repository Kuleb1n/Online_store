from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'products/index.html')


def products(request):
    categories = ProductCategory.objects.all()
    Products = Product.objects.all()
    context = {
        'categories': categories,
        'Products': Products,
    }
    return render(request, 'products/products.html', context)
