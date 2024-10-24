from django.contrib import admin
from MyApps.clients.models import Client

# Register your models here.

# Admin model customization for Client
class ClientAdmin(admin.ModelAdmin):
    # Uncomment to make the 'email' field read-only
    # readonly_fields = ('email',)  # Prevents editing during create and update actions
    
    # Uncomment to make the 'created' and 'updated' fields read-only
    # readonly_fields = ('created', 'updated')  # Prevents editing during create and update actions
    
    list_display = ('first_name', 'address', 'phone', 'email') # Fields to display in the admin list view
    
    # Default ordering of the displayed fields, can specify one or more fields
    ordering = ('first_name', 'address', 'email')  # If only one field: ordering('field',)
    
    # Searchable fields in the admin interface
    search_fields = ('first_name', 'email')  # Fields to include in the search functionality
    
    # Filters in the admin interface, allowing filtering by related fields
    list_filter = ('first_name', 'email', 'address')  # Fields to filter the list

# Register the Client model and its customization
admin.site.register(Client, ClientAdmin)
