from django.db import models
from landBuyer.models import LandBuyer

class Lawyer(models.Model):
    lawyer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    land_buyer = models.ForeignKey(LandBuyer, on_delete=models.CASCADE)

def __str__(self):
    return self.username





# from django.db import models
# from .models import LandBuyer

# # Create your models here.

# class Lawyer(models.Model):
#     lawyer_id = models.AutoField(primary_key=True) 
#     username = models.CharField(max_length=100)  
#     password = models.CharField(max_length=50) 
#     email = models.EmailField(max_length=255, unique=True)  
#     role = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True) 
#     land_buyer =  models.ForeignKey(LandBuyer, on_delete=models.CASCADE)

# def __str__(self):
#     return f"{self.username}"
