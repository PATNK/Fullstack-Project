from django import forms
from .models import Prod

class ProdForm(forms.ModelForm):
    class Meta:
        model = Prod
        fields = ['prod_id', 'prod_name', 'quantity', 'prod_category', 'prod_price', 'restock_level']


         
