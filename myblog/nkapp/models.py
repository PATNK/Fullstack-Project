from django.db import models

# Create your models here.

class Prod(models.Model):
    prod_id = models.IntegerField()
    prod_name = models.CharField(max_length=100)
    #product_name = CharField(max_length=40)
    quantity = models.IntegerField()
    prod_category = models.CharField(max_length=50)
    #product_category = CharField(max_length=40)
    prod_price = models.IntegerField()
    restock_level = models.IntegerField()

def __str__(self):
       return self.prod_name

















