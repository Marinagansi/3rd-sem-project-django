from django.shortcuts import render,redirect
from book_trip.models import TBooking
from book_trip.forms import tbooked
from trip.models import TripPackage


# Create your views here.
# fill form for booking trip
def fillform(request,p_id):
    print(request)
    if request.method=="POST":
        form=tbooked(request.POST)
        form.save()
        return redirect ('home')
              
    else:
        form=tbooked()
    packages=TripPackage.objects.get(package_id=p_id)
    return render(request,"trip/trip.html",{'packages':packages})

  
