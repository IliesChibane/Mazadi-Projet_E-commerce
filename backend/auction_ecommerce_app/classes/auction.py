from datetime import datetime, timedelta
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from auction_ecommerce_app.classes.auction import AuctionView
from auction_ecommerce_app.models import Article, Auction
from auction_ecommerce_app.serializers import ArticleSerializer, AuctionSerializer

class AuctionView(APIView):
    permission_classes=[AllowAny]

    def create_auction(auction_data):
        auction_serializer = AuctionSerializer(data=auction_data)
        if auction_serializer.is_valid():
            auction_serializer.save()
            return True
        return False

    @api_view(['POST', 'PUT'])
    def create_update_auction(request, pk):
        if request.method == 'POST': 
            auction = {}
            auction["best_price"] = request.data.get('best_price')
            auction["actual_best_buyer"] = request.data.get('actual_best_buyer')
            auction["article"] = pk
            if (AuctionView.create_auction(auction)):
                article = Article.objects.get(pk=pk) 
                article_serializer = ArticleSerializer(article, many=False)
                article_data = {
                    "owner": article_serializer.data.get('owner'),
                    "name": article_serializer.data.get('name'),
                    "category": article_serializer.data.get('category'),
                    "initial_price": article_serializer.data.get('initial_price'),
                    "is_in_auction": True
                }
                article_serializer = ArticleSerializer(article, data=article_data) 
                if article_serializer.is_valid(): 
                    article_serializer.save() 
                    return JsonResponse(article_serializer.data) 
                return JsonResponse(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            return JsonResponse("errors", status=status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'PUT':
            try: 
                auction = Auction.objects.get(article=pk) 
            except Auction.DoesNotExist: 
                return JsonResponse({'message': 'The auction does not exist'}, status=status.HTTP_404_NOT_FOUND) 
            og_auction_serializer = AuctionSerializer(auction, many=False) 
            
            auction_data = {
                "best_price" : request.data.get("best_price"),
                "actual_best_buyer" : request.data.get("actual_best_buyer"),
                "article" : pk,
                "finish_at" : (datetime.now() + timedelta(seconds=60))
            }
            if int(og_auction_serializer.data.get("best_price")) < int(request.data.get("best_price")):
                auction_serializer = AuctionSerializer(auction, data=auction_data) 
                if auction_serializer.is_valid(): 
                    auction_serializer.save() 
                    return JsonResponse(auction_serializer.data) 
                return JsonResponse(auction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse("a7chem 3la 3ardek", status=status.HTTP_400_BAD_REQUEST, safe=False)

    @api_view(['PUT'])
    def end_auction(request, pk):
        if request.method == 'PUT':
            try: 
                auction = Auction.objects.get(article=pk) 
            except Auction.DoesNotExist: 
                return JsonResponse({'message': 'The auction does not exist'}, status=status.HTTP_404_NOT_FOUND) 
            og_auction_serializer = AuctionSerializer(auction, many=False)
            try: 
                article = Article.objects.get(pk=pk) 
            except Article.DoesNotExist: 
                return JsonResponse({'message': 'The article does not exist'}, status=status.HTTP_404_NOT_FOUND)
            og_article_serializer = ArticleSerializer(article, many=False)

            t = og_auction_serializer.data.get('finish_at').replace("T", " ")
            print(str(datetime.now()))
            if t >= str(datetime.now()):
                new_article = {
                    "name" : og_article_serializer.data.get("name"),
                    "category" : og_article_serializer.data.get("category"),
                    "initial_price" : og_article_serializer.data.get("initial_price"),
                    "owner" : og_article_serializer.data.get("owner"),
                    "is_selled" : True,
                    "is_in_auction" : False
                }

                new_auction = {
                    "best_price" : og_auction_serializer.data.get("best_price"),
                    "actual_best_buyer" : og_auction_serializer.data.get("actual_best_buyer"),
                    "article" : pk,
                    "is_finnished" : True
                }

                auction_serializer = AuctionSerializer(auction, data=new_auction) 
                article_serializer = ArticleSerializer(article, data=new_article) 
                if auction_serializer.is_valid() and  article_serializer.is_valid(): 
                    auction_serializer.save() 
                    article_serializer.save()
                    return JsonResponse(auction_serializer.data) 
                return JsonResponse(auction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse("not yet", status=status.HTTP_400_BAD_REQUEST, safe=False)