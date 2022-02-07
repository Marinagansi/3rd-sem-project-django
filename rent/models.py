from django.db import models

# Create your models here.
class VDetails(models.Model):
    v_id=models.AutoField(auto_created=True,primary_key=True)
    V_model=models.CharField(max_length=200)
    v_color=models.CharField(max_length=100)
    v_rent=models.CharField(max_length=100)
    v_purchase=models.DateField()
 
    v_image=models.FileField(upload_to='rent')

    class Meta:
        db_table="rent"