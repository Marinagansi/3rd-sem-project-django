from django.contrib import admin
from django.urls import path
from book_guide import views


urlpatterns = [
  
    path('guide/',views.guide)
    
       
   
]