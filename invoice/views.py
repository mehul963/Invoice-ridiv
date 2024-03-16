from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView,CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from invoice.models import *
from invoice.serializers import *
# Create your views here.

class CreateInvoice(CreateAPIView):
    serializer_class = InvoiceSerializer
    

class GetInvoice(RetrieveAPIView):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        invoice_id = self.kwargs['pk']
        return Invoice.objects.filter(pk=invoice_id)
