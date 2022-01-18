from django.contrib import admin
from django.urls import path
from book_event import views


urlpatterns = [
  
    path('event/',views.event),
    
    path('event/event_form',views.form)
     
    
       
   
]