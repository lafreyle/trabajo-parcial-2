# Import necessary modules and classes
from django.contrib import admin  # Import the admin module to customize the Django admin interface
from MyApps.loans.models import Loan, LoanIssued, LoanType  # Import the Loan, LoanIssued, and LoanType models

# Register your models here.

# Inline admin class for LoanIssued, allows LoanIssued to be edited within Loan or Employee
class LoanIssuedInline(admin.TabularInline):
    model = LoanIssued  # Specifies the intermediary model that will be displayed inline
    extra = 1  # Specifies the number of empty forms to display for creating new LoanIssued instances

# Admin customization for Loan, includes LoanIssued as an inline
class LoanAdmin(admin.ModelAdmin):
    inlines = (LoanIssuedInline,)  # Adds the inline form for LoanIssued to the Loan admin interface

# Admin customization for Employee, includes LoanIssued as an inline
class EmployeeAdmin(admin.ModelAdmin):
    inlines = (LoanIssuedInline,)  # Adds the inline form for LoanIssued to the Employee admin interface

# Register the Loan model with LoanAdmin customization
admin.site.register(Loan, LoanAdmin)

# Register the LoanType model with default admin settings
admin.site.register(LoanType)