from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('MyApps.clients.urls')),
    path('employees/', include('MyApps.employees.urls')),
    path('loans/', include('MyApps.loans.urls')),
    path('payments/', include('MyApps.payments.urls')),
    path('requests/', include('MyApps.requests.urls')),
]

