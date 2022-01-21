from django.shortcuts import redirect, render
from rent.forms import RentForm
from rent.models import VDetails
from django.contrib.auth.models import User

# Create your views here.
def create(request):
    print(request.FILES)
    if request.method=="POST":
        rents=RentForm(request.POST,request.FILES)
        rents.save()
        return redirect ("/vehicle/vehicle_rent")
          

    else:
        rents=RentForm()
     
    return render (request,"vehicle/vehicle_form.html",{'rents':rents})

def vehicle(request): 

    rents=VDetails.objects.raw('select * from rent')

    return render(request,"vehicle/vehicle_rent.html",{'rents':rents})

def V_details(request,p_id): 
    rents=VDetails.objects.get(v_id=p_id)
    return render(request,"vehicle/vehicle_details.html",{'rents':rents})

def customer(request): 

    customers=User.objects.raw('select * from auth_user')

    return render(request,"vehicle/vehicle_rent.html",{'customers':customers})