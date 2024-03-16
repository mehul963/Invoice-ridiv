from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(date='2024-03-16', customer_name='Test Customer')

    def test_create_invoice(self):
        data = {
            "date": "2024-03-16",
            "customer_name": "John Doe",
            "details": [
                {
                    "description": "Product A",
                    "quantity": 2,
                    "unit_price": 10.00,
                    "price": 20.00
                },
                {
                    "description": "Product B",
                    "quantity": 1,
                    "unit_price": 18.00,
                    "price": 20.00
                }
            ]
        }

        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_invoice(self):
        response = self.client.get(f'/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, 200)
