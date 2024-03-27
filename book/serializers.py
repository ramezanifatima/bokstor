from rest_framework import serializers
from .models import Book, Profile, Purchase


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.make_author = validated_data.get('author', instance.make_author)
            instance.published_date = validated_data.get('published_date', instance.published_date)
            instance.price = validated_data.get('price', instance.price)
            instance.page_number = validated_data.get('page_number', instance.page_number)
            instance.age_category = validated_data.get('age_category', instance.age_category)
            instance.content = validated_data.get('content', instance.content)
            customer_data = validated_data.pop('customer', None)
            if customer_data:
                customer_id = customer_data.get('id')
                customer_instance = Profile.objects.get(pk=customer_id)
                instance.customer = customer_instance
            instance.save()
            return instance


class BookCustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['content']


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class RequestSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)

