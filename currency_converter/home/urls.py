from django.urls import path
from .views import *
urlpatterns=[
    path("",home_,name="homePage"),
    path("currency/",currency,name="Currency"),
]