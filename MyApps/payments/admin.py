from django.contrib import admin
from MyApps.payments.models import Payment

# Register your models here.

# Admin model customization for Payment
class PaymentAdmin(admin.ModelAdmin):
    # No additional configuration for the admin interface (using default settings)
    pass

# Register the Payment model with default admin settings
admin.site.register(Payment, PaymentAdmin)
