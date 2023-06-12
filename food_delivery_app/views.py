from django.shortcuts import render, redirect
from .models import Restaurant, MenuItem, Order, TableBooking
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.http import HttpResponse
from groceries  import views

def food(request):
    return render(request, 'food.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')


def send_email_view(request):
    send_mail(
        'Subject',
        'Message body',
        'your-email@gmail.com',
        ['recipient@example.com'],
        fail_silently=False,
    )
    return render(request, 'template.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with the name of your home page URL pattern
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def book_table(request):
    return render(request, 'book_table.html')

@login_required
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

@staff_member_required
def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'create_restaurant.html', {'form': form})

def menu_item_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu_item_list.html', {'menu_items': menu_items})

@staff_member_required
def create_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_item_list')
    else:
        form = MenuItemForm()
    return render(request, 'create_menu_item.html', {'form': form})




def order_now(request):
    if request.method == 'POST':
        # Process the order form submission
        # Retrieve the form data and save the order
        # Redirect to a success page or perform further actions
        
        # Example:
        # order_form = OrderForm(request.POST)
        # if order_form.is_valid():
        #     order = order_form.save()
        #     return redirect('order_success')
        
        return HttpResponse('Order placed successfully!')
    else:
        # Render the order form template
        return render(request, 'order_now.html')



def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home view or URL pattern
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})


@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

@login_required
def table_booking_list(request):
    bookings = TableBooking.objects.all()
    return render(request, 'table_booking_list.html', {'bookings': bookings})

@login_required
def create_table_booking(request):
    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_booking_list')
    else:
        form = TableBookingForm()
    return render(request, 'create_table_booking.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home view or URL pattern
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the desired page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the desired page after login
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the desired page after logout


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})

def client_list(request):
    clients = client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})