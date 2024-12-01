from django.db import models


# Collection model class

class Collection(models.Model):
    title = models.CharField(max_length=255)
    

# Product model class

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)


# Customer model class

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES=[
    (MEMBERSHIP_BRONZE, 'Bronze'),
    (MEMBERSHIP_SILVER ,'Silver'),
    (MEMBERSHIP_GOLD , 'Gold')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    birth_date = models.DateField(null= True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


# Order model class

class Order(models.Model):
    PAYMEN_STATUS_PENDING = 'P'
    PAYMEN_STATUS_COMPLETE = 'C'
    PAYMEN_STATUS_FAILED = 'F'

    STATUS_CHOICES = [
    (PAYMEN_STATUS_PENDING , 'Pending'),
    (PAYMEN_STATUS_COMPLETE , 'Complete'),
    (PAYMEN_STATUS_FAILED , 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PAYMEN_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


# Order Item model class

class Orderitem(models.Model):
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name=_(""), on_delete=models.Protect)


# Cart model class 

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


# Cart Item model class 

class Cartitem(models.Model):
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


# Adress model class 

class Adress(models.Model):
    street = 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
