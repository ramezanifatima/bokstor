from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status

from . models import Profile, Book
from .serializers import BookSerializers, ProfileSerializer

class BookViewsets(GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def list(self,request):
        serializer = self.get_serializer(self.queryset,many=True)
        print(self.queryset)
        return Response(serializer.data)


    def retrieve(self,request,pk=None):
        if not request.user.is_authenticated:
            return Response({'massage': 'pleas login!!'})
        book = Book.objects.get(pk=pk)
        user = request.user.profile
        if user.purchased_books.filter(pk=pk).exists() or user.written_book.filter(pk=pk).exists():
            serializer = self.get_serializer(book)
            return Response(serializer.data)
        else:
            return Response({'massage': 'your can not by in book!!'})

    def update(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        user = request.user.profile
        if user.written_book.filter(pk=pk).exists():
            serializer = self.get_serializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'massage': 'your can not update that book!!'},status=status.HTTP_403_FORBIDDEN)
