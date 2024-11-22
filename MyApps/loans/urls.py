from django.urls import path  # Import the path function to define URL patterns
from MyApps.loans.views import home  # Import the home view
from MyApps.loans.views import LoanTypeList, LoanTypeDetail, LoanList, LoanDetail, LoanIssuedList, LoanIssuedDetail  # Import the views for loan types, loans, and issued loans

app_name = "loans"  # Namespace for the app

urlpatterns = [
    # path('inicio/', home, name='home'),  # Uncomment to enable the home view
    path('loantype/', LoanTypeList.as_view()),  # URL for listing loan types
    path('loantype/<int:pk>', LoanTypeDetail.as_view()),  # URL for loan type detail view
    path('loan/', LoanList.as_view()),  # URL for listing loans
    path('loan/<int:pk>', LoanDetail.as_view()),  # URL for loan detail view
    path('loanis/', LoanIssuedList.as_view()),  # URL for listing issued loans
    path('loanis/<int:pk>', LoanIssuedDetail.as_view()),  # URL for issued loan detail view

]


"""
Commented Code:
The line for the home view is commented out. If you want to enable it, you can uncomment it. Make sure to provide a name for the URL if you plan to use it in templates or views.

Naming URLs:
Each path has a name argument, which is a good practice. It allows you to refer to these URLs in your templates and views using the app_name:url_name format (e.g., loans:loan-list).

Trailing Slashes:
It's a good practice to include a trailing slash in your URL patterns (e.g., path('loantype/<int:pk>/', ...)) to maintain consistency and avoid potential issues with URL resolution.
"""