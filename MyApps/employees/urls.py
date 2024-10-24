from django.urls import path
from MyApps.employees.views import home
from MyApps.employees.views import EmployeeList, EmployeeDetail

app_name = "employees"
urlpatterns = [
    # path('inicio/', home, name= 'home'),
    path('', EmployeeList.as_view()),
    path('<int:pk>', EmployeeDetail.as_view()),

]
