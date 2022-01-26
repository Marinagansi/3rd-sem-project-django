from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_id=models.AutoField(auto_created=True,primary_key=True)
    hotel_name=models.CharField(max_length=200)
    hotel_address=models.CharField(max_length=200)
    hotel_email=models.CharField(max_length=100)
    hotel_phone=models.CharField(max_length=10)
    hotel_image=models.CharField(max_length=500)
    Hotel_description=models.CharField(max_length=500)

    class Meta:
        db_table="hotel"
