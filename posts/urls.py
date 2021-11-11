#posts/urls.py
from django.urls import path
from .views import (PostDetailViewAPI, PostListViewAPI)


urlpatterns = [
    path('<int:pk>/', PostDetailViewAPI.as_view(), name = 'detail'),
    path('', PostListViewAPI.as_view(), name ='home'),
]

