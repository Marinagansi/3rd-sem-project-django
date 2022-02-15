from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,redirect
from hotel.forms import Hbooked, HotelFormStepOne,HotelFormStepTwo,HotelFormStepThree,HotelFormStepFour,HotelFormStepFive
from hotel.models import Hotel
from django.contrib import messages


def stepOneSubmit(request):
    print(request)
    if request.method=='POST':
        form=HotelFormStepOne(request.POST)
        data=form.save()
        return render(request,'list_property/add_hotel2.html',{'data':data})
    return render(request,'list_property/add_hotel.html')

def stepTwoSubmit(request,p_id):
    hotel=Hotel.objects.get(hotel_id=p_id)
    form=HotelFormStepTwo(request.POST,instance=hotel)
    data=form.save()
    print(data)
    return render(request,'list_property/add_hotel3.html',{'data':data})



def stepThreeSubmit(request,p_id):
    hotel=Hotel.objects.get(hotel_id=p_id)
    form=HotelFormStepThree(request.POST,instance=hotel)
    data=form.save()
    print(data)
    return render(request,'list_property/add_hotel4.html',{'data':data})

def stepFourSubmit(request,p_id):
    hotel=Hotel.objects.get(hotel_id=p_id)
    form=HotelFormStepFour(request.POST,request.FILES,instance=hotel)
    data=form.save()
    print(data)
    return render(request,'list_property/add_hotel5.html',{'data':data})

def stepFiveSubmit(request,p_id):
    hotel=Hotel.objects.get(hotel_id=p_id)
    form=HotelFormStepFive(request.POST,instance=hotel)
    data=form.save()
    print(data)
    return render(request,'list_property/partneracc_addproperty.html',{'data':data})


#for booking hotel
def hotel_details(request,p_id): 
    hotel=Hotel.objects.get(hotel_id=p_id)
    return render(request,'hotel_details.html',{'hotel':hotel})    

#booking hotel
def book_hotel(request,p_id):
    print(request)
    if request.method=="POST":
        form=Hbooked(request.POST)
        try:
            form.save()
            messages.success(request,"your booking was done")
            return redirect('/hotel')
        except:
            print("error")

    else:
        form=Hbooked()
    
    hotel=Hotel.objects.get(hotel_id=p_id)
    return render(request,'hotel_details.html',{'hotel':hotel,'form':form})   
