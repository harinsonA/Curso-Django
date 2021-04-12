from django.contrib import admin
from django.urls import path

def Prueba(self):
    print("================Aqui=================")
urlpatterns = [
    path('personal/', Prueba),
]
