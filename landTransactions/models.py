from django.db import models

# Create your models here.
class LandTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)  
    parcel_id = models.ForeignKey('LandTitleDetails', on_delete=models.CASCADE) 
    seller_id = models.ForeignKey('LandSeller', on_delete=models.CASCADE, related_name='sales') 
    buyer_id = models.ForeignKey('LandBuyer', on_delete=models.CASCADE, related_name='purchases') 
    transaction_type = models.CharField(max_length=50)  
    transaction_date = models.DateField() 
    amount = models.IntegerField() 
    document_number = models.PositiveSmallIntegerField()  

    def __str__(self):
        return f"Transaction {self.amount} on {self.transaction_date}"













# from django.db import models
# from .models import LandSeller
# from .models import LandBuyer
# from .models import LandTitleDetails

# # Create your models here.
# class LandTransaction(models.Model):
#     transaction_id = models.AutoField(primary_key=True)  
#     parcel_id = models.ForeignKey('LandTitleDetails', on_delete=models.CASCADE) 
#     seller_id = models.ForeignKey('LandSeller', on_delete=models.CASCADE, related_name='sales') 
#     buyer_id = models.ForeignKey('LandBuyer', on_delete=models.CASCADE, related_name='purchases') 
#     transaction_type = models.CharField(max_length=50)  
#     transaction_date = models.DateField() 
#     amount = models.IntegerField() 
#     document_number = models.PositiveSmallIntegerField()  
#     def __str__(self):
#         return f"Transaction {self.amount} on {self.transaction_date}"
