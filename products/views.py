from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, ListView

from products.models import *


class IndexView(TemplateView):
    template_name = 'products/index.html'


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'Products'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category__slug = self.kwargs.get('category_slug')
        return Product.objects.filter(
            category__slug=category__slug).select_related() if category__slug else queryset.select_related()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all().select_related()
        return context


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_delete(request, pk):
    basket = Basket.objects.get(id=pk)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
