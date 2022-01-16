from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def guide(request): 
    return render(request,'book_guide.html')

def event(request): 
    return render(request,'event.html')

def shop1(request): 
    return render(request,'shop.html')
def shop2(request): 
    return render(request,'shop2.html')