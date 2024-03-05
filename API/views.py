from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import mixins
from . models import Customer, Book
from .serializers import CustomersSerializers, BookSerializers, BookCustomerSerializers
from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        book_id = view.kwargs['pk']
        if request.user.is_authenticated:
            if Book.objects.filter(pk = book_id,customer=request.user):
                BookViewsets.serializer_class=BookCustomerSerializers
                return True
        return False


class BookViewsets(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet
                   ):
       queryset = Book.objects.all()
       serializer_class = BookSerializers
       permission_classes = [CustomPermission]