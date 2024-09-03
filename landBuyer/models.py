from django.db import models

# Create your models here.

class LandBuyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)  
    username = models.CharField(max_length=150) 
    password = models.CharField(max_length=128) 
    email = models.EmailField(max_length=255, unique=True) 
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=50) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 

def __str__(self):
    return self.username
