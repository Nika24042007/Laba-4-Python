import unittest
from unittest.mock import patch, MagicMock
from src.BookCollection import BookCollection
from src.Book import Book


class TestBookCollection(unittest.TestCase):
    def setUp(self):
        self.collection = BookCollection()
    
    def test_init_collection(self):
        self.assertEqual(len(self.collection), 0)
    
    def test_add_random_book_adds_book(self):
        mock_book = MagicMock()
        mock_book.random_book.return_value = mock_book
        
        with patch('src.BookCollection.Book', return_value=mock_book):
            self.collection.add_random_book()
            self.assertEqual(len(self.collection), 1)
            self.assertEqual(self.collection[0], mock_book)
            mock_book.random_book.assert_called_once()

    def test_add_two_random_books(self):
        mock_book = MagicMock()
        mock_book.random_book.return_value = mock_book
        
        with patch('src.BookCollection.Book', return_value=mock_book):
            self.collection.add_random_book()
            self.collection.add_random_book()
            self.assertEqual(len(self.collection), 2)
            self.assertEqual(self.collection[0], mock_book)
            self.assertEqual(self.collection[1], mock_book)
            mock_book.random_book.assert_called()
    
    def test_str_empty(self):
        result = str(self.collection)
        self.assertEqual(result, "Коллекция книг пуста")

    def test_str_books_in_collection(self):
        book1 = Book("Война и мир", "Толстой", 1809, "Роман", 123456)
        book2 = Book("Анна Каренина", "Толстой", 1777, "Роман", 78901)
        
        self.collection.append(book1)
        self.collection.append(book2)
        
        result = str(self.collection)
        
        self.assertIn("Коллекция книг:", result)
        self.assertIn('"Война и мир"', result)
        self.assertIn('"Анна Каренина"', result)
        self.assertIn("Толстой", result)
        self.assertIn("1809", result)
        self.assertIn("1777", result)
        self.assertIn("123456", result)
        self.assertIn("78901", result)

    def test_getitem_format(self):
        book = Book("Название", "Автор", 2025, "Жанр", 123456)
        self.collection.append(book)

        result = self.collection.getiem_format(0)

        self.assertIn('"Название"', result)
        self.assertIn("Автор", result)
        self.assertIn("2025", result)
        self.assertIn("Жанр", result)
        self.assertIn("123456", result)

    def test_getitem_format_slice(self):
        book1 = Book("Война и мир", "Толстой", 1809, "Роман", 123456)
        book2 = Book("Анна Каренина", "Толстой", 1777, "Роман", 78901)
        
        self.collection.append(book1)
        self.collection.append(book2)

        result = self.collection.getiem_format(slice(0,1))

        self.assertIn('"Война и мир"', result)
        self.assertIn('"Анна Каренина"', result)
        self.assertIn("Толстой", result)
        self.assertIn("1809", result)
        self.assertIn("1777", result)
        self.assertIn("123456", result)
        self.assertIn("78901", result)