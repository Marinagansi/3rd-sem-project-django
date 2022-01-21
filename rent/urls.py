from django.contrib import admin
from django.urls import path
from rent import views



urlpatterns = [
  
    path('rent',views.create,name="rent"),
    
    path('vehicle',views.vehicle,name="vehicle"),
    path('vehicle_detail/<int:p_id>', views.V_details),

]