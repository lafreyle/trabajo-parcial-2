from django.db import models

# Create your models here.

class Client(models.Model): # Model representing a client
    first_name = models.CharField(max_length=100, help_text="Enter the Client's First Name") # First name of the client, limited to 100 characters
    last_name = models.CharField(max_length=100, help_text="Enter the Client's Last Name") # Last name of the client, limited to 100 characters
    address = models.CharField(max_length=100, help_text="Enter the Client's Address") # Address of the client, limited to 100 characters
    phone = models.CharField(max_length=12, help_text="Enter the Client's Phone Number") # Phone number of the client, limited to 12 characters
    email = models.EmailField(max_length=100, help_text="Enter the Client's Email")  # Email address of the client, using Django's built-in EmailField, limited to 100 characters
    
    def __str__(self):  # String representation of the Client object
        return f'{self.first_name} {self.last_name}'  # Display the full name of the client
    
    class Meta: # Meta class for additional model settings 
        verbose_name = "client"  # Custom singular name for the model
        verbose_name_plural = "clients"  # Custom plural name for the model
