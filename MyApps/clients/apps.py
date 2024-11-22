from django.apps import AppConfig


class ClientsConfig(AppConfig): # Define a new configuration class for the 'clients' application
    default_auto_field = 'django.db.models.BigAutoField'# Specify the default type of auto-generated primary key fields
    name = 'MyApps.clients'  # Set the name of the application, which is used by Django to identify it
