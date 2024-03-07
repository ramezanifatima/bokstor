from rest_framework import serializers
from .models import Book, Profile



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

