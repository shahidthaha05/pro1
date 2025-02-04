

# forms.py
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [ 'name', 'email', 'phone_number', 'shipping_address']


from .models import Product, Size

class ProductForm(forms.ModelForm):
    sizes = forms.ModelMultipleChoiceField(
        queryset=Size.objects.all(),
        widget=forms.CheckboxSelectMultiple  # Show as checkboxes
    )

    class Meta:
        model = Product
        fields = ['pro_id', 'name', 'base_price', 'offer_price', 'img', 'dis', 'sizes', 'quantity']



