from django.contrib import admin
from MyApps.employees.models import Employee

# Register your models here.

# Admin model customization for Employee
class EmployeeAdmin(admin.ModelAdmin):
    # No additional configuration for the admin interface (using default settings)
    pass

# Register the Employee model with the default admin settings
admin.site.register(Employee)
