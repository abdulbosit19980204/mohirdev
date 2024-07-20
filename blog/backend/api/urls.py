from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('', PostListAPIView.as_view(), name='post-list'),
]
