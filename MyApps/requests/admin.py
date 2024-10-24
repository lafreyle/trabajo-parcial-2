from django.contrib import admin
from MyApps.requests.models import LoanApplication

# Register your models here.

# Admin model customization for Application
class LoanApplicationAdmin(admin.ModelAdmin):
    # No additional configuration for the admin interface (using default settings)
    pass

# Register the Application model with default admin settings
admin.site.register(LoanApplication, LoanApplicationAdmin)
