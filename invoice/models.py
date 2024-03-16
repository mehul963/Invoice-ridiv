from django.db import models

# Create your models here.

class Invoice(models.Model):
    #  Date, Invoice CustomerName.
    date = models.DateField()
    customer_name = models.CharField(max_length=100)


class InvoiceDetail(models.Model):
    # invoice (ForeignKey), description, quantity, unit_price, price.
    invoice = models.ForeignKey(Invoice,related_name='details',on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits = 10,decimal_places=2)
    price = models.DecimalField(max_digits = 10,decimal_places=2)