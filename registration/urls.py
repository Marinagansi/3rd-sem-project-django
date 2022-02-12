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
         path('firstpage',views.firstpage,name="firstpage"),
          path('faq',views.faq),
           path('flights',views.flights,name="flights"),
            path('user_profile',views.user_profile),
            path('about_us',views.about_us,name="about_us"),
            path('hotel',views.hotel),
            path('logout',views.logout_view),
             path('userprofile2',views.userprofile2),

            path('forget_password',views.forget_password),
            path('forget_username',views.forget_username),
            path('having_trouble',views.having_trouble),
            path('partneracc_addproperty',views.partneracc_addproperty),
            path('partneracc_signin',views.partneracc_signin),
            path('partneracc_signin2',views.partneracc_signin2),
            path('partneracc_signup',views.partneracc_signup),
            path('partneracc_signup2',views.partneracc_signup2),
            path('partneracc_signup3',views.partneracc_signup3),
            path('list_nav',views.list_nav),
            path('trip',views.package),
            path('things_to_do',views.things_to_do),
            path('find_guide',views.find_guide),
            path('hotelreview',views.hotelreview),
            path('pannel',views.admin_pannel),
            path('explore',views.explore),
<<<<<<< HEAD
            path('admin_page',views.admin_page)
            
=======
            
            path('explore',views.explore,name="explore"),
<<<<<<< HEAD
            path('admin_page',views.admin_page)
  
=======
            path('admin_page',views.admin_page),
           
>>>>>>> a13402b7a9a88c0abfae2bd16c5ee8effd075b83
          
            




            

          
           
       
   

>>>>>>> 2a57676da1b5617d8aa03e33e230ba522a87bde3

>>>>>>> 74784d6c5df8bf8f74cbb3176f12ef21744fa27b
]