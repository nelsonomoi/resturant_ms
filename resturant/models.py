# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    p_id=models.CharField(blank=False, null=False,max_lenght=10)
    pname=models.CharField(max_lenght=50)
    price=models.DecimalField(default=0,max_digits=6,decimal_places=2)
    desc=models.CharField(max_lenght=100)
        
    class Meta:
        verbose_name=['Product']

class Category(models.Model):
    p_id=models.ForeignKey(Product)
    cname=models.CharField(max_lenght=50)

class ProductImages(models.Model):
    p_id=models.ForeignKey(Product)
    pname=models.CharField(max_lenght=50)
    image=models.ImageField()

class Users(models.Model):
    id=models.CharField(max_lenght=10)
    userName=models.CharField(max_lenght=50)
    password=models.CharField()
    email=models.EmailField()
    address=models.CharField(max_lenght=100)
    role=models.CharField(max_lenght=50)

class UsersPayments(models.Model):
    paymentId=models.CharField(max_lenght=10)
    paymentType=models.CharField(max_lenght=50)
    userId=models.ForeignKey(Users)
    securityCode=models.CharField(max_lenght=50)
    ExpiaryDate=models.DateField()
    cardType=models.CharField(max_lenght=50)
    cardHolderName=models.CharField(max_lenght=50)

class UserOrders(models.Model):
    userId=models.ForeignKey(Users)
    paymentId=models.ForeignKey(UsersPayments)
    orderOn=models.CharField(max_lenght=50)
    orderId=models.CharField(max_lenght=50)
    orderTime=models.TimeField()