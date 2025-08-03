from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.book_data = {
            "title": "1984",
            "author": "George Orwell",
            "isbn": "9780451524935",
            "published_date": "1949-06-08"
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        url = reverse('book-list')  # viene del router de DRF
        new_data = {
            "title": "Brave New World",
            "author": "Aldous Huxley",
            "isbn": "9780060850524",
            "published_date": "1932-01-01"
        }
        response = self.client.post(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, "Brave New World")

    def test_get_books_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # solo el de setUp

    def test_create_invalid_book(self):
        url = reverse('book-list')
        invalid_data = {
            "title": "",
            "author": "Unknown",
            "isbn": "",  # inválido porque es obligatorio
            "published_date": "2020-01-01"
        }
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        updated_data = {
            "title": "1984 (Updated)",
            "author": "George Orwell",
            "isbn": self.book.isbn,
            "published_date": self.book.published_date
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "1984 (Updated)")

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

