from django.contrib import admin
from django.urls import path
from book_guide import views


urlpatterns = [
  
    path('guide/',views.guide),
    path('add_guide',views.add_guide),
    path('edit/<str:edit>',views.add_guide),
    path('guide_info',views.guide_info),
    path('update1/<str:guide_name>',views.update1),
    path('searched_guide',views.search_guide),
    path('book_guide/<int:p_id>',views.guide_form),
    
    
       
   
]