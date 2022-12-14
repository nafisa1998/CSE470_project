from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import store, cart, checkout, updateItem



class TestUrls(SimpleTestCase):

    def test_store_url_is_resolves(self):
        url = reverse('store')
        self.assertEquals(resolve(url).func, store)

    def test_cart_url_is_resolves(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func, cart)

    def test_checkout_url_is_resolves(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_updateItem_url_is_resolves(self):
        url = reverse('update_item')
        self.assertEquals(resolve(url).func, updateItem)



