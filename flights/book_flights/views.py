from django.shortcuts import render,redirect
from book_flights.forms import fbooked
from book_flights.models  import FBooking
from flights.models import Book_guide
from django.contrib import messages

# Create your views here.
# booking flights

    
def book_flights(request,p_id):
    print(request)
    if request.method == 'POST':
        form=fbooked(request.POST)
        form.save()
        messages.success(request,"your booking was done")
        return redirect('/flights')
    else:
        form=fbooked()
    flight=Book_guide.objects.get(flight_id=p_id)
    return render (request,'flight/flight_ticket2.html',{'form':form,'flight':flight})

