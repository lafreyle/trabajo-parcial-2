from django.contrib import admin
from MyApps.requests.models import LoanApplication

# Register your models here.

# Admin model customization for Application
class LoanApplicationAdmin(admin.ModelAdmin):
    # No additional configuration for the admin interface (using default settings)
    pass

# Register the Application model with default admin settings
admin.site.register(LoanApplication, LoanApplicationAdmin)

"""
Imports:
from django.contrib import admin: This imports the Django admin module, which is used to create an admin interface for your models.
from MyApps.requests.models import LoanApplication: This imports the LoanApplication model that you want to manage through the admin interface.

Admin Model Customization:
class LoanApplicationAdmin(admin.ModelAdmin): This defines a custom admin class for the LoanApplication model. By inheriting from admin.ModelAdmin, you can customize how the model is displayed and managed in the admin interface.
The pass statement indicates that no additional customization is currently applied. You can add configurations later if needed.

Registering the Model:
admin.site.register(LoanApplication, LoanApplicationAdmin): This line registers the LoanApplication model with the Django admin site, using the LoanApplicationAdmin class for customization. This allows you to manage LoanApplication instances through the Django admin interface.
"""