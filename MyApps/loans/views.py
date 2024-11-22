from django.shortcuts import render  # Import render for rendering templates (not used in this code)
from django.http import HttpResponse, Http404  # Import HttpResponse for returning simple responses and Http404 for raising 404 errors

from rest_framework.response import Response  # Import Response for returning DRF responses
from rest_framework import generics  # Import generics for class-based views

from MyApps.loans.models import LoanType, Loan, LoanIssued  # Import the models
from MyApps.loans.serializers import LoanTypeSerializer, LoanSerializer, LoanIssuedSerializer  # Import the serializers

# Create your views here.

def home(request):
    return HttpResponse("Bienvenidos, Uniguajira!- Aplicación Empleados")  # Simple welcome message

class LoanTypeList(generics.ListCreateAPIView):

    queryset = LoanType.objects.all()  # Queryset for listing all LoanType objects
    serializer_class = LoanTypeSerializer  # Serializer for LoanType

class LoanTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los clientes por pk
    """
    queryset = LoanType.objects.all()  # Queryset for retrieving, updating, or deleting LoanType objects
    serializer_class = LoanTypeSerializer  # Serializer for LoanType

class LoanList(generics.ListCreateAPIView):
  
    queryset = Loan.objects.all()  # Queryset for listing all Loan objects
    serializer_class = LoanSerializer  # Serializer for Loan

class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los clientes por pk
    """
    queryset = Loan.objects.all()  # Queryset for retrieving, updating, or deleting Loan objects
    serializer_class = LoanSerializer  # Serializer for Loan

class LoanIssuedList(generics.ListCreateAPIView):
    
    queryset = LoanIssued.objects.all()  # Queryset for listing all LoanIssued objects
    serializer_class = LoanIssuedSerializer  # Serializer for LoanIssued

class LoanIssuedDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los prestamos por pk
    """
    queryset = LoanIssued.objects.all()  # Queryset for retrieving, updating, or deleting LoanIssued objects
    serializer_class = LoanIssuedSerializer  # Serializer for LoanIssued