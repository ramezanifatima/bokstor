import json
from .models import Book, Profile
from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase



def make_user(username, email, password):
    user = User.objects.create_user(username=username, email=email, password=password)
    return user


def make_author():
    user = make_user(username='author', email='author@gmail.com', password='12345678')
    return baker.make('Profile', user=user, is_author=True)


def make_profile():
    user = make_user(username='profile', email='prof@gmail.com', password='12345678')
    return baker.make('Profile', user=user)


def make_unauthorized_user():
    user = make_user(username='unauthorized_user', email='unauthorized_user@gmail.com', password='12345678')
    return baker.make('Profile', user=user)


class BaseTestCase(APITestCase):
    def setUp(self):
        self.author = make_author()
        self.customer = make_profile()
        self.unauthorized_user = make_unauthorized_user()
        self.book_1 = baker.make('Book', customer=[self.customer], author=self.author)


class BookAPItest(BaseTestCase):
    def test_list_book_author(self):
        url = "http://127.0.0.1:8000/book/"
        self.client.force_login(self.author.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_book_customer(self):
        url = "http://127.0.0.1:8000/book/"
        self.client.force_login(self.customer.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_book_normal(self):
        url = "http://127.0.0.1:8000/book/"
        self.client.force_login(self.unauthorized_user.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book_author(self):
        url = f"http://127.0.0.1:8000/book/{self.book_1.id}/"
        self.client.force_login(self.author.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book_customer(self):
        url = f"http://127.0.0.1:8000/book/{self.book_1.id}/"
        self.client.force_login(self.customer.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book_unauthorized_user(self):
        url = f"http://127.0.0.1:8000/book/{self.book_1.id}/"
        self.client.force_login(self.unauthorized_user.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

