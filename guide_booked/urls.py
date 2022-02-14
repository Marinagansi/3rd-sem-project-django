from django.contrib import admin
from django.urls import path
from guide_booked import views


urlpatterns = [
  
    path('guide_form/<int:p_id>',views.fillform),
    path('history/<int:p_id>',views.userhistory)

]