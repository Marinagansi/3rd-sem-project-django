from django.contrib import admin
from django.urls import path,re_path
from trip import views


urlpatterns = [
    path('tripp/<int:p_id>',views.trip) ,
    path('trip_form', views.create),
    path('package_form/<int:p_id>',views.package_form),
    path('trip1',views.trip1)
]

    
    
    
   