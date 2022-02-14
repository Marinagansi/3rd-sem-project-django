from django.contrib import admin
from django.urls import path
from Event import views


urlpatterns = [
  
    path('event/',views.event, name="event"),
    path('event/fillform',views.fillform),
     path('recipt',views.receipt, name='booked_event')
]