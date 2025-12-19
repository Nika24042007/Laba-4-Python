import unittest
from src.BookIndex import BookIndex
from src.Book import Book
from src.BookCollection import BookCollection
from unittest.mock import patch, MagicMock

class TestBookIndex(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Война и мир", "Лев Толстой", 1567, "Роман", 12345)
        self.book2 = Book("Анна Каренина", "Лев Толстой", 1678, "Роман", 67890)
        self.book3 = Book("Преступление и наказание", "Фёдор Достоевский", 1809, "Психология", 54321)
        self.book4 = Book("Идиот", "Фёдор Достоевский", 1899, "Роман", 98765)
        self.book5 = Book("1984", "Джордж Оруэлл", 1567, "Антиутопия", 45678)
        
        self.book_list = [self.book1, self.book2, self.book3, self.book4, self.book5]
    
    def test_dict_author(self):
        dict_a = BookIndex(self.book_list, "author")
        
        self.assertIn("Лев Толстой", dict_a)
        self.assertIn("Фёдор Достоевский", dict_a)
        self.assertIn("Джордж Оруэлл", dict_a)
        
        self.assertEqual(len(dict_a["Лев Толстой"]), 2)
        self.assertEqual(len(dict_a["Фёдор Достоевский"]), 2)
        self.assertEqual(len(dict_a["Джордж Оруэлл"]), 1)
        
        self.assertIn(self.book1, dict_a["Лев Толстой"])
        self.assertIn(self.book2, dict_a["Лев Толстой"])
        self.assertIn(self.book3, dict_a["Фёдор Достоевский"])
        self.assertIn(self.book4, dict_a["Фёдор Достоевский"])
        self.assertIn(self.book5, dict_a["Джордж Оруэлл"])
    
    def test_dict_year(self):
        dict_y = BookIndex(self.book_list, "year")

        self.assertIn(1567, dict_y)
        self.assertIn(1678, dict_y)
        self.assertIn(1809, dict_y)
        self.assertIn(1899, dict_y)
        
        self.assertEqual(len(dict_y[1567]), 2)  
        self.assertEqual(len(dict_y[1678]), 1) 
        self.assertEqual(len(dict_y[1809]), 1)  
        self.assertEqual(len(dict_y[1899]), 1)
    
    def test_dict_title(self):
        dict_t = BookIndex(self.book_list, "title")
        
        self.assertIn("Война и мир", dict_t)
        self.assertIn("Анна Каренина", dict_t)
        self.assertIn("Преступление и наказание", dict_t)
        self.assertIn("Идиот", dict_t)
        self.assertIn("1984", dict_t)
        
        self.assertEqual(len(dict_t["Война и мир"]), 1)
        self.assertEqual(dict_t["Война и мир"][0], self.book1)
    
    def test_dict_genre(self):
        dict_g = BookIndex(self.book_list, "genre")
        
        self.assertIn("Психология", dict_g)
        self.assertIn("Роман", dict_g)
        self.assertIn("Антиутопия", dict_g)
        
        self.assertEqual(len(dict_g ["Роман"]), 3) 
        self.assertEqual(len(dict_g ["Антиутопия"]), 1)
        self.assertEqual(len(dict_g ["Психология"]), 1)
    
    def test_dict_isbn(self):
        dict_i = BookIndex(self.book_list, "isbn")
        
        self.assertIn(12345, dict_i)
        self.assertIn(67890, dict_i)
        self.assertIn(54321, dict_i)
        self.assertIn(98765, dict_i)
        self.assertIn(45678, dict_i)
        
        self.assertEqual(len(dict_i[12345]), 1)
        self.assertEqual(dict_i[12345][0], self.book1)
    
    def test_update_index(self):
        books = [self.book1, self.book2]
        dict_two = BookIndex(books, "author")
        
        self.assertEqual(len(dict_two["Лев Толстой"]), 2)
        
        dict_two.update_index([self.book3])
        
        self.assertIn("Фёдор Достоевский", dict_two)
        self.assertNotIn("Лев Толстой", dict_two)
        self.assertEqual(len(dict_two["Фёдор Достоевский"]), 1)
    
    def test_str(self):
        b = BookIndex([self.book1, self.book2], "author")
        result = str(b)
        
        self.assertIn("Лев Толстой:", result)
        self.assertIn('"Война и мир"', result)
        self.assertIn('"Анна Каренина"', result)
        self.assertIn("1567", result)
        self.assertIn("1678", result)
    
    def test_empty(self):
        b = BookIndex([], "author")
        self.assertEqual(len(b), 0)
        result = str(b)
        self.assertEqual(result, "")
    
    def test_ucorrect_key(self):
        b = BookIndex(self.book_list, "key")
        self.assertEqual(len(b), 0)