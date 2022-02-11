from django.db import models
from django.contrib.auth.models import User
from trip.models import TripPackage

# Create your models here.
class TBooking(models.Model):
    TBooking_id=models.AutoField(auto_created=True,primary_key=True)
    packages=models.ForeignKey(TripPackage,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    Nationality=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    group_size=models.CharField(max_length=100)
    arrival_data= models.DateField()
    other_details=models.CharField(max_length=200)

    class Meta:
        db_table="book_trip"