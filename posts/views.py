from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics 
from .permissions import IsAuthorOrReadOnly
from .serializers import (PostSerializer, UserSerializer)
from .models import Post
from django.contrib.auth import get_user_model 

from rest_framework import viewsets # new


# Create your views here.
# This view is for read and create new Models
class PostListViewAPI(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailViewAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    
class UserListViewAPI(generics.ListCreateAPIView) :
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
class UserDetailViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset =   get_user_model().objects.all()
    serializer_class = UserSerializer      

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
