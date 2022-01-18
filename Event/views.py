from django.shortcuts import render,redirect
from Event.forms import EventForm
from Event.models import event

# Create your views here.
def event(request): 
    return render(request,'event/event.html')


def receipt(request): 
    return render(request,'event/booked_event.html')


def fillform(request):
    print(request)
    if request.method=="POST":
        form=EventForm(request.POST)
        form.save()
        return redirect ('booked_event')
              
    else:
        form=EventForm()
    return render (request,"event/event_form.html",{'form':form})


def Event(request): 

    events=event.objects.raw('select * from Event')

    return render(request,"Event.html",{'events':events})