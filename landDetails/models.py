from django.db import models

class LandTitleDetails(models.Model):
    RESIDENTIAL = 'RES'
    COMMERCIAL = 'COM'
    INDUSTRIAL = 'IND'
    AGRICULTURAL = 'AGR'
    RECREATIONAL = 'REC'
    
    LAND_USE_CHOICES = [
        (RESIDENTIAL, 'Residential'),
        (COMMERCIAL, 'Commercial'),
        (INDUSTRIAL, 'Industrial'),
        (AGRICULTURAL, 'Agricultural'),
        (RECREATIONAL, 'Recreational'),
    ]

    # land_details = models.ForeignKey('SearchDetail', on_delete=models.CASCADE)
    parcel_number = models.CharField(max_length=50)
    ownership_type = models.CharField(max_length=255)
    property_address = models.CharField(max_length=255)
    land_use = models.CharField(
        max_length=10,
        choices=LAND_USE_CHOICES,
        default=RESIDENTIAL
    )
    date_surveyed = models.DateField()

    def __str__(self):
        return f"{self.land_use} ({self.parcel_number})"











# from django.db import models
# from .models import SearchDetails

# class LandTitleDetails(models.Model):
#     RESIDENTIAL = 'RES'
#     COMMERCIAL = 'COM'
#     INDUSTRIAL = 'IND'
#     AGRICULTURAL = 'AGR'
#     RECREATIONAL = 'REC'
    
#     LAND_USE_CHOICES = [
#         (RESIDENTIAL, 'Residential'),
#         (COMMERCIAL, 'Commercial'),
#         (INDUSTRIAL, 'Industrial'),
#         (AGRICULTURAL, 'Agricultural'),
#         (RECREATIONAL, 'Recreational'),
#     ]

#     land_details = models.ForeignKey(SearchDetails, on_delete=models.CASCADE)
#     parcel_number = models.CharField(max_length=50)
#     ownership_type = models.CharField(max_length=255)
#     property_address = models.CharField(max_length=255)
#     land_use = models.CharField(
#         max_length=10,
#         choices=LAND_USE_CHOICES,
#         default=RESIDENTIAL
#     )
#     date_surveyed = models.DateField()

# def __str__(self):
#     return f"{self.Land_use} ({self.parcel_number})"

