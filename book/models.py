from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, related_name='profile')
    phone_number = models.CharField(max_length=11)
    age = models.PositiveIntegerField()
    is_author = models.BooleanField()

    def __str__(self):
        return self.user.username


class Book(models.Model):
    name = models.CharField(max_length=51)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='written_book')
    published_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    page_number = models.PositiveIntegerField()
    customer = models.ManyToManyField(Profile, related_name='purchased_books')
    age_category = models.PositiveIntegerField()
    content = models.TextField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, related_name='purchases', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
