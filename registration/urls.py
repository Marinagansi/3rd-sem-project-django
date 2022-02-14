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
          path('faq',views.faq,name='faq'),
           path('flights',views.flights,name="flights"),
            path('user_profile',views.user_profile),
            path('about_us',views.about_us,name="about_us"),
            path('hotel',views.hotel,name="hotel"),
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
            path('find_guide',views.find_guide,name='find_guide'),
            path('hotelreview',views.hotelreview,name='hotelreview'),
            path('pannel',views.admin_pannel),
<<<<<<< HEAD

=======
<<<<<<< HEAD

            path('admin_page',views.admin_page),

=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
            path('explore',views.explore,name="explore"),
            path('admin_page',views.admin_page,name="admin_page"),
=======
            path('explore',views.explore),
<<<<<<< HEAD
            path('admin_page',views.admin_page)
            
=======
>>>>>>> d85194fd25a77426d9c25edee2101532bbc382fd
            
>>>>>>> a1d29c4e92676589a7862a1c40ebc122375e5436
            path('explore',views.explore,name="explore"),
<<<<<<< HEAD

=======
            path('admin_page',views.admin_page)
<<<<<<< HEAD
=======
  
=======
            path('admin_page',views.admin_page),
>>>>>>> c675cc07b1e5cf379b823ef52cbddffcbe3c57a3
           
>>>>>>> a13402b7a9a88c0abfae2bd16c5ee8effd075b83
>>>>>>> d85194fd25a77426d9c25edee2101532bbc382fd
          
            




            

          
           
<<<<<<< HEAD
=======
       
   


>>>>>>> 74784d6c5df8bf8f74cbb3176f12ef21744fa27b
>>>>>>> a1d29c4e92676589a7862a1c40ebc122375e5436
>>>>>>> d85194fd25a77426d9c25edee2101532bbc382fd
>>>>>>> 5ca2431c64e3e0b72a9cfaec5356185a1a9d1675
]