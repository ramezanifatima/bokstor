from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from . models import Customer, Book
from .serializers import CustomersSerializers, BookSerializers


class CustomerListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializers

class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

