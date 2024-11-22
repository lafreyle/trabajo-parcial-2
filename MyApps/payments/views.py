from django.shortcuts import render  # Import render for rendering templates (not used in this code)
from django.http import HttpResponse  # Import HttpResponse for returning simple HTTP responses
from django.http import Http404  # Import Http404 for raising 404 errors

from rest_framework.response import Response  # Import Response for returning DRF responses
from rest_framework import generics  # Import generics for class-based views

from rest_framework import status  # Import status for HTTP status codes

from MyApps.payments.models import Payment  # Import the Payment model
from MyApps.payments.serializers import PaymentSerializer  # Import the Payment serializer

"""
The imports at the top of the file include necessary modules from Django and Django REST Framework.
render is imported but not used in this code. If you plan to render templates, you can use it; otherwise, you can remove it.
HttpResponse is used to return simple HTTP responses, such as the welcome message in the home view.
Http404 is imported but not used in this code. You can use it to raise 404 errors if a resource is not found.
Response is used to return responses in DRF views.
generics provides class-based views for common patterns like listing, creating, retrieving, updating, and deleting objects.
status is used to define HTTP status codes.
"""


# Create your views here.

def home(request):
    return HttpResponse("Bienvenidos, Uniguajira! - Aplicación Clientes")  # Simple welcome message

class PaymentList(generics.ListCreateAPIView):
    """
    Lista de Pagos
    """
    queryset = Payment.objects.all()  # Queryset to retrieve all Payment objects
    serializer_class = PaymentSerializer  # Specify the serializer to use for this view

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los pagos por pk
    """
    queryset = Payment.objects.all()  # Queryset to retrieve all Payment objects
    serializer_class = PaymentSerializer  # Specify the serializer to use for this view

"""
Home View:

The home function returns a simple HTTP response with a welcome message. This view can be accessed via the URL pattern you defined earlier.
PaymentList View:

class PaymentList(generics.ListCreateAPIView): This class-based view handles listing all payments and creating a new payment.
queryset = Payment.objects.all(): This defines the queryset to retrieve all Payment objects from the database.
serializer_class = PaymentSerializer: This specifies the serializer to use for serializing and deserializing Payment objects.
PaymentDetail View:

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView): This class-based view handles retrieving, updating, and deleting a specific payment identified by its primary key (pk).
queryset = Payment.objects.all(): This defines the queryset to retrieve all Payment objects.
serializer_class = PaymentSerializer: This specifies the serializer to use for this view.

""" 