from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Grocery(models.Model):
    image = models.ImageField(upload_to='grocery_images')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class GroceryBooking(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    datetime = models.DateTimeField()
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Send email notification
        subject = 'Grocery Booking Confirmation'
        html_message = render_to_string('booking_email.html', {'booking': self})
        plain_message = strip_tags(html_message)
        from_email = 'your-email@example.com'  # Replace with the desired "from" email address
        to_email = self.email  # Replace with the recipient's email address
        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)


class Order(models.Model):
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=200)
    customer_phone_number = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)

    def calculate_total_price(self):
        return self.grocery.price * self.quantity

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_items(self):
        return self.cartitem_set.aggregate(total_items=Sum('quantity'))['total_items'] or 0

    def total_price(self):
        items = self.cartitem_set.all()
        total = sum(item.grocery.price * item.quantity for item in items)
        return total

    def add_item_to_cart(self, grocery_item, quantity):
        try:
            cart_item = self.cartitem_set.get(grocery=grocery_item)
            cart_item.quantity += quantity
            cart_item.save()
        except CartItem.DoesNotExist:
            CartItem.objects.create(cart=self, grocery=grocery_item, quantity=quantity)

    def get_paginated_items(self, page_number, items_per_page):
        items = self.cartitem_set.all()
        paginator = Paginator(items, items_per_page)

        try:
            paginated_items = paginator.page(page_number)
        except PageNotAnInteger:
            paginated_items = paginator.page(1)
        except EmptyPage:
            paginated_items = paginator.page(paginator.num_pages)

        return paginated_items


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
   
