from django.urls import path
from MyApps.payments.views import home
from MyApps.payments.views import PaymentList, PaymentDetail

app_name = "payments"
urlpatterns = [
    # path('inicio/', home, name= 'home'),
    path('', PaymentList.as_view()),
    path('<int:pk>', PaymentDetail.as_view()),
]
