from dataclasses import field
from statistics import mode

# Import necessary modules and classes
from rest_framework import serializers  # Import serializers module from Django REST Framework
from MyApps.employees.models import Employee  # Import the Employee model from the employees app

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee model.
    """
    # Uncomment the line below to define a custom field for the length of the first name
    # len_first_nameCliente = serializers.SerializerMethodField()

    class Meta:
        model = Employee  # Specify the model to be serialized
        fields = "__all__"  # Include all fields from the Employee model in the serialization process
       