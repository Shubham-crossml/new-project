from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'phone_number', 'rating')

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('restaurant', 'name', 'price', 'rating')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('menu_item', 'quantity', 'customer_name', 'customer_address', 'customer_phone_number', 'rating')

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ('name', 'date', 'time', 'guests', 'contact', 'comments')


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    

class ClientForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ['customer_image', 'name', 'message']