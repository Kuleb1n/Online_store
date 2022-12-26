from django.http import HttpResponseRedirect
from django.shortcuts import render
from products.models import *


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


def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)


def basket_delete(request, pk):
    basket = Basket.objects.get(id=pk)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
