from django.shortcuts import render
from book_guide.models import Book_guide

# Create your views here.
def guide(request): 

    guides=Book_guide.objects.raw('select * from book_guide')

    return render(request,"book_guide.html",{'guides':guides})
