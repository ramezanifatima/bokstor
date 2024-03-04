from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from . models import Customer, Book
from .serializers import CustomersSerializers, BookSerializers, BookCustomerSerializers
from  rest_framework import viewsets
from rest_framework.decorators import action


class BookViewsets(viewsets.ViewSet):
    def list(self, request):
        if User.is_authenticated:
            queryset = Book.objects.all()
            serializer = BookCustomerSerializers(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Book.objects.all()
            serializer = BookSerializers(queryset,many=True)
            return Response(serializer.data)