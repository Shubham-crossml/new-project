from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    # path('',food,name='food'),
    path('about/',about, name='about'),
    path('',home, name='home'),
    path('contact/',contact, name='contact'),
    path('book_table/',book_table, name='book_table'),
    path('restaurants/', restaurant_list, name='restaurant_list'),
    path('restaurants/create/', create_restaurant, name='create_restaurant'),
    path('menu-items/', menu_item_list, name='menu_item_list'),
    path('menu-items/create/', create_menu_item, name='create_menu_item'),
    path('orders/', order_list, name='order_list'),
    path('orders/create/', create_order, name='create_order'),
    path('table-bookings/', table_booking_list, name='table_booking_list'),
    path('table-bookings/create/',create_table_booking, name='create_table_booking'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='user_logout'),
    path('login/', user_login, name='user_login'),
    path('signup/', signup, name='signup'),
    path('signup/', user_signup, name='user_signup'),
    path('create-restaurant/',create_restaurant, name='create_restaurant'),
    path('menu-items/', menu_item_list, name='menu_item_list'),
    path('menu-items/create/', create_menu_item, name='create_menu_item'),
    path('orders/',order_list, name='order_list'),
    path('orders/create/', create_order, name='create_order'),
    path('table-bookings/create/',create_table_booking, name='create_table_booking'),
    path('table-bookings/',table_booking_list, name='table_booking_list'),
    path('send-email/', send_email_view, name='send_email'),
     path('order_now/', order_now, name='order_now'),
]

