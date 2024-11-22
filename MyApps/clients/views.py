# Import statements
from django.shortcuts import render  # Import render for rendering templates (not used in this code)
from django.http import HttpResponse  # Import HttpResponse to return simple HTTP responses
from django.http import Http404  # Import Http404 to raise a 404 error if a resource is not found

from rest_framework.response import Response  # Import Response for returning API responses
from rest_framework import generics  # Import generics for class-based views in Django REST framework
from rest_framework import status  # Import status for HTTP status codes

from MyApps.clients.models import Client  # Import the Client model from the clients application
from MyApps.clients.serializers import ClientSerializer  # Import the ClientSerializer for serializing Client objects


# Create your views here.

def home(request):
    """
    Home view that returns a welcome message.
    """
    return HttpResponse("Bienvenidos, Uniguajira! - Aplicación Clientes")  # Return a simple HTTP response with a welcome message

class ClientList(generics.ListCreateAPIView):
    """
    View to list all clients and create a new client.
    """
    queryset = Client.objects.all()  # Define the queryset to retrieve all clients from the database
    serializer_class = ClientSerializer  # Specify the serializer class to use for serializing client data


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a client by its primary key (pk).
    """
    queryset = Client.objects.all()  # Define the queryset to retrieve all clients from the database
    serializer_class = ClientSerializer  # Specify the serializer class to use for serializing client data