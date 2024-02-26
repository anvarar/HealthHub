from django.db import models

# Create your models here.
class add_details(models.Model):
    medicine_name=models.CharField(max_length=30)
    dosage=models.CharField(max_length=15)
    price=models.IntegerField(max_length=30)
    description=models.CharField(max_length=50)