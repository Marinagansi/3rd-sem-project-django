from django.shortcuts import render,redirect
from hotel.forms import HotelForm1,HotelForm2
from hotel.models import Hotel

# Create your views here.
def hotel_form(request):
    print(request)
    if request.method=="POST":
        form=HotelForm1(request.POST)
        form.save()
        return redirect ('/hotel/hotel2/')
              
    else:
        form=HotelForm1()
    return render (request,"list_property/add_hotel.html",{'form':form})

def update_hotel(request,hotel_name):
    print(request.POST)
    hotels=Hotel.objects.get(hotel_name=hotel_name)
    #bind data in form with instance of customer
    form = HotelForm2(request.POST, instance=hotels)
    if form.is_valid():
        try:
            form.save()
            return redirect("/hotel/add_hotel#form2")
        except:
            print("validation false")

    return render(request,"list_property/add_hotel.html",{'hotels':hotels})