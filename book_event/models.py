from django.db import models

# Create your models here.
class Book_event(models.Model):
    event_id=models.AutoField(auto_created=True,primary_key=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    event_email=models.CharField(max_length=100)
    event_phone=models.CharField(max_length=10)
    event_message=models.CharField(max_length=500)
    event_budget=models.CharField(max_length=100)
    purpose_event=models.CharField(max_length=200)
    event_date=models.DateField()

    class Meta:
        db_table="book_event"