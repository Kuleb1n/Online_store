from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from products.models import *
from django.core.paginator import Paginator


def index(request):
    return render(request, 'products/index.html')


def products(request, category_slug=None, page=1):
    context = {
        'categories': ProductCategory.objects.all(),
    }
    if category_slug:
        Products = Product.objects.filter(category__slug=category_slug).select_related()

    else:
        Products = Product.objects.all().select_related()
    paginator = Paginator(Products, 3)
    products_paginator = paginator.page(page)
    context.update({'Products': products_paginator})
    return render(request, 'products/products.html', context)


@login_required
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


@login_required
def basket_delete(request, pk):
    basket = Basket.objects.get(id=pk)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
