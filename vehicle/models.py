from django.db import models

# Create your models here.
class VDetails(models.Model):
    vehicle_id=models.AutoField(auto_created=True,primary_key=True)
    Vehicle_model=models.CharField(max_length=200)
    vehicle_color=models.CharField(max_length=100)
    vehicle_rent=models.CharField(max_length=100)
    vehicle_purchase=models.DateField()
    vehicle_image=models.FileField(upload_to='vehicle')

    class Meta:
        db_table="vehicle"