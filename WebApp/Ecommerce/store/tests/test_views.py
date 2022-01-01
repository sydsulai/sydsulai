# import unittest
from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import reverse
from django.test import Client, RequestFactory, TestCase

from store.models import Category, Product
from store.views import all_products


@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_example(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, title='django beginners', created_by=1, slug='django-beginners',
                               price='20.00')

    def test_url_allowed_hosts(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse('store:product_detail', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail(self):
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        print(html)
        self.assertIn('<title>Home</title>', html)
        self.assertEqual(response.status_code, 200)

    def test_views_function(self):
        request = self.factory.get('/item/django-beginners')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertEqual(response.status_code, 200)
