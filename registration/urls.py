from django.contrib import admin
from django.urls import path
from registration import views



urlpatterns = [
  
    path('home',views.home,name="home"),
      path('boy_shop',views.shop1,name="shop"),
       path('girl_shop',views.shop2),
        path('try',views.try2),
         path('signup',views.registration),
         path('login',views.signin),
         path('firstpage',views.firstpage),
          path('faq',views.faq),
           path('flights',views.flights,name="flights"),
            path('user_profile',views.user_profile),
            path('contact',views.contact),
            path('about_us',views.about_us),
            path('hotel',views.hotel),
            
          
           
       
   
]