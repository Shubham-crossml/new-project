from django.contrib import admin
from .models import *

admin.site.register(Grocery)
admin.site.register(GroceryBooking)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)