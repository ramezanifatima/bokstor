from rest_framework import serializers
from .models import Book, Author, Customer

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CustomersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BookSerializers(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(),many=True)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),many=True)
    class Meta:
        model = Book
        fields = ['name','author','customer','price','page_number','age_category']

class BookCustomerSerializers(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(),many=True)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),many=True)
    class Meta:
        model = Book
        fields = '__all__'