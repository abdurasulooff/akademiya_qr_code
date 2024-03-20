from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from .models import Items
from .views import items_detail


class HomeViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.item = Items.objects.create(title="Test Item")

    def test_items_detail_view_status_code(self):
        request = self.factory.get(reverse('items:detail', args=[self.item.pk]))
        response = items_detail(request, self.item.pk)
        self.assertEqual(response.status_code, 200)

    def test_items_detail_view_template(self):
        request = self.factory.get(reverse('items:detail', args=[self.item.pk]))
        response = items_detail(request, self.item.pk)
        self.assertTemplateUsed(response, 'detail.html')

    def test_items_detail_view_context(self):
        request = self.factory.get(reverse('items:detail', args=[self.item.pk]))
        response = items_detail(request, self.item.pk)
        self.assertIn('item', response.context)
        self.assertIn('qrcode', response.context)
        self.assertEqual(response.context['item'].title, self.item.title)