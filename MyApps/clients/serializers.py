from dataclasses import field
from statistics import mode

# Import statements
from MyApps.clients.models import Client  # Import the Client model from the clients application
from rest_framework import serializers      # Import the serializers module from Django REST framework

# Serializer class definition
class ClientSerializer(serializers.ModelSerializer):
    # Uncomment the following line to add a custom field for the length of the first name
    # len_first_nameCliente = serializers.SerializerMethodField()
    
    class Meta:
        # Specify the model that this serializer is associated with
        model = Client
        
        # Include all fields from the model in the serialized output
        fields = "__all__"
        
        # Uncomment the following line to exclude the passwordCliente field from the serialized output
        # exclude = ['passwordCliente']
        
        # Alternatively, you can specify the fields to include explicitly
        # fields = (
        #     'pk',
        #     'nombreCliente',
        #     'direccionCliente',
        #     'telefonoCliente',
        #     'correoCliente',
        #     'passwordCliente',
        # )

    # Custom field methods (uncomment if needed)
    # def get_len_nombreCliente(self, object):
    #     length = len(object.nombreCliente)
    #     return length

    # Custom validation methods (uncomment if needed)
    # def validate(self, data):
    #     # Ensure that nombreCliente and direccionCliente are not the same
    #     if data['nombreCliente'] == data['direccionCliente']:
    #         raise serializers.ValidationError('Nombre y Correo No pueden ser iguales')
    #     else:
    #         return data

    # Custom validation method for the first_nameClient field
    def validate_first_nameClient(self, value):
        # Check if the length of the value is less than 3 characters
        if len(value) < 3:
            # Raise a validation error if the condition is met
            raise serializers.ValidationError('Nombre no puede ser tan corto')
        else:
            # Return the validated value if it passes the check
            return value
