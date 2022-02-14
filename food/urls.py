from django.contrib import admin
from django.urls import path
from food import views


urlpatterns = [
  
   path('food',views.food),
   path('food_form',views.food_form),
   path('searched_food',views.search_food)
     
   
]