from django.db import models
from django.utils.timezone import now
from MyApps.clients.models import Client
from MyApps.employees.models import Employee
from MyApps.loans.models import LoanType

# Create your models here.

# Model for Loan Application (Solicitud)
class LoanApplication(models.Model):
    # Application status choices
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    application_date = models.DateField(default=now, verbose_name="Current Date") # Application date, defaults to the current date 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending') # Application status with choices
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
