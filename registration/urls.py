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
            path('about_us',views.about_us),
            path('hotel',views.hotel),
            path('logout',views.logout_view),
            path('forget_password',views.forget_password),
            path('forget_username',views.forget_username),
            path('having_trouble',views.having_trouble),
            path('partneracc_addproperty',views.partneracc_addproperty),
            path('partneracc_signin',views.partneracc_signin),
            path('partneracc_signin2',views.partneracc_signin2),
            path('partneracc_signup',views.partneracc_signup),
            path('partneracc_signup2',views.partneracc_signup2),
            path('partneracc_signup3',views.partneracc_signup3)       




          
           
       
   


]