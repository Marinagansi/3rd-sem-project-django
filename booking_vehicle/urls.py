from django.contrib import admin
from django.urls import path
from booking_vehicle import views


urlpatterns = [
  
    path('vbook/<int:p_id>',views.booking),
    path('fillform/<int:p_id>',views.fillform),
    path('vehicle_rent',views.book_vehicle),
    path('edit/<int:p_id>',views.edit),
    path('update/<int:p_id>',views.update),

    
       
   
]