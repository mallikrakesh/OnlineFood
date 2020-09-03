from django.db import models
from Myadmin.models import CityModel
from Vender.models import FoodItemsModel

# CUSTOMER MODULE

class CustomerRegistrationModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact = models.IntegerField(unique=True)
    address = models.TextField()
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    OTP = models.IntegerField()

class OrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    items = models.ManyToManyField(FoodItemsModel)
    quantity = models.IntegerField()
    total = models.FloatField()
    status = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    address = models.TextField()


class CustomerLoginModel(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField(default=1234)