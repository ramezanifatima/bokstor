from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Author (models.Model):
    name = models.CharField(max_length=50)


class Customer (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    age = models.PositiveIntegerField()


class Book (models.Model):
    name = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)
    published_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places= 2 )
    page_number = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True,related_name='book')
    age_category = models.PositiveIntegerField()
    content = models.TextField()

class By (models.Model):
    customer = models.ForeignKey(Customer,related_name='customer',on_delete=models.CASCADE)
    book = models.ForeignKey(Book,related_name='book',on_delete=models.CASCADE)


