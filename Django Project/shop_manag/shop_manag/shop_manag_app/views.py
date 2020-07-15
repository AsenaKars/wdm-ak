from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

from .forms import Order_Form, Create_User_Form

from .filters import Order_Filter

from django.contrib import messages
#https://docs.djangoproject.com/en/3.0/ref/contrib/messages/

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
#for restricting access

from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@login_required(login_url='login')
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    customer_count = customers.count()
    orders_count = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    return render(request, 'shop_manag_app/dashboard.html', {'orders': orders, 'customers': customers, 'orders_count': orders_count, 'delivered': delivered, 'pending': pending})


@login_required(login_url='login')
def products(request):
    products = Product.objects.all()

    return render(request, 'shop_manag_app/products.html', {'products': products})


@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    #delivery_address = customer.delivery_address_set.all()
    #RESOURCE: https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/

    filter = Order_Filter(request.GET, queryset=orders)
    orders = filter.qs
    #orders is now refiltered

    return render(request, 'shop_manag_app/customer.html', {'customer': customer, 'orders': orders, 'order_count': order_count, 'filter': filter})


@login_required(login_url='login')
def create_order(request):
    form = Order_Form()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'shop_manag_app/form_create__order.html', {'form': form})


@login_required(login_url='login')
def update_order(request, pk):

    #preview the current selection on de update panel
    order = Order.objects.get(id=pk)
    form = Order_Form(instance=order)
    if request.method == 'POST':
        form = Order_Form(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'shop_manag_app/form_create__order.html', {'form': form})


@login_required(login_url='login')
def delete_order(request, pk):
    order = Order.objects.get(id=pk)

    #the action of deleting the order
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(request, 'shop_manag_app/form_delete__order.html', {'item': order})


def register_user(request):
    if request.user.is_authenticated:
    #property for restricting loged in users from accessing again the r/l pages
        return redirect('/')
    else:
        form = Create_User_Form()
        if request.method == 'POST':
            form = Create_User_Form(request.POST)
            if form.is_valid():
                form.save()

                user = form.cleaned_data.get('username')
                messages.success(request, 'An account was created for ' + user)
                #flash message when an account is succesfully made

                return redirect('login')
                #connecting the login page to the registration page when the registration is succesfull

        return render(request, 'shop_manag_app/register.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect')
        return render(request, 'shop_manag_app/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def user(request):
    return render(request, 'shop_manag_app/user.html')
