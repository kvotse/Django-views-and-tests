from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode
from django.shortcuts import get_object_or_404
from .models import News, Category

class TestViews(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Test Category')
        self.news = News.objects.create(
            title='Test News',
            category=self.category
        )

    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)



    def test_redirect_view(self):
        response = self.client.get('/redirect/')
        self.assertEqual(response.status_code, 302)

    def test_form_view_get(self):
        response = self.client.get('/form/')
        self.assertEqual(response.status_code, 200)
