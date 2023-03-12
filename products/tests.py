from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):

    def test_index_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):
    fixtures = []

    def setUp(self):
        self.products = Product.objects.all()

    def _common_product_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_products_list(self):
        path = reverse('products')
        response = self.client.get(path)

        self._common_product_tests(response)
        self.assertEqual(list(response.context_data['object_list']), list(self.products[:3]))

    def test_products_list_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products', kwargs={'category_slug': category.slug})
        response = self.client.get(path)

        self._common_product_tests(response)
        self.assertEqual(list(response.context_data['object_list']),
                         list(self.products.filter(category__slug=category.slug)))
