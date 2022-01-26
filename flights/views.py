from django.shortcuts import render

from flights.models import Book_guide

# Create your views here.
def book_flights(request): 

    flight=Book_guide.objects.raw('select * from flights')

    return render(request,"flight/book_flights.html",{'flight':flight})

def flights2(request): 
    return render(request,'flights2.html')

def flights(request): 
    return render(request,'flight/flights.html')


def flightsTicket(request,p_id): 
    flight=Book_guide.objects.get(flight_id=p_id)
    return render(request,"flight/flight_ticket.html",{'flight':flight})

