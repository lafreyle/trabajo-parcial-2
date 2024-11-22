# Import necessary modules
from django.urls import path  # Import the path function for defining URL patterns
from MyApps.employees.views import home  # Import the home view (currently commented out)
from MyApps.employees.views import EmployeeList, EmployeeDetail  # Import class-based views for employee listing and detail

# Define the app namespace
app_name = "employees"  # This sets the namespace for the app, allowing for reverse URL resolution

# Define the URL patterns for the employees app
urlpatterns = [
    # Uncomment the line below to enable the home view
    # path('inicio/', home, name='home'),  # URL pattern for the home view, accessible at '/inicio/'

    path('', EmployeeList.as_view(), name='employee_list'),  # URL pattern for listing employees, accessible at '/'
    path('<int:pk>', EmployeeDetail.as_view(), name='employee_detail'),  # URL pattern for employee detail, accessible at '/<employee_id>/'
]
