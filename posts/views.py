from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

# Create your views here.
class PostListViewAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


