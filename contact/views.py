from django.shortcuts import render,redirect
from contact.forms import  ContactForm
from django.contrib import messages


# Create your views here.

def contact(request):
    print(request)
    if request.method=="POST":
        form=ContactForm(request.POST)
        form.save()
        return redirect ('/home')
              
    else:
        form=ContactForm()
    return render (request,"contact.html",{'form':form})





