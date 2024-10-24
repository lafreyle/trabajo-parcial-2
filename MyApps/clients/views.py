from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from MyApps.clients.models import Client
from MyApps.clients.serializers import ClientSerializer


# Create your views here.


def home(request):
    return HttpResponse("Bienvenidos, Uniguajira!- Aplicación Clientes")

class ClientList(generics.ListCreateAPIView):
    """
    Lista de Clientes
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer



class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los clientes por pk
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer