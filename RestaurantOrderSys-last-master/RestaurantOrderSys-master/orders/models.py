from django.db import models
from datetime import datetime
import string
from django.contrib.auth.models import User
import secrets


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.FileField(default='default.jpg', upload_to='profile_photos')
    money = models.CharField(default="0", max_length=1000)

    def __str__(self):
        return f'{self.user.username} Profile'


class Category(models.Model):
    category_title = models.CharField(max_length=200)
    category_gif = models.CharField(max_length=200)
    category_description = models.TextField()  # make this the wysiwyg text field

    def __str__(self):
        # overriding the string method to get a good representation of it in string format
        return f"{self.category_title}"


class RegularPizza(models.Model):
    # example row :: 1 topping , 5.00 , 7.00
    pizza_choice = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)
    category_description = models.TextField()  # make this the wysiwyg text field

    def __str__(self):
        # overriding the string method to get a good representation of it in string format
        return f"Regular Pizza : {self.pizza_choice}"


class SicilianPizza(models.Model):
    # example row :: 1 topping , 5.00 , 7.00
    pizza_choice = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)
    category_description = models.TextField()  # make this the wysiwyg text field

    def __str__(self):
        # overriding the string method to get a good representation of it in string format
        return f"Sicilian Pizza : {self.pizza_choice}"


class Toppings(models.Model):
    # example row :: Pepperoni
    topping_name = models.CharField(max_length=200)

    def __str__(self):
        # overriding the string method to get a good representation of it in string format
        return f"{self.topping_name}"


class Hawka(models.Model):
    # example row :: meatball , 5.00 , 6.50
    hawka = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        # overriding the string method to get a good representation of it in string format
        return f"hawka : {self.hawka}"


class Pasta(models.Model):
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        # overriding the string method to get a good representation of it in string format
        return f"{self.dish_name}"


class Salad(models.Model):
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        # overriding the string method to get a good representation of it in string format
        return f"Salad : {self.dish_name}"


class UserOrder(models.Model):
    username = models.CharField(max_length=200)  # who placed the order
    order = models.TextField()  # this will be a string representation of the cart from localStorage
    price = models.DecimalField(max_digits=6, decimal_places=2)  # how much was the order
    time_of_order = models.DateTimeField(default=datetime.now, blank=True)
    token = models.TextField(default="A1")
    delivered = models.BooleanField()

    def __str__(self):
        # overriding the string method to get a good representation of it in string format
        return f"Order placed by  : {self.username} on {self.time_of_order.date()} at {self.time_of_order.time().strftime('%H:%M:%S')}"


class SavedCarts(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    cart = models.TextField()  # this will be a string representation of the cart from localStorage

    def __str__(self):
        # overriding the string method to get a good representation of it in string format
        return f"Saved cart for {self.username}"
