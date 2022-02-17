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
         path('',views.firstpage,name="firstpage"),
          path('faq',views.faq,name='faq'),
           path('flights',views.flights,name="flights"),
            path('user_profile',views.user_profile),
            path('about_us',views.about_us,name="about_us"),
            path('hotel',views.hotel,name="hotel"),
            path('logout',views.logout_view),
             path('userprofile2',views.userprofile2),
            path('partneracc_addproperty',views.partneracc_addproperty),
            path('partneracc_signin',views.partneracc_signin),
            path('partneracc_signin2',views.partneracc_signin2),
            path('partneracc_signup',views.partneracc_signup),
            path('partneracc_signup2',views.partneracc_signup2),
            path('partneracc_signup3',views.partneracc_signup3),
            path('list_nav',views.list_nav),
            path('trip',views.package),
            path('things_to_do',views.things_to_do),
            path('find_guide',views.find_guide,name='find_guide'),
            path('hotelreview',views.hotelreview,name='hotelreview'),
            path('pannel',views.admin_pannel),
 


            path('admin_page',views.admin_page),



            path('explore',views.explore,name="explore"),
            path('admin_page',views.admin_page,name="admin_page"),

            path('explore',views.explore),
            path('admin_page',views.admin_page),
            
            

            path('explore',views.explore,name="explore"),

   
            path('explore',views.explore,name="explore"),
            path('admin_page',views.admin_page,name="admin_page"),

            path('explore',views.explore),

            path('admin_page',views.admin_page),
            


            path('explore',views.explore,name="explore"),


]