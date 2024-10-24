from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from MyApps.employees.models import Employee
from MyApps.employees.serializers import EmployeeSerializer

# Create your views here.

def home(request):
    return HttpResponse("Bienvenidos, Uniguajira!- Aplicación Empleados")


class EmployeeList(generics.ListCreateAPIView):
    """
    Lista de empleados
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los clientes por pk
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer