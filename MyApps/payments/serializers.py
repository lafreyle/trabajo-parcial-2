from dataclasses import field
from statistics import mode
from rest_framework import serializers  # Import serializers from Django REST Framework
from MyApps.payments.models import Payment  # Import the Payment model

"""
The above imports are essential for creating a serializer for the Payment model.
- from rest_framework import serializers: This imports the serializers module from Django REST Framework, which is used to convert complex data types (like model instances) into native Python data types that can then be easily rendered into JSON or other content types.
- from MyApps.payments.models import Payment: This imports the Payment model, which you will serialize.
"""

class PaymentSerializer(serializers.ModelSerializer):
    # len_first_nameCliente = serializers.SerializerMethodField()  # Example of a custom field (commented out)
    
    """
    The PaymentSerializer class is defined here, inheriting from serializers.ModelSerializer.
    This provides a convenient way to create serializers for Django models.
    """

    class Meta:
        model = Payment  # Specify the model to serialize
        fields = "__all__"  # Include all fields in the serialization

"""
Meta Class:

The Meta class is an inner class that provides configuration options for the serializer.
model = Payment: This specifies which model the serializer is associated with, in this case, the Payment model.
fields = "__all__": This indicates that all fields from the Payment model should be included in the serialized output. You can also specify a list of fields explicitly or use exclude to omit specific fields.
"""