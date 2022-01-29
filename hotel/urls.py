from django.contrib import admin
from django.urls import path
from hotel import views


urlpatterns = [
  
    path('add_hotel', views.hotel_form),
    path('hotel2/<str:hotel_name>', views.update_hotel),
    
   
]