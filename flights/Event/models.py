from django.db import models

# Create your models here
class event(models.Model):
    Event_id=models.AutoField(auto_created=True,primary_key=True)
    first=models.CharField(max_length=200)
    last=models.CharField(max_length=200)
    e_email=models.CharField(max_length=100)
    e_phone=models.CharField(max_length=10)
    e_message=models.CharField(max_length=500)
    e_budget=models.CharField(max_length=100)
    e_purpose=models.CharField(max_length=200)
    e_date=models.DateField()

    class Meta:
        db_table="Event" 
