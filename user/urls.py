from django.urls import path 
from .views import profile, password_change

urlpatterns = [
    #Perfil
    path('', profile, name="profile"),
    path('change/', password_change, name="change"),
]