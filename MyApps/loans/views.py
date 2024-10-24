from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from MyApps.loans.models import LoanType, Loan, LoanIssued
from MyApps.loans.serializers import LoanTypeSerializer, LoanSerializer, LoanIssuedSerializer

# Create your views here.

def home(request):
    return HttpResponse("Bienvenidos, Uniguajira!- Aplicación Empleados")


class LoanTypeList(generics.ListCreateAPIView):
    """
    Lista de prestamos
    """

    queryset = LoanType.objects.all()
    serializer_class = LoanTypeSerializer

class LoanTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los clientes por pk
    """
    queryset = LoanType.objects.all()
    serializer_class = LoanTypeSerializer


class LoanList(generics.ListCreateAPIView):
    """
    Lista de prestamos
    """
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los clientes por pk
    """
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanIssuedList(generics.ListCreateAPIView):
    """
    Lista de prestamos
    """

    queryset = LoanIssued.objects.all()
    serializer_class = LoanIssuedSerializer

class LoanIssuedDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los prestamos por pk
    """
    queryset = LoanIssued.objects.all()
    serializer_class = LoanIssuedSerializer