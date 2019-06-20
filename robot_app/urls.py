from django.urls import path,include
from . import views

urlpaterns=[
    path('',views.home)
]