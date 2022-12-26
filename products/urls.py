from django.urls import path
from products.views import *

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete/<int:pk>/', basket_delete, name='basket_delete'),
]
