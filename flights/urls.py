from django.contrib import admin
from django.urls import path
from flights import views


urlpatterns = [
  
    path('flights/', views.flights, name="flights"),
    path('flights/book_flights', views.book_flights, name="flights"),
    #  path('flights/flight_ticket/<int:p_id>', views.flightsTicket, name="flights"),
<<<<<<< HEAD
    # path('flights/flight_ticket/<int:p_id>', views.flightsTicket, name="flights"),
=======
    #path('flights/flight_ticket/<int:p_id>', views.flightsTicket, name="flights"),
>>>>>>> 7926d69b176bfd1f796dfe46531d5799aebd83fd
    path('flights2/', views.flights2),
    path('search_flight', views.search_flights),
]