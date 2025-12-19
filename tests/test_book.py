import unittest
from unittest.mock import patch, MagicMock
from src.Book import Book

class TestBook(unittest.TestCase):

    def test_book_init(self):
        book = Book("Белоснежка", "Братья Гримм", 1674, "Сказка", 3456789)
        self.assertEqual(book.title, "Белоснежка")
        self.assertEqual(book.author, "Братья Гримм")
        self.assertEqual(book.genre, "Сказка")
        self.assertEqual(book.year, 1674)
        self.assertEqual(book.isbn, 3456789)
    
    def test_init_default_values(self):
        book = Book()
        
        self.assertEqual(book.title, "")
        self.assertEqual(book.author, "")
        self.assertEqual(book.year, 0)
        self.assertEqual(book.genre, "")
        self.assertEqual(book.isbn, 0)

    def test_random_book(self):
        with (patch('random.choice') as mock_choice,
             patch('random.randint') as mock_randint):
            
            mock_choice.side_effect = ["Случайная книга", "Случайный автор", "Фантастика"]
            mock_randint.side_effect = [1999, 987654]

            book = Book()
            book.random_book()
        
            self.assertEqual(book.title, "Случайная книга")
            self.assertEqual(book.author, "Случайный автор")
            self.assertEqual(book.year, 1999)
            self.assertEqual(book.genre, "Фантастика")
            self.assertEqual(book.isbn, 987654)
        
            self.assertEqual(mock_choice.call_count, 3)
            self.assertEqual(mock_randint.call_count, 2)