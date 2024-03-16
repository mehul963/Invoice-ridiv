from django.urls import path, include
from invoice.views import *
urlpatterns = [
    path('', CreateInvoice.as_view(),name='create_invoice'),
    path('<int:pk>/', GetInvoice.as_view(),name='get_invoice'),
]

