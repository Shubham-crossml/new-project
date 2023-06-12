from django.shortcuts import render, redirect , get_object_or_404
from .models import *
from django.core.paginator import Paginator
from.forms import *



def format_date(value):
    return value

def grocery_list(request):
    groceries = Grocery.objects.all()
    paginator = Paginator(groceries, 10)  # Display 10 groceries per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'grocery_list.html', {'page_obj': page_obj})


def grocery_detail(request, grocery_id):
    grocery = Grocery.objects.get(id=grocery_id)
    return render(request, 'grocery_detail.html', {'grocery': grocery})


def book_grocery(request, grocery_id):
    if request.method == 'POST':
        # Handle form submission and create a grocery booking
        # You can access the form data using request.POST.get() method
        grocery = Grocery.objects.get(id=grocery_id)
        # Create GroceryBooking instance and save it
        # Redirect to the grocery list or show a success message

    else:
        grocery = Grocery.objects.get(id=grocery_id)
        return render(request, 'book_grocery.html', {'grocery': grocery})



def create_grocery_booking(request):
    if request.method == 'POST':
        form = GroceryBookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Perform any additional logic or redirect to a success page
            return redirect('grocery_list')
    else:
        form = GroceryBookingForm()
    
    return render(request, 'create_grocery_booking.html', {'form': form})


def add_to_cart(request, grocery_id):
    if request.method == 'POST':
        # Handle form submission and add the grocery item to the user's cart
        # You can access the form data using request.POST.get() method
        grocery = Grocery.objects.get(id=grocery_id)
        # Add the grocery item to the user's cart using the add_item_to_cart() method
        # Redirect to the cart or show a success message

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')


def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    total_price = cart.total_price()
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})

def checkout(request):
    if request.method == 'POST':
        # Handle form submission and process the checkout
        # You can access the form data using request.POST.get() method
        # Create an Order instance and save it
        # Redirect to the order confirmation page or show a success message
        pass
    else:
        # Render the checkout page template
        pass


def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_detail.html', {'order': order})
