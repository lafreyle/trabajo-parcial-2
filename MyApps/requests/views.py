from django.shortcuts import render  # Import render for rendering templates (not used in this code)
from django.http import HttpResponse, Http404  # Import HttpResponse and Http404 for HTTP responses

from rest_framework.response import Response  # Import Response for returning DRF responses
from rest_framework import generics  # Import generics for DRF class-based views
from rest_framework import status  # Import status for HTTP status codes

from MyApps.requests.models import LoanApplication  # Import the LoanApplication model
from MyApps.requests.serializers import LoanApplicationSerializer  # Import the LoanApplication serializer

# Create your views here.
def home(request):
    """
    Home view that returns a welcome message.
    """
    return HttpResponse("Bienvenidos, Uniguajira! - Aplicación Clientes")

class LoanApplicationList(generics.ListCreateAPIView):
    """
    View to list all loan applications or create a new one.
    """
    queryset = LoanApplication.objects.all()  # Queryset for retrieving loan applications
    serializer_class = LoanApplicationSerializer  # Serializer for converting model instances to JSON

class LoanApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a loan application by primary key (pk).
    """
    queryset = LoanApplication.objects.all()  # Queryset for retrieving loan applications
    serializer_class = LoanApplicationSerializer  # Serializer for converting model instances to JSON

"""

Imports:
The imports at the top include necessary modules from Django and Django REST Framework.
HttpResponse is used to return simple HTTP responses, while Http404 can be raised to indicate that a resource was not found.
Response is used to return DRF responses, and generics provides class-based views for common patterns.
The LoanApplication model and its serializer are imported for use in the views.

Home View:
The home function is a simple view that returns a welcome message. It uses HttpResponse to send a plain text response.
You might consider using a template for rendering a more complex home page in the future.

LoanApplicationList View:
This class-based view inherits from generics.ListCreateAPIView, which provides functionality to list all loan applications and create a new one.
queryset: This defines the set of loan applications that will be retrieved from the database.
serializer_class: This specifies the serializer that will be used to convert the loan application instances to JSON format.

LoanApplicationDetail View:
This class-based view inherits from generics.RetrieveUpdateDestroyAPIView, which provides functionality to retrieve, update, or delete a loan application based on its primary key (pk).
Similar to the LoanApplicationList view, it defines the queryset and serializer_class.
"""