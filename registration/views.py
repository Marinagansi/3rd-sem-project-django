from django.shortcuts import render,redirect
from book_guide.models import Book_guide
from registration.forms import CustomerForm
from registration.models import Registration
# Create your views here.
def home(request):
    return render(request,'home.html')

def guide(request): 

    guides=Book_guide.objects.raw('select * from book_guide')

    return render(request,"book_guide.html",{'guides':guides})
   


def firstpage(request): 
    return render(request,'firstpage.html')

def shop1(request): 
    return render(request,'shop.html')
def shop2(request): 
    return render(request,'shop2.html')

def try2(request): 
    return render(request,'try.html')

def faq(request): 
    return render(request,'faq.html')

def flights(request): 
    return render(request,'flights.html')

def user_profile(request): 
    return render(request,'user_profile.html')

def vehicle_rent(request): 
    return render(request,'vehicle_rent.html')


def signin(request):
    if request.method=='POST':
        customer_name=request.POST.get("customer_name")
        customer_password=request.POST.get("customer_phone")

        user=Registration.objects.get(customer_name=customer_name,customer_phone=customer_password)
        if user is not None:
            return redirect ("home")

      
    return render(request,"signup.html")
    
    



def registration(request):
    print(request)
    if request.method=="POST":
        form=CustomerForm(request.POST)
        form.save()
        return redirect ("home")
              
    else:
        form=CustomerForm()
    return render (request,"signup.html",{'form':form})
                    