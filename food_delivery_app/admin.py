from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(TableBooking)
admin.site.register(client)

