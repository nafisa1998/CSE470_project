from django.test import TestCase
from store.models import Customer, Product, Order, OrderItem, ShippingAddress
from faker import Faker
fake = Faker()

# Create your tests here.

class FirstTestCase(TestCase):

    def setUp(self):
        print('setup called')
    # def test_equal(self):
    #     self.assertEqual(1,1)

    def test_customer(self):
        names = ['nafisa', 'anika']

        for n in names:
            obj = Customer.objects.create(
                name = n
            )
            self.assertEquals(n, obj.name)

        objs = Customer.objects.all()

        self.assertEqual(objs.count(), 2)

