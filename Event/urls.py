from django.contrib import admin
from django.urls import path
from Event import views


urlpatterns = [
  
    path('event/',views.event),
    path('event/fillform',views.fillform)
]