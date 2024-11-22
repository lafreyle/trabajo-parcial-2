from dataclasses import field
from statistics import mode
from rest_framework import serializers  # Import serializers from Django REST Framework
from MyApps.loans.models import LoanType, Loan, LoanIssued  # Import the LoanType, Loan, and LoanIssued models

"""
Imports:

from rest_framework import serializers: This imports the serializers module from Django REST Framework, which is used to convert complex data types (like model instances) into native Python data types that can then be easily rendered into JSON or other content types.
from MyApps.loans.models import LoanType, Loan, LoanIssued: This imports the LoanType, Loan, and LoanIssued models, which you will serialize.
"""

class LoanTypeSerializer(serializers.ModelSerializer):
    # len_first_nameCliente = serializers.SerializerMethodField()  # Example of a custom field (commented out)
    
    class Meta:
        model = LoanType  # Specify the model to serialize
        fields = "__all__"  # Include all fields in the serialization


class LoanSerializer(serializers.ModelSerializer):
    # len_first_nameCliente = serializers.SerializerMethodField()  # Example of a custom field (commented out)
    
    class Meta:
        model = Loan  # Specify the model to serialize
        fields = "__all__"  # Include all fields in the serialization
"""
LoanSerializer Class:

class LoanSerializer(serializers.ModelSerializer): This defines a serializer class for the Loan model, following the same structure as the LoanTypeSerializer.
The Meta class specifies the Loan model and includes all fields.
"""
class LoanIssuedSerializer(serializers.ModelSerializer):
    # len_first_nameCliente = serializers.SerializerMethodField()  # Example of a custom field (commented out)
    
    class Meta:
        model = LoanIssued  # Specify the model to serialize
        fields = "__all__"  # Include all fields in the serialization
"""
LoanIssuedSerializer Class:

class LoanIssuedSerializer(serializers.ModelSerializer): This defines a serializer class for the LoanIssued model, again following the same structure.
The Meta class specifies the LoanIssued model and includes all fields.
"""