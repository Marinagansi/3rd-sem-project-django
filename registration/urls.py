from django.contrib import admin
from django.urls import path
from registration import views


urlpatterns = [
  
    path('home',views.home),
     path('guide',views.guide),
      path('event',views.event)
   
]