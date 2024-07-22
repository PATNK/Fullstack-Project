from django import forms
from .models import ProductInfo
from .models import InventoryDetails
from .models import SupplierInfo
from .models import PricingDetails
from .models import SalesInfo

class ProductInfoForm(forms.ModelForm):
    class Meta:
        model = ProductInfo
        fields = ['product_id', 'product_name', 'description', 'category', 'sub_category', 'sku', 'upc', 'manufacturer', 'brand', 'model_number']

class InventoryDetailsForm(forms.ModelForm):
    class Meta:
        model = InventoryDetails
        fields = ['quantity_in_stock', 'reorder_level', 'reorder_quantity', 'safety_stock_level', 'leadtime', 'storage_location', 'batch_number', 'expiry_date']

class SupplierInfoForm(forms.ModelForm):
    class Meta:
        model = SupplierInfo
        fields = ['supplier_id', 'supplier_name', 'contact_info', 'payment_terms', 'delivery_terms', 'supplier_rating']

class PricingDetailsForm(forms.ModelForm):
    class Meta:
        model = PricingDetails
        fields = ['cost_price', 'selling_price', 'discounts']

class SalesInfoForm(forms.ModelForm):
    class Meta:
        model = SalesInfo
        fields = ['salesorder_id', 'customer_id', 'order_date', 'delivery_date', 'order_quantity', 'sales_channel']

