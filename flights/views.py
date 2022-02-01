from django.shortcuts import render,redirect
from book_flights.forms import fbooked
from flights.models import Book_guide

# Create your views here.
def book_flights(request): 
    

    flight=Book_guide.objects.raw('select * from flights')

    return render(request,"flight/book_flights.html",{'flight':flight})

def flights2(request): 
    return render(request,'flights2.html')

def flights(request): 
    return render(request,'flight/flights.html')



def flightsTicket(request,p_id): 
    print(request)
    if request.method=="POST":
        form=fbooked(request.POST)
        form.save()
        return redirect ('/flights')
              
    else:
        form=fbooked()

    flight=Book_guide.objects.get(flight_id=p_id)
    return render(request,"flight/flight_ticket.html",{'flight':flight})

def search_flights(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Book_guide.objects.filter(flight_from__icontains= searched)
        count = Book_guide.objects.count()
        print(count)
        if (count > 1):
            #  return render(request,'flight/search_f.html',{'searched':searched,'venues':venues})
            return render(request,'flight/search_f.html',{'searched':searched,'venues':venues})
    else:
        # return render(request,'flight/search_f.html',{})
         return render(request,'flight/search_f.html',{})

 
   