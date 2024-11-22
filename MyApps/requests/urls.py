from django.urls import path  # Import the path function for URL routing
from MyApps.requests.views import home  # Import the home view (commented out)
from MyApps.requests.views import LoanApplicationList, LoanApplicationDetail  # Import the views for loan applications

app_name = "requests"  # Namespace for the app's URLs

urlpatterns = [
    # Uncomment the following line to enable the home view
    # path('inicio/', home, name='home'),  # URL pattern for the home view

    path('', LoanApplicationList.as_view(), name='loan_application_list'),  # URL pattern for listing loan applications
    path('<int:pk>', LoanApplicationDetail.as_view(), name='loan_application_detail'),  # URL pattern for loan application detail view
]

"""
Imports:
from django.urls import path: This imports the path function, which is used to define URL patterns.
The views home, LoanApplicationList, and LoanApplicationDetail are imported from the views module of the requests app.

App Namespace:
app_name = "requests": This sets a namespace for the app's URLs. This is useful when you have multiple apps in your project and want to avoid naming conflicts. You can refer to these URLs in templates or views using the namespace, e.g., {% url 'requests:loan_application_list' %}.

URL Patterns:
urlpatterns: This is a list that contains the URL patterns for the app.
path('', LoanApplicationList.as_view(), name='loan_application_list'): This pattern matches the root URL of the app (e.g., /requests/) and routes it to the LoanApplicationList view. The name argument allows you to refer to this URL pattern in templates and views.
path('<int:pk>', LoanApplicationDetail.as_view(), name='loan_application_detail'): This pattern matches URLs that contain an integer primary key (e.g., /requests/1/) and routes it to the LoanApplicationDetail view. The pk variable will be passed to the view as a keyword argument.
"""