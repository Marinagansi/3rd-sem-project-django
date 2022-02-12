from django.shortcuts import render,redirect
from food.forms import FoodForm
from food.models import Food

# Create your views here.
def food(request):
    return render (request,'Food/find_food.html')



def food_form(request):
    print(request.FILES)
    if request.method=="POST":
        forms=FoodForm(request.POST,request.FILES)
        forms.save()
        return redirect ("/partneracc_addproperty")
          

    else:
        foods=FoodForm() 
    return render(request,'list_property/add_food.html',{'foods':foods})


def search_food(request):
    if request.method == "POST":
        searched=request.POST['searched']
        venues=Food.objects.filter(food_place__icontains=searched)
        return render(request,'food/searched_food.html',{'searched':searched,'venues':venues})
    else:
        return render(request,'food/searched_food.html',{})
