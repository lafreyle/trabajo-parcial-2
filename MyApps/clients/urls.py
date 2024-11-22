# Import statements
from django.urls import path  # Import the path function to define URL patterns
from MyApps.clients.views import home  # Import the home view function for the homepage
from MyApps.clients.views import ClientList, ClientDetail  # Import class-based views for listing and detailing clients

# Set the application namespace for URL names, allowing for namespacing in reverse URL lookups
app_name = "clients"

# Define the URL patterns for the clients application
urlpatterns = [
    # Define a URL pattern for the home view; currently commented out
    # This would map the URL 'inicio/' to the home view function
    # path('inicio/', home, name='home'),

    # Define a URL pattern for the ClientList view
    # This maps the root URL ('') to the ClientList view, which will display a list of all clients
    path('', ClientList.as_view(), name='client_list'),

    # Define a URL pattern for the ClientDetail view
    # This maps URLs in the format '<int:pk>/' to the ClientDetail view
    # The '<int:pk>' part captures an integer from the URL, which represents the primary key of a specific client
    path('<int:pk>', ClientDetail.as_view(), name='client_detail'),
]