from django.db import models # This imports the necessary classes to define your database models.
from django.utils.timezone import now # This imports the now function to set the default value for the payment_date field to the current date.
from MyApps.clients.models import Client # This imports the Client model, which is referenced in the Payment model.
from MyApps.loans.models import Loan # This imports the Loan model, which is also referenced in the Payment model.

# Create your models here.

# Model for Payment
class Payment(models.Model):
    # Payment status choices
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    ]

    payment_date = models.DateField(default=now, verbose_name="Current Date")  # Payment date, defaults to the current date
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Payment amount with maximum 10 digits and 2 decimal places
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # Payment status with choices
    loan = models.ForeignKey(Loan,   # Foreign key to Loan, can be null or blank
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    client = models.ForeignKey(Client,  # Foreign key to Client, can be null or blank
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)
    
    # String representation of the Payment object
    def __str__(self):
        return f"Payment {self.id} - {self.client.first_name}"
    """
    The __str__ method provides a string representation of the Payment object, which is useful for debugging and in the Django admin interface. It returns a string that includes the payment ID and the first name of the associated client.
    """

    # Meta class for additional model settings
    class Meta:
        verbose_name = 'Payment'  # Singular form
        verbose_name_plural = 'Payments'  # Plural form


