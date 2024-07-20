from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from blog.models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = User.objects.all()
    serializer_class = UserSerializer
