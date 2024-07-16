from django.urls import path
from .views import BookListAPIView, BookDetailAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='index'),
    path('books/', BookDetailAPIView.as_view(), name='books'),
]
