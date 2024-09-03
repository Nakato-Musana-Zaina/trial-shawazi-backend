from django.db import models
from landDetails.models import LandTitleDetails

class LandSeller(models.Model):
    owner_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=255)  # Increased length
    phone_number = models.CharField(max_length=15)  # Changed to CharField
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)  # Changed to auto_now_add
    updated_at = models.DateField(auto_now=True)  # Corrected to updated_at

    land_title_details = models.ForeignKey(LandTitleDetails, on_delete=models.CASCADE, related_name='titledetails')

    def __str__(self):
        return f"{self.user_name} {self.email}"









# from django.db import models

# class LandSeller(models.Model):
#     owner_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=100)
#     national_id = models.CharField(max_length=255)  # Changed length for longer IDs
#     phone_number = models.CharField(max_length=15)  # Changed to CharField for phone formats
#     email = models.EmailField(max_length=255)
#     password = models.CharField(max_length=25)
#     address = models.CharField(max_length=255)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)
#     land_title_details = models.ForeignKey('LandTitleDetails', on_delete=models.CASCADE)  # Use string reference

#     def __str__(self):
#         return f"{self.user_name} {self.email}"




# from django.db import models

# class LandSeller(models.Model):
#     owner_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=100)
#     national_id = models.CharField(max_length=255)  # Changed to accommodate longer IDs
#     phone_number = models.CharField(max_length=15)  # Changed to CharField for various phone formats
#     email = models.EmailField(max_length=255)
#     password = models.CharField(max_length=25)
#     address = models.CharField(max_length=255)
#     created_at = models.DateField(auto_now_add=True)  # Changed to auto_now_add for creation date
#     updated_at = models.DateField(auto_now=True)  # Changed to updated_at

#     land_title_details = models.ForeignKey('LandTitleDetails', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user_name} {self.email}"








# from django.db import models
# from .models import LandTitleDetails

# # Create your models here.
# class LandSeller(models.Model):
#     owner_id = models.AutoField(primary_key=True)  
#     user_name = models.CharField(max_length=100)    
#     national_id = models.CharField(max_length=8)  
#     phone_number = models.PositiveSmallIntegerField()  
#     email = models.EmailField(max_length=255) 
#     password = models.CharField(max_length=25)
#     address = models.CharField(max_length=255)  
#     created_at = models.DateField(auto_now=True)
#     Updated_at = models.DateField(auto_now_add=True) 
#     land_title_details = models.ForeignKey(LandTitleDetails, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user_name} {self.email}"

