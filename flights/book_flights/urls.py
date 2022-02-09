from django.contrib import admin
from django.urls import path
from book_flights import views
import book_flights


urlpatterns = [
  
path('ticket/<int:p_id>',views.book_flights)
]