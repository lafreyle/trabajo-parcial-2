from django.urls import path
from MyApps.requests.views import home
from MyApps.requests.views import LoanApplicationList, LoanApplicationDetail

app_name = "requests"
urlpatterns = [
    # path('inicio/', home, name= 'home'),
    path('', LoanApplicationList.as_view()),
    path('<int:pk>', LoanApplicationDetail.as_view()),
]