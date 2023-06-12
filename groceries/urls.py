from django.urls import path
from django.contrib import admin
from . import views

app_name = 'groceries'

urlpatterns = [
    path('groceries/', views.grocery_list, name='grocery_list'),
    path('groceries/<int:grocery_id>/', views.grocery_detail, name='grocery_detail'),
    path('groceries/<int:grocery_id>/book/', views.book_grocery, name='book_grocery'),
    path('groceries/<int:grocery_id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/<int:cart_item_id>/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('create_booking/', views.create_grocery_booking, name='create_grocery_booking'),
    
]