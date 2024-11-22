from django.apps import AppConfig  # Import AppConfig from Django

class RequestsConfig(AppConfig):
    """
    Configuration class for the Requests app.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Specify the default type for auto-generated fields
    name = 'MyApps.requests'  # Specify the name of the application

    """
Imports:
from django.apps import AppConfig: This imports the AppConfig class, which is used to configure an application in Django.
RequestsConfig Class:
class RequestsConfig(AppConfig): This defines a configuration class for the requests app. By inheriting from AppConfig, you can customize the behavior of the app.

Attributes:
default_auto_field = 'django.db.models.BigAutoField': This attribute specifies the default type for auto-generated fields in models. BigAutoField is a 64-bit integer that can be used for primary keys. This is particularly useful for applications that may have a large number of records.
name = 'MyApps.requests': This attribute specifies the full Python path to the application. It is used by Django to identify the app and is important for various functionalities, such as migrations and app loading.
    """