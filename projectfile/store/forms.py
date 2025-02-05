from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]
    
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if Product.objects.filter(name=name).exists():
            raise forms.ValidationError("Product with this name already exists.")
        return name
