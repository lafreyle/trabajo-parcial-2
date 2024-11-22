from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MyApps.requests.models import LoanApplication

class LoanApplicationSerializer(serializers.ModelSerializer):
    # len_first_nameCliente = serializers.SerializerMethodField()
    class Meta:
        model = LoanApplication
        fields = "__all__"

"""
Imports:
from rest_framework import serializers: This imports the serializers module from Django REST Framework, which is used to convert complex data types (like model instances) into native Python data types that can then be easily rendered into JSON or other content types.
from MyApps.requests.models import LoanApplication: This imports the LoanApplication model, which the serializer will be based on.

LoanApplicationSerializer Class:
class LoanApplicationSerializer(serializers.ModelSerializer): This defines a serializer class for the LoanApplication model. By inheriting from serializers.ModelSerializer, you get a lot of functionality out of the box, such as automatic field generation and validation.

Meta Class:
The Meta class is used to configure the serializer.
model = LoanApplication: This specifies the model that the serializer is associated with.
fields = "__all__": This indicates that all fields from the LoanApplication model should be included in the serialized output. You can also specify a list of fields if you want to include only specific fields, e.g., fields = ['id', 'application_date', 'status'].
"""