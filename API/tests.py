import json

from .models import Book, Profile, User

from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase


def UserFactory():
    return baker.make('User')


def author():
    user = UserFactory()
    return baker.make('Profile', user=user, is_author=True)


def profile():
    user = UserFactory()
    return baker.make('Profile', user=user)


class BaseTestCase(APITestCase):
    def setUp(self):
        self.author = author()
        self.customer = profile()
        self.unauthorized_user = profile()
        self.book_1 = baker.make('Book', customer=[self.customer], author=self.author)


class BookAPItest(BaseTestCase):
    def test_list_book_author(self):
        url = "http://127.0.0.1:8000/Book/"
        self.client.login(username=self.author.user.username, password=self.author.user.password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_book_customer(self):
        url = "http://127.0.0.1:8000/Book/"
        self.client.login(username=self.customer.user.username, password=self.customer.user.password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_book_normal(self):
        url = "http://127.0.0.1:8000/Book/"
        self.client.login(username=self.unauthorized_user.user.username, password=self.unauthorized_user.user.password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book_author(self):
        breakpoint()
        url = f"http://127.0.0.1:8000/{self.book_1.id}"
        self.client.force_login(self.author)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book_customer(self):
        url = f"http://127.0.0.1:8000/{self.book_1.id}"
        self.client.force_login(self.customer)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book_unauthorized_user(self):
        url = f"http://127.0.0.1:8000/{self.book_1.id}"
        self.client.force_login(self.unauthorized_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


















# class BookListViewTestCase(BaseTestCase):
#     def setUp(self):
#         super().setUp()
#         self.book_1 = baker.make('Book', author=self.profile)
#         self.book_2 = baker.make(Book, author=self.profile)
#
#     def test_book_list_view(self):
#         url = "http://127.0.0.1:8000/Book/"
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#         data = response.json()
#         book1 = BookSerializers(self.book_1)
#         book2 = BookSerializers(self.book_2)
#         self.assertContains(data, book1)
#         self.assertContains(data, book2)
#         self.assertEqual(len(data), 2)
#
#
# class BookRetrieveTestCase(BaseTestCase):
#     def setUp(self):
#         super().setUp()
#         print(f'profile:{self.profile}')
#         self.profile_a = author()
#         self.user_1 = UserFactory()
#         self.profile_1 = baker.make('Profile', user=self.user_1, is_author=False)
#         self.book_1 = baker.make('Book', author=self.profile_a, customer=[self.profile, ])
#         self.client = APIClient()
#
#     def test_user_permissions(self):
#         breakpoint()
#         url = f"http://127.0.0.1:8000/{self.book_1.id}"
#
#         self.client.force_login(self.profile)
#         response_c = self.client.get(url)
#
#         self.client.force_login(self.profile_a)
#         response_a = self.client.get(url)
#         self.assertEqual(response_c.status_code, 200)
#         self.assertEqual(response_a.status_code, 200)
#
#     def test_user_unauthorized(self):
#         url = f"http://127.0.0.1:8000/{self.book_1.id}"
#         client = APIClient()
#         client.login(username=self.profile_1.user.username, password=self.profile_1.user.password)
#         response = client.get(url)
#         self.assertEqual(response.status_code, 404)
