from django.shortcuts import render,redirect
from booking_vehicle.models import VBooking
from booking_vehicle.forms import vbooked
# Create your views here.



def fillform(request,p_id):
    print(request)
    if request.method=="POST":
        form=vbooked(request.POST)
        form.save()
        return redirect ('home')
              
    else:
        form=vbooked()
    vehicle=VBooking.objects.get(vbooking_id=p_id)
    return render(request,"vehicle/book_vehicle.html",{'form':form},{'p_id_id':p_id,'vehicle':vehicle})

  

def booking(request,p_id): 
    print(request)
    if request.method=="POST":
        form=vbooked(request.POST)
        form.save()
        return redirect ('home')
              
    else:
        form=vbooked()
    book=VBooking.objects.get(vehicle_id=p_id)
    return render(request,"vehicle/vehicle_details.html",{'book':book})

def book_flights(request): 

    flight=VBooking.objects.raw('select * from booking_vehicle')

    return render(request,"flight/book_flights.html",{'flight':flight})