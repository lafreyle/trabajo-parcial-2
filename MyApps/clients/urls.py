from django.urls import path
from MyApps.clients.views import home
from MyApps.clients.views import ClientList, ClientDetail

app_name = "clients"
urlpatterns = [
    # path('inicio/', home, name= 'home'),
    path('', ClientList.as_view()),
    path('<int:pk>', ClientDetail.as_view()),
]