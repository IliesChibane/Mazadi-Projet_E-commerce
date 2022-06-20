from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('owner','id', 'name', 'category', 'initial_price', "is_selled", "is_in_auction")

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ('id', 'best_price', 'actual_best_buyer', 'article', 'finish_at')