# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random, string

from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import User
from users.models import Profile

from django.core.validators import RegexValidator

class OrderPlace(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    #Geo coordinates?

    #Picture of icon

class OrderItem(models.Model):
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    #Where to get this item from
    place = models.ForeignKey(OrderPlace, on_delete=models.SET_NULL)


class Order(models.Model):
    #Customer is who it is being delivered to
    customer = models.OneToOneField(Profile, on_delete=models.SET_NULL)
    courier = models.OneToOneField(Profile, null=True, on_delete=models.SET_NULL)
    delivery_address = models.CharField(max_length=100)

    #Geo coordinates of delivery address?

    items = models.ManyToManyField(OrderItem, on_delete=models.SET_NULL)

    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    #Order status: OP=open, IP=In progress, CL=closed
    order_status = models.CharField(max_length=2, default="OP")

    #1 to 5, representing star rating
    courier_rating = models.IntegerField()

    order_time = models.DateTimeField(auto_now_add=True)
    completion_time = models.DateTimeField(null=True, blank=True)



    def __str__(self):
        return str(self.customer) + " at " + str(order_time)

    