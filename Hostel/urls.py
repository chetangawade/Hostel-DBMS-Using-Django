from django.contrib import admin
from django.urls import path ,include
from Hostel import views

urlpatterns = [
    path('', views.index,name="index"),
    path('hostel', views.hostel,name="hostel"),
    path('admi_form', views.admi_form,name="admi_form"),
    path('mess', views.mess,name="mess")
]
