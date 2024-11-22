from django.contrib import admin
from MyApps.payments.models import Payment

# Register your models here.

# Admin model customization for Payment
class PaymentAdmin(admin.ModelAdmin):
    # No additional configuration for the admin interface (using default settings)
    pass

# Register the Payment model with default admin settings
admin.site.register(Payment, PaymentAdmin)

"""
While you are currently using the default settings, you can customize the PaymentAdmin class to add features such as:
List Display: Specify which fields to display in the list view.
Search Fields: Enable searching by specific fields.
Filters: Add filters to the sidebar for easier navigation.
Fieldsets: Organize fields into sections in the detail view.

example:

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'payment_date', 'status')  # Display these fields in the list view
    search_fields = ('id', 'status')  # Enable search by ID and status
    list_filter = ('status',)  # Add a filter for status
"""