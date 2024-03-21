from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status

from .models import Profile, Book
from .serializers import BookSerializers, ProfileSerializer, BookCustomerSerializers


class BookViewsets(GenericViewSet):
    queryset = Book.objects.defer('content')
    serializer_class = BookCustomerSerializers

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        print(self.queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        user = request.user.profile
        user_status = user.purchased_books.filter(pk=pk).exists() or user.written_book.filter(pk=pk).exists()

        if user_status:
            serializer = BookSerializers(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'massage': 'your can not by in book!!'}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        user = request.user.profile
        if user.written_book.filter(pk=pk).exists():
            serializer = self.get_serializer(book, data=request.data)
            if serializer.is_valid(raise_exeption=True):
                serializer.update(book, request.data)
                return Response(serializer.data)
        else:
            return Response({'massage': 'your can not update that book!!'}, status=status.HTTP_403_FORBIDDEN)
