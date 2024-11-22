from django.db import models  # Import the models module from Django
from django.utils.timezone import now  # Import the now function to get the current date
from MyApps.clients.models import Client  # Import the Client model
from MyApps.employees.models import Employee  # Import the Employee model
from MyApps.loans.models import LoanType  # Import the LoanType model

# Create your models here.

# Model for Loan Application (Solicitud)
class LoanApplication(models.Model):
    # Application status choices
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    application_date = models.DateField(default=now, verbose_name="Current Date")  # Application date, defaults to the current date 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # Application status with choices
    client = models.ForeignKey(Client,  # Foreign key to Client, can be null or blank
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)
    
    # Foreign key to Employee, can be null or blank
    employee = models.ForeignKey(Employee,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)
    
    # Foreign key to LoanType, can be null or blank
    loan_type = models.ForeignKey(LoanType,
                                  null=True,
                                  blank=True,
                                  on_delete=models.CASCADE)

    # String representation of the Loan Application object
    def __str__(self):
        return f"Application {self.id} - {self.client.first_name}"

    # Meta class for additional model settings
    class Meta:
        verbose_name = 'Loan Application'  # Singular form
        verbose_name_plural = 'Loan Applications'  # Plural form

"""
Imports:

The imports at the top of the file include necessary modules from Django and your other app models.
models is imported to define the model fields and behaviors.
now is imported to set the default value for the application_date field to the current date.
The Client, Employee, and LoanType models are imported to create foreign key relationships.

LoanApplication Model:
class LoanApplication(models.Model): This defines the LoanApplication model, which inherits from models.Model.

Fields:
STATUS_CHOICES: This is a list of tuples that define the possible choices for the status field.
application_date: A DateField that defaults to the current date using now. The verbose_name argument provides a human-readable name for the field.
status: A CharField that uses the STATUS_CHOICES for its choices and defaults to 'pending'.
client: A foreign key to the Client model. It can be null or blank, and if the associated Client is deleted, the LoanApplication will also be deleted (on_delete=models.CASCADE).
employee: A foreign key to the Employee model, with similar behavior as the client field.
loan_type: A foreign key to the LoanType model, also allowing null or blank values.

String Representation:
The __str__ method returns a string representation of the LoanApplication object, which includes the application ID and the first name of the associated client. This is useful for debugging and in the Django admin interface.

Meta Class:
The Meta class allows you to define additional options for the model. Here, verbose_name and verbose_name_plural are set to provide human-readable names for the model in the admin interface.
"""