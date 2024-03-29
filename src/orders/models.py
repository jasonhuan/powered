# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random, string

from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import User
from profiles.models import Profile
from categories.models import OrderItem

from django.core.validators import RegexValidator


class Order(models.Model):
    #Customer is who it is being delivered to
    customer = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='customer')
    courier = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name='courier')

    delivery_address = models.CharField(max_length=100)

    #geo coordinates of delivery address?

    items = models.ManyToManyField(OrderItem)

    initial_delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    final_delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)


    #Order status: OP=open, IP=In progress, CL=closed
    order_status = models.CharField(max_length=2, default="OP")

    #1 to 5, representing star rating
    courier_rating = models.IntegerField(null=True, blank=True)

    order_time = models.DateTimeField(auto_now_add=True)
    acceptance_time = models.DateTimeField(null=True, blank=True)
    completion_time = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return str(self.customer) + " at " + str(self.order_time)


class OrderFeeAction(models.Model):

    user = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    was_counter_offer = models.BooleanField()
    is_final_fee = models.BooleanField(default = False)

    for_order = models.ForeignKey(Order)

    offer_made_time = models.DateTimeField(auto_now_add=True)

    #Accept time is only for counter offers, and is the time that the customer accepted it
    offer_accept_time = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return str(self.user) + " for " + str(self.for_order)

    