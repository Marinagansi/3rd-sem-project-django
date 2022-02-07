from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_id=models.AutoField(auto_created=True,primary_key=True)
    hotel_name=models.CharField(max_length=200)
    contact_name=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=100)
    hotel_address=models.CharField(max_length=100)
    hotel_region=models.CharField(max_length=100)
    room_type=models.CharField(max_length=100)
    smoking_policy=models.CharField(max_length=100)
    no_of_rooms=models.CharField(max_length=100)
    Beds=models.CharField(max_length=100)
    no_of_guest=models.CharField(max_length=100)
    parking=models.CharField(max_length=100)
    Breakfast=models.CharField(max_length=100)
    image1=models.FileField(upload_to='hotel_images')
    image2=models.FileField(upload_to='hotel_images')
    cancelation=models.CharField(max_length=100)
    Day_of_payment=models.CharField(max_length=100)
    Hotel_description=models.CharField(max_length=500)
    check_in_from=models.CharField(max_length=100)
    check_in_to=models.CharField(max_length=100)
    check_out_from=models.CharField(max_length=100)
    check_out_to=models.CharField(max_length=100)
    pet=models.CharField(max_length=100)
    class Meta:
        db_table="hotel"
