#posts/urls.py
from django.urls import path
from .views import (PostDetailViewAPI, 
                    PostListViewAPI, 
                    UserDetailViewAPI, 
                    UserListViewAPI,
                    PostViewSet, 
                    UserViewSet)
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls

# urlpatterns = [
#     path('<int:pk>/', PostDetailViewAPI.as_view(), name = 'detail'),
#     path('', PostListViewAPI.as_view(), name ='home'),
#     path('users/', UserListViewAPI.as_view(), name = 'users'),
#     path('users/<int:pk>', UserDetailViewAPI.as_view(), name = 'detailuser'),
    
# ]

