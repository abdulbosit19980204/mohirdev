from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.serializers import BookSerializer
from book.models import Book


class BookListAPIView(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        if not queryset:
            return Response(data={"error": "Book is not found", "ok": False}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


class BookDetailAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
