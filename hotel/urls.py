from django.contrib import admin
from django.urls import path,re_path
from hotel import views


urlpatterns = [
  
    # path('add_hotel', views.hotel_form),
    # re_path(r'^hotel/hotel2/(?hotel_name>\d+)/$', views.step2, name='add_hotel2')
    # path('update_hotel/<str:hotel_name',views.update_hotel,name="hotel2")
    path('add_hotel', views.stepOneSubmit),
    path('add_hotel/<int:p_id>', views.stepTwoSubmit),

    path('hotel2',views.step2,name='step2')
    
    
   
]