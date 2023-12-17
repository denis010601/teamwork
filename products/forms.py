from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'volume', 'packaging', 'netto', 'brutto', 'delivery', 'minimal_order', 'barcode', 'pcs_truck', 'pallets_truck', 'cases_truck', 'gross_weight', 'description', 'date_add', 'created_by']
        widgets = {
            'delivery': forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY'}),
            'date_add': forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY'}),
        }
