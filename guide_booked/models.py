from django.db import models
from django.contrib.auth.models import User
from book_guide.models import Book_guide

# Create your models here.
class GBooking(models.Model):
    Gbooking_id=models.AutoField(auto_created=True,primary_key=True)
    guide=models.ForeignKey(Book_guide,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    Nationality=models.CharField(max_length=200)
    visit=models.CharField(max_length=100)
    group_size=models.CharField(max_length=200)
    days=models.CharField(max_length=100)
    start_date= models.DateField()
    More_details=models.CharField(max_length=200)


    class Meta:
        db_table="guide_booked"