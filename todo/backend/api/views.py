from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework import status

from todo.models import Todo
from .serializers import ToDoSerializer


class TodoList(APIView):
    def get(self, request, format=None):
        queryset = Todo.objects.all()
        serializer = ToDoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
