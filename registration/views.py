from django.shortcuts import render
from book_guide.models import Book_guide
# Create your views here.
def home(request):
    return render(request,'home.html')

def guide(request): 

    guides=Book_guide.objects.raw('select * from book_guide')

    return render(request,"book_guide.html",{'guides':guides})
   

def event(request): 
    return render(request,'event.html')

def shop1(request): 
    return render(request,'shop.html')
def shop2(request): 
    return render(request,'shop2.html')

def try2(request): 
    return render(request,'try.html')