from django.shortcuts import render,redirect
from booking_vehicle.models import VBooking
from book_flights.models import FBooking

from guide_booked.forms import gbooked
from guide_booked.models import GBooking
from book_guide.models import Book_guide
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def fillform(request,p_id):
    print(request)
    if request.method=="POST":
        form=gbooked(request.POST)
        form.save()
        messages.success(request,"your booking was done")
        return redirect ('find_guide')
              
    else:
        form=gbooked()
    guide=Book_guide.objects.get(guide_id=p_id)
    return render(request,"find_guide/guide_form2.html",{'guide':guide})


# history of user
def userhistory(request,p_id):        
    user=User.objects.get(id=p_id)
    guides=GBooking.objects.filter(customer_id=p_id)
    # vehicle=VBooking.objects.get(customer=p_id)
    
    vehicles=VBooking.objects.filter(customer_id=p_id)
    flights=FBooking.objects.filter(customer_id=p_id)
 
    print("invalid")
    
    return render(request,"user_history.html",{'guides':guides,'vehicles':vehicles,'flights':flights})