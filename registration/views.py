from django.shortcuts import render,redirect
from book_guide.models import Book_guide
from registration.forms import CustomerForm
from registration.models import Registration
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def firstpage(request):
    return render(request,'firstpage.html')

def guide(request): 

    guides=Book_guide.objects.raw('select * from book_guide')

    return render(request,"book_guide.html",{'guides':guides})
   

def hotel(request): 
    return render(request,'hotel.html')
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
# for login list property 
def partneracc_signin(request): 
   
    if request.method=='POST':
        customer_name=request.POST.get("customer_name")
        customer_pasword=request.POST.get("customer_address")
        try:
            user=Registration.objects.get(customer_name=customer_name,customer_address=customer_pasword)
       
            if user is not None:
          
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
        # print(form)
        form.save()
                
        return redirect ("/home")
           

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

def user_profile(request): 
    return render(request,'user_profile.html')

   




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
    # print(request)
    # if request.method=="POST":
    #     form=CustomerForm(request.POST)
    #     form.save()
    #     return redirect ("home")
              
    # else:
    #     form=CustomerForm()
    # return render (request,"signup.html",{'form':form})
                    
@login_required(login_url='/login')
def home(request): 

    user=Registration.objects.raw('select * from registration')

    return render(request,"home.html",{'user':user})                

def user_profile(request): 
    
    return render(request,"user_profile.html")

def logout_view(request):
    logout(request)
    return redirect('/firstpage')

# login for hotels
# def Hsignin(request):
#     print(request)
#     if request.method=='POST':
#         customer_name=request.POST.get("customer_name")
#         customer_pasword=request.POST.get("customer_pasword")

#         user=Registration.objects.get(customer_name=customer_name,customer_pasword=customer_pasword)
#         if user is not None:
#             return redirect ("/registration/index")

#         else:
#             messages.info(request,"incorect username and password") 
#     return render(request,'registration/login.html')

#for hotel registration
# def Hregistration(request):
#         # print(request)

#         if request.method=="POST":

#             form=CustomerForm(request.POST)
#         # print(form)

#             if form.is_valid():
#                 try:
#                     print("valid")
#                     form.save()
                    
#                     return redirect ("/registration/index")
#                 except:
                    
#                  print("invalid")

#         else:

#                 form=CustomerForm()
#                 print("invalid")
#                 return render (request,"registration/registration.html",{'form':form})