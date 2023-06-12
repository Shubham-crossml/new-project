from rest_framework import serializers
from .models import *
from groceries .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number', 'rating']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'restaurant', 'name', 'price', 'rating']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'menu_item', 'quantity', 'customer_name', 'customer_address', 'customer_phone_number', 'rating']


class TableBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableBooking
        fields = ['id', 'name', 'date', 'time', 'guests', 'contact', 'comments']



class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = ['id', 'image', 'name', 'price', 'quantity']


class GroceryBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryBooking
        fields = ['id', 'name', 'address', 'phone_number', 'item_name', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'grocery', 'quantity', 'customer_name', 'customer_address', 'customer_phone_number', 'rating']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'grocery', 'quantity', 'created_at']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'cart_items']