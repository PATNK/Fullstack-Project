from django.db import models

# Create your models here.
#Product Information
class ProductInfo(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    sku = models.IntegerField()
    upc = models.IntegerField()
    manufacturer = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model_number = models.IntegerField()


def __str__(self):
       return f"{self.product_id} {self.product_name}"

#Inventory Details.
class InventoryDetails(models.Model):
    quantity_in_stock = models.IntegerField()
    reorder_level = models.IntegerField()
    reorder_quantity = models.IntegerField()
    safety_stock_level = models.IntegerField()
    leadtime = models.DateField()
    storage_location = models.CharField(max_length=100)
    batch_number = models.IntegerField()
    expiry_date = models.IntegerField()


def __str__(self):
       return self.quantity_in_stock

#Supplier Information
class SupplierInfo(models.Model):
    supplier_id = models.IntegerField()
    supplier_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    payment_terms = models.CharField(max_length=100)
    delivery_terms = models.CharField(max_length=100)
    supplier_rating = models.CharField(max_length=100)


def __str__(self):
       return f"{self.supplier_id} {self.supplier_name}"

#Pricing Details
class PricingDetails(models.Model):
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()
    discounts = models.IntegerField()


def __str__(self):
       return f"{self.cost_price} {self.selling_price}"

#Sales Information
class SalesInfo(models.Model):
    salesorder_id = models.IntegerField()
    customer_id = models.IntegerField()
    order_date = models.DateField()
    delivery_date = models.DateField()
    order_quantity = models.IntegerField()
    sales_channel = models.CharField(max_length=100)


def __str__(self):
       return f"{self.salesorder_id} {self.customer_id}"