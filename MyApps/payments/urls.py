from django.urls import path  # Import the path function to define URL patterns
from MyApps.payments.views import home  # Import the home view (commented out)
from MyApps.payments.views import PaymentList, PaymentDetail  # Import the PaymentList and PaymentDetail views

"""
Imports:

from django.urls import path: This imports the path function, which is used to define URL patterns in Django.
from MyApps.payments.views import home: This imports the home view from your views.py file in the payments app. This line is currently commented out, indicating that it may not be in use.
from MyApps.payments.views import PaymentList, PaymentDetail: This imports the PaymentList and PaymentDetail views, which are likely class-based views for listing and detailing payments, respectively.

"""

app_name = "payments"  # Define the application namespace for URL reversing
urlpatterns = [
    # path('inicio/', home, name='home'),  # Example of a URL pattern for the home view (commented out)
    path('', PaymentList.as_view(), name='payment-list'),  # URL pattern for listing payments
    path('<int:pk>', PaymentDetail.as_view(), name='payment-detail'),  # URL pattern for viewing a specific payment by primary key
]

"""
App Namespace:

app_name = "payments": This defines a namespace for the URLs in this app. It allows you to use the app_name when reversing URLs, which helps avoid naming conflicts with URLs in other apps.
URL Patterns:

urlpatterns: This is a list that contains the URL patterns for the app.
path('', PaymentList.as_view(), name='payment-list'): This pattern matches the root URL of the payments app and routes it to the PaymentList view. The name='payment-list' argument allows you to refer to this URL pattern in templates and views using the payments:payment-list syntax.
path('<int:pk>/', PaymentDetail.as_view(), name='payment-detail'): This pattern matches URLs that contain an integer primary key (pk) and routes them to the PaymentDetail view. The name='payment-detail' argument allows you to refer to this URL pattern in a similar way.
"""