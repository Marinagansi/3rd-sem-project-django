from django.shortcuts import render,redirect
from book_guide.models import Book_guide
from registration.forms import CustomerForm
from registration.models import Registration
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from hotel.models import Hotel
from book_flights.models import FBooking
from guide_booked.models import GBooking
from booking_vehicle.models import VBooking

# Create your views here.
def firstpage(request):
    return render(request,'firstpage.html')

def things_to_do(request):
    return render(request,'things_to_do.html')

def package(request):
    return render(request,'packages.html')


def guide(request): 

    guides=Book_guide.objects.raw('select * from book_guide')

    return render(request,"book_guide.html",{'guides':guides})
   

def hotel(request): 
    hotels=Hotel.objects.raw('select * from hotel')
    return render(request,'hotel.html',{'hotels':hotels})


def forget_password(request): 
    return render(request,'list_property/forget_password.html')
def forget_username(request): 
    return render(request,'list_property/forget_username.html')
def having_trouble(request): 
    return render(request,'list_property/having_trouble.html')
def partneracc_addproperty(request): 
    return render(request,'list_property/partneracc_addproperty.html') 
def userprofile2(request): 
    return render(request,'user_profile2.html') 
<<<<<<< HEAD
 


def hotel_details(request): 
    return render(request,'hotel_details.html')     
=======

def hotel_details(request): 
    return render(request,'hotel_details.html') 
    
        
>>>>>>> 2a57676da1b5617d8aa03e33e230ba522a87bde3
# for login list property 
def partneracc_signin(request): 
   
    if request.method=='POST':
        customer_name=request.POST.get("customer_name")
        customer_pasword=request.POST.get("customer_address")
        try:
            user=Registration.objects.get(customer_name=customer_name,customer_address=customer_pasword)
       
            if user is not None:

                request.session['customer_name']=user.customer_name
                request.session['customer_email']=user.customer_email
                return redirect ("/partneracc_addproperty")
           
        except:
            print("invalid")
            messages.info(request,"incorect username and password")
       
           
    
    return render(request,'list_property/partneracc_signin.html')  

def partneracc_signin2(request): 
    return render(request,'list_property/partneracc_signin2.html')  

#for hotel registration
def partneracc_signup3(request): 
    if request.method=="POST":
        form=CustomerForm(request.POST)
        try:
        # print(form)
            result=form.save()
            request.session['customer_id']=result.customer_id
            return redirect ("/home")
           
        except:
            print("invalid")

    else:

        form=CustomerForm()
        print("invalid")
               
    return render(request,'list_property/partneracc_signup3.html', {'form':form})

def partneracc_signup2(request): 
    return render(request,'list_property/partneracc_signup2.html')   
def partneracc_signup(request): 
    return render(request,'list_property/partneracc_signup.html')     

def about_us(request): 
    return render(request,'about_us.html')
def shop1(request): 
    return render(request,'shop.html')
def shop2(request): 
    return render(request,'shop2.html')

def try2(request): 
    return render(request,'try.html')

def faq(request): 
    return render(request,'faq.html')

def flights(request): 
    return render(request,'flight/flights.html')

def find_guide(request): 
    return render(request,'find_guide/find_guide.html')

def user_profile(request): 
    return render(request,'user_profile.html')

def explore(request): 
    return render(request,'explore.html')
def admin_pannel(request): 
    flights=FBooking.objects.all
    guides=GBooking.objects.all
    vehicles=VBooking.objects.all
    return render(request,'adminn/admin_page.html',{'flights':flights,'guides':guides,'vehicles':vehicles})
def admin_page(request): 
    return render(request,'adminn/admin_page.html')



# sigin from firstpage

def signin(request):
    if request.method=='POST':
        print(request)
      
        customer_name=request.POST["customer_name"]
        customer_password=request.POST["customer_phone"]
        try:
            print(request)   
            admin=Registration.objects.get(customer_name=customer_name,customer_address=customer_password)
            if admin is not None:
                return redirect ("/pannel")
            
        except:
            user = authenticate(request, username=customer_name,password=customer_password)
            if user is not None:
                    login(request, user)
                    # print(request.user.username)
                    return redirect ("/home")
            return render("/login")

    else:
        messages.info(request,'Invalid user')
       
    return render(request,"signup.html")
    
    



def registration(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        
        psw=request.POST['psw']

        user=User.objects.create_user(username=name,email=email,password=psw)
        user.save()
    return render (request,"signup.html")


                    
@login_required(login_url='/login')
def home(request): 

    user=Registration.objects.raw('select * from registration')

    return render(request,"home.html",{'user':user})                

def user_profile(request): 
    
    return render(request,"user_profile.html")

def logout_view(request):
    logout(request)
    return redirect('/firstpage')



def list_nav(request): 
    return render(request,'list_property/list_nav.html')        

def hotelreview(request):
    return render (request,'hotelreview.html')



