from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MyApps.loans.models import LoanType, Loan, LoanIssued

class LoanTypeSerializer(serializers.ModelSerializer):
    # len_first_nameCliente = serializers.SerializerMethodField()
    class Meta:
        model = LoanType
        fields = "__all__"
        # exclude = ['passwordCliente']
        # fields = (
        #     'pk',
        #     'nombreCliente',
        #     'direccionCliente',
        #     'telefonoCliente',
        #     'correoCliente',
        #     'passwordCliente',
        # )
    
class LoanSerializer(serializers.ModelSerializer):
    # len_first_nameCliente = serializers.SerializerMethodField()
    class Meta:
        model = Loan
        fields = "__all__"
        # exclude = ['passwordCliente']
        # fields = (
        #     'pk',
        #     'nombreCliente',
        #     'direccionCliente',
        #     'telefonoCliente',
        #     'correoCliente',
        #     'passwordCliente',
        # )

class LoanIssuedSerializer(serializers.ModelSerializer):
    # len_first_nameCliente = serializers.SerializerMethodField()
    class Meta:
        model = LoanIssued
        fields = "__all__"
        # exclude = ['passwordCliente']
        # fields = (
        #     'pk',
        #     'nombreCliente',
        #     'direccionCliente',
        #     'telefonoCliente',
        #     'correoCliente',
        #     'passwordCliente',
        # )

    # def get_len_nombreCliente(self, object):
    #     length = len(object.nombreCliente)
    #     return length

    # def validate(self, data):
    #     if data['nombreCliente'] == data['direccionCliente']:
    #         raise serializers.ValidationError('Nombre y Correo No pueden ser iguales')
    #     else:
    #         return data

    #def validate_first_nameClient(self, value):
    #   if len(value) < 3:
    #       raise serializers.ValidationError('Nombre no puede ser tan corto')
    #   else:
    #       return value
