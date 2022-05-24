from unicodedata import category
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from auction_ecommerce_app.models import Article
from auction_ecommerce_app.serializers import ArticleSerializer

class ArticleView(APIView):
    permission_classes=[AllowAny]

    @api_view(['GET', 'POST'])
    def article_list(request):
        if request.method == 'GET':
            article = Article.objects.all()
            article_serializer = ArticleSerializer(article, many=True)
            return JsonResponse(article_serializer.data, safe=False)
        
        elif request.method == 'POST':
            article_data = JSONParser().parse(request)
            article_serializer = ArticleSerializer(data=article_data)
            if article_serializer.is_valid():
                article_serializer.save()
                return JsonResponse(article_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'DELETE'])  
    def article_detail(request, pk):
        try: 
            article = Article.objects.get(pk=pk) 
        except Article.DoesNotExist: 
            return JsonResponse({'message': 'The article does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
        if request.method == 'GET': 
            article_serializer = ArticleSerializer(article) 
            return JsonResponse(article_serializer.data) 
    
        elif request.method == 'PUT': 
            article_data = JSONParser().parse(request) 
            article_serializer = ArticleSerializer(article, data=article_data) 
            if article_serializer.is_valid(): 
                article_serializer.save() 
                return JsonResponse(article_serializer.data) 
            return JsonResponse(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
        elif request.method == 'DELETE': 
            article.delete() 
            return JsonResponse({'message': 'article was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    @api_view(['POST'])
    def article_list_by_category(request):
        if request.method == 'POST': 
            c = request.data.get('category')
            print(c)
            article = Article.objects.filter(category=c)
            article_serializer = ArticleSerializer(article, many=True)
            return JsonResponse(article_serializer.data, safe=False)
