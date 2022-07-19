from django import forms
from apps.models import Order,Product

class OrderForm(forms.Form):        
    user_email = forms.CharField(label='Email', max_length=100)
    product = forms.ChoiceField(label='product',choices=tuple(Product.objects.values_list('id', 'name')))
    quatities = forms.IntegerField(label="Quantity")
    price = forms.IntegerField(label="Price")
        
