from collections import UserString
from django.db import models
from rent.models import VDetails
from django.contrib.auth.models import User

# Create your models here.
class VBooking(models.Model):
    vbooking_id=models.AutoField(auto_created=True,primary_key=True)
    vehicle=models.ForeignKey(VDetails,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    start_date = models.DateField()
    end_date=models.DateField()

    class Meta:
        db_table="boking_vehicle"

