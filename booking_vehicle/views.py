from django.shortcuts import render,redirect
from booking_vehicle.models import VBooking
from booking_vehicle.forms import vbooked, vupdatebooked
# Create your views here.




  
# for booking
def booking(request,p_id): 
    print(request)
    if request.method=="POST":
        form=vbooked(request.POST)
        form.save()
        return redirect ('vehicle')
              
    else:
        form=vbooked()
    book=VBooking.objects.get(vehicle_id=p_id)
    return render(request,"vehicle/book_vehicle.html",{'book':book})

def book_vehicle(request): 

    vehicles=VBooking.objects.raw('select * from boking_vehicle')

    return render(request,"vehicle/book_vehicle3.html",{'vehicles':vehicles})

def edit(request,p_id):
    vehicles=VBooking.objects.get(vbooking_id=p_id)
    return render (request,"vehicle/update_vehicle.html",{'vehicles':vehicles})

def update(request,p_id):
    #data verification
    print(request.POST)
    vehicles=VBooking.objects.get(vbooking_id=p_id)
    #bind data in form with instance of customer
    form = vbooked(request.POST, instance=vehicles)
    if form.is_valid():
        try:
            form.save()
            return redirect("/vehicle_rent")
        except:
            print("validation false")

    return render(request,"vehicle/update_vehicle.html",{'vehicles':vehicles})