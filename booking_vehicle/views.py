from django.shortcuts import render,redirect
from booking_vehicle.models import VBooking
# Create your views here.



def fillform(request):
    print(request)
    if request.method=="POST":
        form=VBooking(request.POST)
        form.save()
        return redirect ('book_vehicle')
              
    else:
        form=VBooking()
    return render (request,"vehicle/book_vehicle.html",{'form':form})

def booking(request,p_id): 
    book=VBooking.objects.get(vehicle_id=p_id)
    return render(request,"vehicle/book_vehicle.html",{'book':book})

def book_flights(request): 

    flight=VBooking.objects.raw('select * from booking_vehicle')

    return render(request,"flight/book_flights.html",{'flight':flight})