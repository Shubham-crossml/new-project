from django import forms
from .models import *

class GroceryBookingForm(forms.ModelForm):
    class Meta:
        model = GroceryBooking
        fields = ['name', 'address', 'phone_number', 'item_name', 'quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['grocery', 'quantity', 'customer_name', 'customer_address', 'customer_phone_number', 'rating']


class GroceryBookingForm(forms.ModelForm):
    class Meta:
        model = GroceryBooking
        fields = ['name', 'address', 'phone_number', 'item_name', 'quantity']
