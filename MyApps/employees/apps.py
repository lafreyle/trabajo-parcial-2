# Import the AppConfig class from Django
from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    """
    Configuration class for the Employees application.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Set the default type for auto-generated primary keys to BigAutoField
    name = 'MyApps.employees'  # Specify the name of the application, which is used by Django to reference this app
