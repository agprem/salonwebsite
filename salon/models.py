from user.models import CustomUser
from django.db import models
import datetime
from django.utils import timezone
from user.models import CustomUser



# Create your models here.
class bookappointment(models.Model):
    service=models.CharField(max_length=20,verbose_name="Service/Package",blank=False)
    # pkgexp=models.DateField(default=datetime.date.today()+datetime.timedelta(days=60))
    technician=models.CharField(max_length=20,verbose_name="Technician")
    date=models.DateField(default=datetime.date.today(),blank=True,null=True)
    time=models.TimeField(default=timezone.now,blank=True,null=True)
    client= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    aptdone=models.BooleanField(default=False)
    price=models.IntegerField(default=0,blank=True,null=True)

    def __str__(self):
       return self.service


class seasonaloffers(models.Model):
    offercategory=models.CharField( default="Seasonal Offers",max_length=100,blank=True)
    offername=models.CharField(max_length=30)
    offerdetail=models.TextField(max_length=200,blank=True)
    offerimg=models.ImageField(default='default.jpg',upload_to='offer_pics')
    offerexp=models.DateField(default=datetime.date.today()+datetime.timedelta(days=60))
    price=models.IntegerField(blank=True)
    discount=models.IntegerField(blank=True)


    def __str__(self):
        return self.offername
    
    

class alltimeoffers(models.Model):
    offercategory=models.CharField(default="All Time Offers",max_length=100,blank=True)
    offername=models.CharField(max_length=30)
    offerdetail=models.TextField(max_length=200,blank=True)
    offerimg=models.ImageField(default='default.jpg',upload_to='offer_pics')
    offerexp=models.DateField(default=datetime.date.today()+datetime.timedelta(days=60))
    price=models.IntegerField(blank=True)
    discount=models.IntegerField(blank=True)


    def __str__(self):
        return self.offername


class otheroffers(models.Model):
    offercategory=models.CharField(default="Other Offers",max_length=100,blank=True)
    offername=models.CharField(max_length=30)
    offerdetail=models.TextField(max_length=200,blank=True)
    offerimg=models.ImageField(default='default.jpg',upload_to='offer_pics')
    offerexp=models.DateField(default=datetime.date.today()+datetime.timedelta(days=60))
    price=models.IntegerField(blank=True)
    discount=models.IntegerField(blank=True)


    def __str__(self):
        return self.offername


class discountoffers(models.Model):
    offercategory=models.CharField(default="Discount Offers",max_length=100,blank=True)
    offername=models.CharField(max_length=30)
    offerdetail=models.TextField(max_length=200,blank=True)
    offerimg=models.ImageField(default='default.jpg',upload_to='offer_pics')
    offerexp=models.DateField(default=datetime.date.today()+datetime.timedelta(days=60))
    price=models.IntegerField(blank=True)
    discount=models.IntegerField(blank=True)


    def __str__(self):
        return self.offername

class Products(models.Model):
    productname=models.CharField(max_length=100)
    productdetail=models.CharField(max_length=200,blank=True)
    productimg=models.ImageField(default='default.jpg',upload_to='product_pics')
    price=models.IntegerField(default=0,blank=True,null=True)
    discount=models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.productname


class CartItem(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    cartitem=models.ForeignKey(Products,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.cartitem}'

class Cart(models.Model):
    user= models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    items=models.ManyToManyField(CartItem)
    orderdate=models.DateTimeField(null=True,blank=True)
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.user.name