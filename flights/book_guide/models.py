from django.db import models

# Create your models here.
class Book_guide(models.Model):
    guide_id=models.AutoField(auto_created=True,primary_key=True)
    guide_name=models.CharField(max_length=200)
    guide_email=models.CharField(max_length=100)
    guide_address=models.CharField(max_length=100)
    guide_phone=models.CharField(max_length=10)
    guide_descripition=models.CharField(max_length=500)
    guide_image=models.FileField(upload_to="guide_images")

    class Meta:
        db_table="book_guide"
