from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,redirect
from hotel.forms import HotelForm1,HotelForm2,HotelFormStepOne,HotelFormStepTwo
from hotel.models import Hotel

# Create your views here.
# def hotel_form(request):
#     print(request)
#     if request.method=="POST":
#         form=HotelForm1(request.POST)
#         result=form.save()
#         # hotels=result.objects.get(result.hotel_name)
#         return redirect (reverse('hotel2',args=[result.hotel_name]))
              
#     else:
#         form=HotelForm1()
#     return render (request,"list_property/add_hotel.html",{'form':form})

# def update_hotel(request,hotel_name):
#     print(request.POST)
#     hotels=Hotel.objects.get(hotel_name=hotel_name)
#     #bind data in form with instance of customer
#     form = HotelForm2(request.POST, instance=hotels)
#     if form.is_valid():
#         try:
#             form.save()
#             return redirect("/hotel/add_hotel2")
#         except:
#             print("validation false")

#     return render(request,"list_property/add_hotel2.html",{'hotels':hotels})

# def hotel2(request):
#     return render(request,"list_property/add_hotel2.html")

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
    return render(request,'list_property/add_hotel2.html',{'data':data})

#views
def step1(request):
    initial={'hotel_name':request.session.get('hotel_name',None)}
    form=HotelForm1(request.POST , initial=initial)
    if request.method =='POST':
        if form.is_valid():
            request.session['hotel_name']=form.cleaned_data['hotel_name']
            return HttpResponseRedirect(reverse('step2'))

    return render(request,'list_property/add_hotel.html',{'form':form})

def step2(request):
    form=HotelForm2(request.POST)
    print(request)
    if request.method=='POST':
        if form.is_valid():
            hotels=form.save(commit=False)
            step=Hotel.objects.create(hotel_name=request.session['hotel_name'])
            hotels.hotel_name=step
            hotels.save()
            return HttpResponseRedirect(reverse('home'))
    return render (request,'list_property/add_hotel2.html',{'form':form})
   