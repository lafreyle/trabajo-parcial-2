from django.contrib import admin
from MyApps.loans.models import Loan, LoanIssued, LoanType

# Register your models here.

# Inline admin class for LoanIssued, allows LoanIssued to be edited within Loan or Employee
class LoanIssuedInline(admin.TabularInline):
    model = LoanIssued  # Specifies the intermediary model
    extra = 1  # Specifies the number of empty forms to display

# Admin customization for Loan, includes LoanIssued as an inline
class LoanAdmin(admin.ModelAdmin):
    inlines = (LoanIssuedInline,)  # Adds the inline form for LoanIssued to Loan

# Admin customization for Employee, includes LoanIssued as an inline
class EmployeeAdmin(admin.ModelAdmin):
    inlines = (LoanIssuedInline,)  # Adds the inline form for LoanIssued to Employee

# Register the Loan model with LoanAdmin customization
admin.site.register(Loan, LoanAdmin)

# Register the LoanType model with default admin settings
admin.site.register(LoanType)
