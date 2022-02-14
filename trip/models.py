from django.db import models

# Create your models here.
class TripPackage(models.Model):
    package_id=models.AutoField(auto_created=True,primary_key=True)
    package_name=models.CharField(max_length=100)
    trip_days=models.CharField(max_length=100)
    itinary_route=models.CharField(max_length=150)
    details1=models.CharField(max_length=200)
    details2=models.CharField(max_length=200)
    trip_image=models.FileField(upload_to='trip')


    class Meta:
        db_table="trip"