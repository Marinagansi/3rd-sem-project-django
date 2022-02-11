from django.shortcuts import render,redirect
from Event.forms import EventForm
from Event.models import event
from django.contrib import messages

# Create your views here.
def event(request): 
    return render(request,'event/event.html')


def receipt(request): 
    return render(request,'event/booked_event.html')


def fillform(request):
    print(request)
    if request.method=="POST":
        form=EventForm(request.POST)
        try:
            form.save()
            messages.success(request,"your booking was done")
            return redirect ('booked_event')

        except:
            print("false")  
    else:
        form=EventForm()
    return render (request,"event/event_form.html",{'form':form})


def Event(request): 

    events=event.objects.raw('select * from Event')

    return render(request,"Event.html",{'events':events})