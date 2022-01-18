from django.shortcuts import render

# Create your views here.
def event(request): 
    return render(request,'event.html')

def form(request): 
    return render(request,'event_form.html')

def create(request):
    print(request)
    if request.method=="POST":
        form=CustomerForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect ("/customer/index")
            except:
                    
                print("invalid")

    else:
        form=CustomerForm()
        print("invalid")
    return render (request,"customer/create.html",{'form':form})
                    