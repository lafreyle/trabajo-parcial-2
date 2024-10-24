from django.db import models
from django.utils.timezone import now
from MyApps.clients.models import Client
from MyApps.employees.models import Employee

# Create your models here.

# Model for Loan Type
class LoanType(models.Model):
    
    name = models.CharField(max_length=50, verbose_name="Name") # Loan type name, limited to 50 characters
    
    # String representation of the Loan Type object
    def __str__(self):
        return self.name

    # Meta class for additional model settings
    class Meta:
        verbose_name = "loan type"  # Singular form
        verbose_name_plural = "loan types"  # Plural form


# Model for Loan
class Loan(models.Model):
    # Loan status choices
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    ]
    
    # Loan amount with maximum 10 digits and 2 decimal places
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2) # Interest rate with maximum 5 digits and 2 decimal places   
    disbursement_date = models.DateField(default=now, verbose_name="Current Date") # Disbursement date, defaults to the current date
    due_date = models.DateTimeField(auto_now=True, verbose_name="Due Date")  # Due date, automatically set to the current time
    employee = models.ManyToManyField(Employee, through='LoanIssued', verbose_name="LoanIssued")  # Many-to-Many relationship with Employee through LoanIssued
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # Loan status with choices
    loan_type = models.ForeignKey(LoanType,  # Foreign key to LoanType, can be null or blank
                                  null=True,
                                  blank=True,
                                  on_delete=models.CASCADE)
    
    # Foreign key to Client, can be null or blank
    client = models.ForeignKey(Client,
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)

    # String representation of the Loan object
    def __str__(self):
        return f"Loan {self.id} - {self.client.first_name}"

    # Meta class for additional model settings
    class Meta:
        verbose_name = "Loan"  # Singular form
        verbose_name_plural = "Loans"  # Plural form

# Model for Loan Issued (intermediary table)
class LoanIssued(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, verbose_name="Loan")  # Foreign key to Loan
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Employee")  # Foreign key to Employee
    loan_date = models.DateField(default=now, verbose_name="Current Date") # Date when the loan was issued, defaults to the current date

    # Meta class for additional model settings
    class Meta:
        verbose_name = "Loan Issued"  # Singular form
        verbose_name_plural = "Loans Issued"  # Plural form
