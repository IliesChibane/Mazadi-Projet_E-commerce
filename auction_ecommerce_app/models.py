from pyexpat import model
from django.db import models
from authentication.models import User
from datetime import datetime, timedelta


class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    initial_price = models.IntegerField()
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to ='images/')
    owner = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    is_selled = models.BooleanField(default=False)
    is_in_auction = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['name','category','initial_price']

class Auction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    best_price = models.IntegerField()
    actual_best_buyer = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    finish_at = models.DateTimeField(default=(datetime.now() + timedelta(seconds=60)))
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    is_finnished = models.BooleanField(default=False)

