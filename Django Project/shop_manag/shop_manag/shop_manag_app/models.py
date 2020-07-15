from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Delivery_Address(models.Model):
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    other = models.CharField(max_length=200, null=True)


    def __str__(self):
        return '%s, %s, %s, %s' %(self.country,self.city, self.postal_code, self.other)
        #source: https://stackoverflow.com/questions/41153261/using-str-to-return-a-variable-number-of-different-lined-strings


class Customer(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    #profile_pic
    #
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    delivery_address = models.ManyToManyField(Delivery_Address)
    #orderID??


    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)


class Product(models.Model):
    TAGS = (
        ('Book', 'Book'),
        ('E-book', 'E-book'),
        ('DVD', 'DVD'),
        ('Vinyl', 'Vinyl'),
        ('Map', 'Map'),
        ('Painting', 'Painting'),
        ('Decoration', 'Decoration'),
    )
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    tag = models.CharField(max_length=100, choices=TAGS, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return '%s | %s - %s' %(self.tag, self.name, self.description)


class Order_Product(models.Model):
    price = models.FloatField(null=True)
    quantity = models.IntegerField()
    #
    productID = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    #orderID??


    def __str__(self):
       return '%s - %f' %(self.productID, self.price)


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
    )
    total = models.FloatField()
    status = models.CharField(max_length=100, choices=STATUS, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    #Find a way to (errorless) format the date_created var
    #
    customerID = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    order_productID = models.ManyToManyField(Order_Product)


    def __str__(self):
       return '%s - %s | %.2f ' %(self.status, self.date_created, self.total)


class Payment(models.Model):
    cc_no = models.CharField(max_length=100, null=True)
    cc_expiry = models.DateField()
    #I should probably have custom DateField() in MM/YY format, CharField with some encription?
    cc_code = models.CharField(max_length=100, null=True)
    billing_address = models.CharField(max_length=200, null=True)
    #
    customerID = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)

