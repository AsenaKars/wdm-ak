from django.forms import ModelForm
from .models import Order
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class Order_Form(ModelForm):
    class Meta:
        model = Order
        fields = ['customerID', 'order_productID', 'status', 'total']


class Create_User_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



