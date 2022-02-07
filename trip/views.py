from django.shortcuts import render,redirect
from trip.forms import TripForm
from trip.models import TripPackage
from book_trip.forms import tbooked

# Create your views here.
def trip(request,p_id):
    print(request)
    if request.method=="POST":
        form=tbooked(request.POST)
        form.save()
        return redirect ('/trip/trip1')
              
    else:
        form=tbooked()
    packages=TripPackage.objects.get(package_id=p_id)
    trips=TripPackage.objects.raw('select * from trip')
    return render(request,"trip/trip2.html",{'trips':trips,'packages':packages})

def trip1(request):
    trips=TripPackage.objects.raw('select * from trip')
    return render(request,"trip/trip.html",{'trips':trips,})



def create(request):
    print(request.FILES)
    if request.method=="POST":
        trips=TripForm(request.POST,request.FILES)
        trips.save()
        return redirect ("/partneracc_addproperty")
          

    else:
        trips=TripForm()
     
    return render (request,"trip/trip_form.html",{'trips':trips})


def package_form(request,p_id):
    
    packages=TripPackage.objects.get(package_id=p_id)
    return render (request,"trip/trip.html",{'packages':packages})

