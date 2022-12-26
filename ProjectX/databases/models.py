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
    # Role_Id=models.IntegerField(max_length=1,choices=roles)
    def __str__(self):
        return self.name

class Customer(models.Model):
    Username=models.CharField(max_length=100)
    Role_Id=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    Addr=models.TextField(max_length=500)
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    GST_no =models.IntegerField(primary_key=True)
    Role_Id=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    Addr=models.TextField(max_length=500)
    Mgr_name=models.CharField(max_length=100)
    Mgr_no=models.IntegerField()
    Descr=models.TextField()
    # Images=models.ImageField()
    def __str__(self):
        return self.name


class DeliveryAgent(models.Model):
    DL_no=models.IntegerField(primary_key=True,max_length=100)
    Role_Id=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    Location=models.CharField(max_length=100)
    License=models.ImageField()
    def __str__(self):
        return self.name

class Menu(models.Model):
    Name=models.CharField(max_length=100)
    Tag=models.CharField(max_length=100)
    Price=models.DecimalField(decimal_places=2,max_digits=7)
    GST_no=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    Photo=models.ImageField()
    def __str__(self):
        return self.name

class Cart(models.Model):
    Cust_Id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Food_Id=models.ForeignKey(Menu,on_delete=models.CASCADE)
    Amount = models.DecimalField(decimal_places=2,max_digits=7)
    Total_No_items=models.IntegerField()
    def __str__(self):
        return self.name



class Order(models.Model):
    status=(
        (1,"Order Accepted"),
        (2,"Out for Delivery"),
        (3,"Delivered"),
    )
    Cust_Id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Status= models.IntegerField(max_length=1,choices=status)
    def __str__(self):
        return self.name

class Payment(models.Model):
    status=(
        (1,"Paid"),
        (2,"Not paid"),
    )
    Cust_Id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Satus=models.IntegerField(max_length=1,choices=status)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

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
    Value=models.DecimalField(decimal_places=2,max_digits=7)
    def __str__(self):
        return self.name
    

