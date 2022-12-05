from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model):
    roles=(
        (1,"Customer"),
        (2,"Restaurant"),
        (3,"Delivery Agent"),
    )
    email = models.EmailField(max_length=100,unique=True,primary_key=True)
    password= models.CharField(max_length=100)
    phone_no=models.IntegerField()
    Role_Id=models.IntegerField(max_length=1,choices=roles)

class Customer(models.Model):
    Username=models.CharField(max_length=100)
    Role_Id=models.ForeignKey(User,null=True)
    Addr=models.TextField(max_length=500)

class Restaurant(models.Model):
    GST_no =models.IntegerField(primary_key=True)
    Role_Id=models.ForeignKey(User,null=True)
    Addr=models.TextField(max_length=500)
    Mgr_name=models.CharField(max_length=100)
    Mgr_no=models.IntegerField()
    Descr=models.TextField()
    Images=models.ImageField()


class DeliveryAgent(models.Model):
    DL_no=models.IntegerField(primary_key=True,max_length=100)
    Role_Id=models.ForeignKey(User,null=True)
    Location=models.CharField(max_length=100)
    License=models.ImageField()

class Menu(models.Model):
    Name=models.CharField(max_length=100)
    Tag=models.CharField(max_length=100)
    Price=models.DecimalField()
    GST_no=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    Photo=models.ImageField()

class Cart(models.Model):
    Cust_Id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Food_Id=models.ForeignKey(Menu)
    Amount = models.DecimalField()
    Total_No_items=models.IntegerField()



class Order(model.Model):
    status=(
        (1,"Order Accepted"),
        (2,"Out for Delivery"),
        (3,"Delivered"),
    )
    Cust_Id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Status= models.IntegerField(max_length=1,choices=status)

class Payment(models.Model):
    status=(
        (1,"Paid"),
        (2,"Not paid"),
    )
    Cust_Id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Satus=models.IntegerField(max_length=1,choices=status)

""""
class Address(models.Model):
    Cust_Id = models.ForeignKey(Customer)
    Location = models.CharField(max_length=100)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['Cust_Id', 'Location'], name='unique_primary_key'),
        ]
"""

class Wallet(models.Model):
    Cust_Id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Value=models.DecimalField()
    

