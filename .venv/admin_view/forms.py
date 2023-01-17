from django import forms
# from . models import Bouquet, Category
from sample_app.models import Product, Category

class BouquetForm(forms.ModelForm):
    remove = forms.BooleanField(
        required = False,
        widget = forms.CheckboxInput(
            attrs = {
                "id": "remove_img",
                "style": "display:none"
            }
        )
    )
    class Meta:
        model = Product
        fields = ['image', 'name', 'category', 'stock', 'price', 'desc'] 
        widgets = {
            'image': forms.FileInput(attrs={'id': 'img', 'onchange': 'getUrls(this);', 'class': 'form-control form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control mt-2'}),
        }