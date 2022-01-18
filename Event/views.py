from django.shortcuts import render,redirect
from Event.forms import EventForm
from Event.models import event

# Create your views here.
def event(request): 
    return render(request,'event.html')


def fillform(request):
    print(request)
    if request.method=="POST":
        form=EventForm(request.POST)
        form.save()
        return redirect ("home")
              
    else:
        form=EventForm()
    return render (request,"event_form.html",{'form':form})
