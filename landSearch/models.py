from django.db import models

class SearchDetails(models.Model):
    land_id = models.AutoField(primary_key=True)
    title_number = models.CharField(max_length=25)
    owners_name = models.CharField(max_length=100)
    previous_owners_name = models.CharField(max_length=100)
    property_address = models.CharField(max_length=255)
    land_location = models.CharField(max_length=255)
    parcel_number = models.CharField(max_length=50)
    deed_type = models.CharField(max_length=50)
    date_of_issue = models.DateField()
    grantors = models.CharField(max_length=255)
    property_size = models.CharField(max_length=50)
    restrictions = models.CharField(max_length=255)
    mortgage_information = models.CharField(max_length=255)
    land_title_details = models.OneToOneField('LandTitleDetails', on_delete=models.CASCADE)  # Use string reference

    def __str__(self):
        return f"{self.title_number}, {self.owners_name}"





# from django.db import models

# class SearchDetails(models.Model):
#     land_id = models.AutoField(primary_key=True)
#     title_number = models.CharField(max_length=25)
#     owners_name = models.CharField(max_length=100)
#     previous_owners_name = models.CharField(max_length=100)  # Changed to lowercase
#     property_address = models.CharField(max_length=255)
#     land_location = models.CharField(max_length=255)
#     parcel_number = models.CharField(max_length=50)
#     deed_type = models.CharField(max_length=50)
#     date_of_issue = models.DateField()
#     grantors = models.CharField(max_length=255)
#     property_size = models.CharField(max_length=50)
#     restrictions = models.CharField(max_length=255)
#     mortgage_information = models.CharField(max_length=255)
#     land_title_details = models.OneToOneField('LandTitleDetails', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.title_number}, {self.owners_name}"









# from django.db import models
# from .models import LandTitleDetails

# class SearchDetails(models.Model):
#     land_id = models.AutoField(primary_key=True)
#     title_number = models.CharField(max_length=25)
#     owners_name = models.CharField(max_length=100)
#     Previous_owners_name = models.CharField(max_length=100)
#     property_address = models.CharField(max_length=255)
#     land_location = models.CharField(max_length=255)
#     parcel_number = models.CharField(max_length=50)
#     deed_type = models.CharField(max_length=50)
#     date_of_issue = models.DateField()
#     grantors = models.CharField(max_length=255)
#     property_size = models.CharField(max_length=50)
#     restrictions = models.CharField(max_length=255)
#     mortgage_information = models.CharField(max_length=255)
#     land_title_details = models.OneToOneField(LandTitleDetails, on_delete=models.CASCADE)
 

#     def __str__(self):
#         return f"{self.title_number}, {self.owners_name}"

