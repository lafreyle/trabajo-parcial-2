from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyApps.payments'

"""
Imports:
from django.apps import AppConfig: This imports the AppConfig class, which is used to configure the application.

PaymentsConfig Class:
class PaymentsConfig(AppConfig): This defines a configuration class for the payments app. By inheriting from AppConfig, you can customize various aspects of the app's behavior.
"""
