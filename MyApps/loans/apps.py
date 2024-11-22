from django.apps import AppConfig  # Import AppConfig to create a configuration class for the app

class LoansConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Set the default type for auto-generated primary keys
    name = 'MyApps.loans'  # Specify the name of the app