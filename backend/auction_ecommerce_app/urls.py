from django.urls import path
from .views import ArticleView

urlpatterns = [
    path('articles/',ArticleView.article_list),
    path('articles/<int:pk>/',ArticleView.article_detail),
    path('articles/category/',ArticleView.article_list_by_category)
]