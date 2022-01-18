from django.shortcuts import render,redirect
from book_guide.models import Book_guide
from registration.forms import CustomerForm
from registration.models import Registration
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.
def firstpage(request):
    return render(request,'firstpage.html')

def guide(request): 

    guides=Book_guide.objects.raw('select * from book_guide')

    return render(request,"book_guide.html",{'guides':guides})
   




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

        # user=Registration.objects.get(customer_name=customer_name,customer_phone=customer_password)
        # if user is not None:
        

        user = authenticate(request, username=customer_name,password=customer_password)
      
        if user is not None:
            login(request, user)
            print(request.user.username)
            return redirect ("home")
      
    return render(request,"signup.html")
    
    



def registration(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        
        psw=request.POST['psw']

        user=User.objects.create_user(username=name,email=email,password=psw)
        user.save()
    return render (request,"signup.html")
    # print(request)
    # if request.method=="POST":
    #     form=CustomerForm(request.POST)
    #     form.save()
    #     return redirect ("home")
              
    # else:
    #     form=CustomerForm()
    # return render (request,"signup.html",{'form':form})
                    

def home(request): 

    user=Registration.objects.raw('select * from registration')

    return render(request,"home.html",{'user':user})                
