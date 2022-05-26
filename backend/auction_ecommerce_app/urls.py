from django.urls import path
from .views import ArticleView, AuctionView

urlpatterns = [
    path('articles/',ArticleView.article_list),
    path('articles/<int:pk>/',ArticleView.article_detail),
    path('articles/category/',ArticleView.article_list_by_category),
    path('articles/name/',ArticleView.article_list_by_name),
    path('articles/<int:pk>/auction',AuctionView.create_update_auction),
    path('articles/<int:pk>/endauction',AuctionView.end_auction)
]