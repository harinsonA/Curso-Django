from django.contrib import admin
from django.urls import path

def Prueba(self):
    print("=======Hola=======")

urlpatterns = [
    path('departamento/', Prueba),
]
