from django.db import models

# Create your models here.
class Book_guide(models.Model):
    flight_id=models.AutoField(auto_created=True,primary_key=True)
    flight_name=models.CharField(max_length=200)
    flight_from=models.CharField(max_length=100)
    flight_to=models.CharField(max_length=100)
    flight_way=models.CharField(max_length=100)
    flight_money=models.CharField(max_length=500)
    flight_date=models.DateField()
    flight_time=models.TimeField()
    class Meta:
        db_table="flights"

