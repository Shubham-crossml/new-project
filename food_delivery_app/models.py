from django.db import models
from django.core.validators import MinValueValidator


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)

class client(models.Model):
    customer_image = models.ImageField(upload_to='customer_images/')
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=5000)
   
    

class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=200)
    customer_phone_number = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)

class TableBooking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    contact = models.CharField(max_length=20)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
