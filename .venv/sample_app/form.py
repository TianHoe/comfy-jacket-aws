from django import forms
from django.shortcuts import render

from order.models import Order

from .models import Product

class SampleForm(forms.ModelForm):
    name  = forms.CharField(label='Name', widget=forms.TextInput(attrs={"class": "flower_name", "placeholder": "Enter the flower name"}))
    stock = forms.IntegerField()
    price = forms.DecimalField(initial=10.00)

    class Meta:
        model = Product
        fields = [
            'name',
            'stock',
            'price'
        ]
    
    def clean_data(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        if not "flower" in name:
            return name
        else:
            raise forms.ValidationError("this is not a valid name")

class SampleRawForm(forms.Form):
    name  = forms.CharField(label='Flower Name', widget=forms.TextInput(attrs={"class": "flower_name", "placeholder": "Enter the flower name"}))
    stock = forms.IntegerField()
    price = forms.DecimalField(initial=10.00)

class PurchaseForm(forms.ModelForm):
    qty       = forms.IntegerField(label='', initial=0, widget=forms.NumberInput(attrs={"min": 0, "name": "flower_qty"}))
    subtotal  = forms.DecimalField(label='', initial=0.00, max_digits=6, decimal_places=2, disabled=True)
    
    class Meta:
        model = Order
        fields = [
            'qty',
            'subtotal'
        ]
    
    # def __init__(self, *args, **kwargs):
    #     product_obj = Product.objects.all()
    #     product = kwargs.pop('id', '')
    #     super(PurchaseForm, self).__init__(*args, **kwargs)
    #     self.fields['product'] = forms.ModelChoiceField(queryset=Product.objects.filter(id=1).values_list('id', flat=True))

