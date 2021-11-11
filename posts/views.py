from django.shortcuts import render
from rest_framework import generics 
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from .models import Post

# Create your views here.
class PostListViewAPI(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailViewAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer 


