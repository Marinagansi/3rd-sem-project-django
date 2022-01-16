from django.contrib import admin
from django.urls import path
from registration import views


urlpatterns = [
  
    path('home',views.home),
     path('guide',views.guide),
      path('event',views.event),
      path('boy_shop',views.shop1),
       path('girl_shop',views.shop2)
   
]