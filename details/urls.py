from django.urls import path
from . import  views

urlpatterns=[
    path('register.html',views.register,name="details"),
    # path for register page
]