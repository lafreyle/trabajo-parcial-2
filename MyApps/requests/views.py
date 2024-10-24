from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from MyApps.requests.models import LoanApplication
from MyApps.requests.serializers import LoanApplicationSerializer


# Create your views here.


def home(request):
    return HttpResponse("Bienvenidos, Uniguajira!- Aplicación Clientes")

class LoanApplicationList(generics.ListCreateAPIView):
    """
    Lista de solicitudes
    """

    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer



class LoanApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de las solicitudes por pk
    """
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer
