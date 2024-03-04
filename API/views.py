from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from . models import Customer, Book
from .serializers import CustomersSerializers, BookSerializers, BookCustomerSerializers
from  rest_framework import viewsets
from rest_framework.decorators import action


class BookViewsets(viewsets.ViewSet):
        def list (self,request):
            queryset = Book.objects.all()
            serializer = BookSerializers(queryset,many=True)
            return Response(serializer.data)
        def retrieve(self,request,pk=None):
            if not request.user.is_authenticated:
                return Response({'massage':'pleas login!!'})
            product = Book.objects.get(pk=pk)
            customer = request.user.customer
            if customer.book.filter(pk=pk).exists():
                serializer = BookCustomerSerializers(product)
                return Response(serializer.data)
            else:
                return Response({'massage':"in mahsol baray shoma da dastres nist"})