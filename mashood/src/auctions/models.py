from django.contrib.auth.models import AbstractUser
from django.db import models

import datetime


class User(AbstractUser):
    watchlist = models.ManyToManyField('AuctionListing')


class AuctionListing(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.FloatField()
    image = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.name) + str(self.created_by)

class Bids(models.Model):
    auction_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    offered_price = models.FloatField()
    time_created = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return str(self.name)

class Comments(models.Model):
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()