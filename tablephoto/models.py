from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=60)
    age=models.IntegerField()
    address=models.TextField()
    mobile=models.CharField(max_length=10)
    pic=models.ImageField(upload_to='media/')