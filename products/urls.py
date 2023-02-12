from django.urls import path
from products.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('page/<int:page>/', ProductsListView.as_view(), name='page'),
    path('<slug:category_slug>/', ProductsListView.as_view(), name='category'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete/<int:pk>/', basket_delete, name='basket_delete'),
]
