from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import mixins
from . models import Customer, Book
from .serializers import CustomersSerializers, BookSerializers, BookCustomerSerializers
from rest_framework.permissions import BasePermission

class BookViewsets(GenericViewSet):
    queryset = Book.objects.all().defer('content')
    serializer_class = BookCustomerSerializers

    def list(self,request):
        serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        if not request.user.is_authenticated:
            return Response({'massage': 'pleas login!!'})
        book = Book.objects.get(pk=pk)
        customer = request.user.customer
        if customer.book.filter(pk=pk).exists():
            serializer = BookCustomerSerializers(book)
            return Response(serializer.data)
        else:
            return Response({'massage':'your can not by in book!!'})


