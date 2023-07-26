from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.TextField()
    mobile=models.CharField(max_length=10)
    pic=models.ImageField(upload_to='media/')