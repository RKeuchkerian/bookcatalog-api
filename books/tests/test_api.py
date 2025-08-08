from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.book_data = {
            "title": "1984",
            "author": "George Orwell",
            "isbn": "9780451524935",
            "published_date": "1949-06-08"
        }
        Book.objects.create(**self.book_data)

    def test_create_book(self):
        url = reverse('book-list')
        new_data = {
            "title": "Brave New World",
            "author": "Aldous Huxley",
            "isbn": "9780060850524",
            "published_date": "1932-01-01"
        }
        response = self.client.post(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_books_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_book(self):
        url = reverse('book-list')
        invalid_data = {
            "title": "",
            "author": "Unknown",
            "isbn": "",
            "published_date": "2020-01-01"
        }
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
