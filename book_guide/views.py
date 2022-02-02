from django.shortcuts import render,redirect
import book_guide
from book_guide.models import Book_guide
from book_guide.forms import GuideForm

# Create your views here.
def guide(request): 

    guides=Book_guide.objects.raw('select * from book_guide')

    return render(request,"guide/book_guide.html",{'guides':guides})

def add_guide(request):
    print(request.FILES)
    if request.method=="POST":
        forms=GuideForm(request.POST,request.FILES)
        forms.save()
        return redirect ("/partneracc_addproperty")
          

    else:
        guides=GuideForm() 
    return render(request,'list_property/add_guide.html',{'guides':guides})

def guide_info(request):
    if request.method == "POST":
        guide_name1 = request.POST['searched']
        guides=Book_guide.objects.filter(guide_name__contains=guide_name1)

        return render(request,"list_property/update_guide.html",{'guide_name1':guide_name1,'guides': guides})

    else:
            
         return render(request,"list_property/update_guide.html",{})

def edit(request,edit):
    guides=Book_guide.objects.get(guide_name=edit)
    return render (request,"list_property/update_guide.html",{'guides':guides})

def update1(request,guide_name):
    print(request.POST)
    guides=Book_guide.objects.get(guide_name=guide_name)
    #bind data in form with instance of customer
    form = GuideForm(request.POST, instance=guides)
    if form.is_valid():
        try:
            form.save()
            return redirect("/home")
        except:
            print("validation false")

    return render(request,"list_property/update_guide.html",{'guides':guides})

def search_guide(request):
    if request.method == "POST":
        searched=request.POST['searched']
        venues=Book_guide.objects.filter(guide_address__icontains=searched)
        return render(request,'find_guide/searched_guide.html',{'searched':searched,'venues':venues})
    else:
        return render(request,'find_guide/searched_guide.html',{})


def guide_form(request,p_id):
    guides=Book_guide.objects.get(guide_id=p_id)
    return render (request,"find_guide/guide_form.html",{'guides':guides})


