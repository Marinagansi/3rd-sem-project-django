from django.db import models

# Create your models here.
class Food(models.Model):
    food_id=models.AutoField(auto_created=True,primary_key=True)
    food_name=models.CharField(max_length=200)
    food_place=models.CharField(max_length=200)
    food_details=models.CharField(max_length=200)
    food_type=models.CharField(max_length=200)
    food_image=models.FileField(upload_to='food_image')

    class Meta:
        db_table="food"



    
