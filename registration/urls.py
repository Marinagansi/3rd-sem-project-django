from django.contrib import admin
from django.urls import path
from registration import views



urlpatterns = [
  
    path('home',views.home,name="home"),
      path('boy_shop',views.shop1),
       path('girl_shop',views.shop2),
        path('try',views.try2),
         path('signup',views.registration),
         path('login',views.signin),
         path('firstpage',views.firstpage)
       
   
]