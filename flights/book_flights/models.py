from django.db import models
from flights.models import Book_guide
from django.contrib.auth.models import User
# Create your models here.
class FBooking(models.Model):
    fbooking_id=models.AutoField(auto_created=True,primary_key=True)
    flights=models.ForeignKey(Book_guide,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    tickets=models.CharField(max_length=100)
    
    class Meta:
        db_table="book_flight"