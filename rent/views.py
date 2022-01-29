from django.shortcuts import redirect, render
from rent.forms import RentForm
from rent.models import VDetails
from django.contrib.auth.models import User
from booking_vehicle.models import VBooking
from booking_vehicle.forms import vbooked

# Create your views here.
def create(request):
    print(request.FILES)
    if request.method=="POST":
        rents=RentForm(request.POST,request.FILES)
        rents.save()
        return redirect ("/partneracc_addproperty")
          

    else:
        rents=RentForm()
     
    return render (request,"vehicle/vehicle_form.html",{'rents':rents})

def vehicle(request): 

    rents=VDetails.objects.raw('select * from rent')

    return render(request,"vehicle/vehicle_rent.html",{'rents':rents})

# for forienkey
def V_details(request,p_id):
    print(request)
    if request.method=="POST":
        form=vbooked(request.POST)
        form.save()
        return redirect ('home')
              
    else:
        form=vbooked() 
    rents=VDetails.objects.get(v_id=p_id)
    return render(request,"vehicle/vehicle_details.html",{'rents':rents})

def customer(request): 

    customers=User.objects.raw('select * from auth_user')

    return render(request,"vehicle/vehicle_rent.html",{'customers':customers})