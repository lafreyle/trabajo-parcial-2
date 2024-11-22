# Import necessary modules and classes
from django.shortcuts import render  # Import render function for rendering templates (not used in this example)
from django.http import HttpResponse  # Import HttpResponse for returning simple HTTP responses
from django.http import Http404  # Import Http404 for raising 404 errors

from rest_framework.response import Response  # Import Response for returning API responses
from rest_framework import generics  # Import generic views from Django REST Framework
from rest_framework import status  # Import status for HTTP status codes

from MyApps.employees.models import Employee  # Import the Employee model from the employees app
from MyApps.employees.serializers import EmployeeSerializer  # Import the EmployeeSerializer

# Create your views here.

def home(request):
    """
    Home view that returns a simple welcome message.
    """
    return HttpResponse("Bienvenidos, Uniguajira! - Aplicación Empleados")  # Return a simple HTTP response with a welcome message

class EmployeeList(generics.ListCreateAPIView):
    """
    View to list all employees or create a new employee.
    """
    queryset = Employee.objects.all()  # Queryset to retrieve all Employee records
    serializer_class = EmployeeSerializer  # Specify the serializer class for the Employee model

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete an employee by primary key (pk).
    """
    queryset = Employee.objects.all()  # Queryset to retrieve all Employee records
    serializer_class = EmployeeSerializer  # Specify the serializer class for the Employee model