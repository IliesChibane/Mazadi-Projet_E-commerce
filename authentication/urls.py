from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.Login_view.as_view()),
    path('logout/', views.Logout_view.as_view()),
    path('user/', views.User_view.as_view()),
]
