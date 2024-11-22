# Import the models module from Django
from django.db import models

# Create your models here.

class Employee(models.Model):
    """
    Model representing an employee in the system.
    """
    first_name = models.CharField(max_length=100, help_text="Enter the Employee's First Name")  # Employee's first name, limited to 100 characters
    last_name = models.CharField(max_length=100, help_text="Enter the Employee's Last Name")  # Employee's last name, limited to 100 characters
    position = models.CharField(max_length=100, help_text="Enter the Employee's Job Position")  # Employee's job position, limited to 100 characters
    
    # String representation of the Employee object
    def __str__(self): 
        return f'{self.first_name} {self.last_name}'  # Return a string representation of the employee's full name
    
    # Meta class for additional model settings
    class Meta:
        verbose_name = "employee"  # Singular form for the model name in the admin interface
        verbose_name_plural = "employees"  # Plural form for the model name in the admin interface