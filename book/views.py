from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework import mixins

from .models import Profile, Book
from .serializers import BookSerializers, ProfileSerializer, BookCustomerSerializers, PurchaseSerializer


class BookViewsets(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Book.objects.defer('content')
    serializer_class = BookCustomerSerializers

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        print(self.queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        book = Book.objects.filter(pk=pk).first()
        if book:
            user = request.user.profile
            user_status = user.purchased_books.filter(pk=pk).exists() or user.written_book.filter(pk=pk).exists()
            if user_status:
                serializer = BookSerializers(book)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'massage': 'your can not by in book!!'}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None, *args, **kwargs):
        book = Book.objects.get(pk=pk)
        user = request.user.make_profile
        if user.written_book.filter(pk=pk).exists():
            serializer = self.get_serializer(book, data=request.data)
            if serializer.is_valid(raise_exeption=True):
                serializer.update(book, request.data)
                return Response(serializer.data)
        else:
            return Response({'massage': 'your can not update that book!!'}, status=status.HTTP_403_FORBIDDEN)

    def post(self, request, pk=None, *args, **kwargs):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'massage': 'book DoesNotExists'}, status=status.HTTP_404_NOT_FOUND)
        quantity = request.data.get('q', 1)
        total_price = book.price * quantity
        purchase_data = {
            'product': book,
            'user': request.user.profile,
            'quantity': quantity,
            'total_price': total_price
        }

        serializer = PurchaseSerializer(data=purchase_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
