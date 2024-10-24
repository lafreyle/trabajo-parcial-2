from django.urls import path
from MyApps.loans.views import home
from MyApps.loans.views import LoanTypeList, LoanTypeDetail, LoanList, LoanDetail, LoanIssuedList, LoanIssuedDetail

app_name = "loans"
urlpatterns = [
    # path('inicio/', home, name= 'home'),
    path('loantype/', LoanTypeList.as_view()),
    path('loantype/<int:pk>', LoanTypeDetail.as_view()),
    path('loan/', LoanList.as_view()),
    path('loan/<int:pk>', LoanDetail.as_view()),
    path('loanis/', LoanIssuedList.as_view()),
    path('loanis/<int:pk>', LoanIssuedDetail.as_view()),

]
