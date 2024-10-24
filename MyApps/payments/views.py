from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from MyApps.payments.models import Payment
from MyApps.payments.serializers import PaymentSerializer


# Create your views here.


def home(request):
    return HttpResponse("Bienvenidos, Uniguajira!- Aplicación Clientes")

class PaymentList(generics.ListCreateAPIView):
    """
    Lista de Pagos
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer



class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los pagos por pk
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer