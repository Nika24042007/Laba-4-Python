import unittest
from unittest.mock import patch, MagicMock
from src.Liblary import Liblary
from src.BookCollection import BookCollection
from src.BookIndex import BookIndex
from src.Book import Book

class TestLiblary(unittest.TestCase):
    def setUp(self):
        self.liblary = Liblary()

    def test_liblary_creation(self):
        with (patch('src.Liblary.BookCollection') as mock_collection_book,
             patch('src.Liblary.BookIndex') as mock_index_book):
            
            mock_collection = MagicMock()
            mock_collection_book.return_value = mock_collection
            
            mock_index = MagicMock()
            mock_index_book.return_value = mock_index
            
            liblary = Liblary()
            
            mock_collection_book.assert_called_once()
            self.assertEqual(mock_index_book.call_count, 5)
            self.assertEqual(liblary.bookcol, mock_collection)

    def test_update_indexs(self):
            self.liblary.bookisbn.update_index = MagicMock()
            self.liblary.bookyear.update_index = MagicMock()
            self.liblary.bookauthor.update_index = MagicMock()
            self.liblary.bookgenre.update_index = MagicMock()
            self.liblary.booktitle.update_index = MagicMock()
        
            self.liblary.updata_indexs()

            self.liblary.bookisbn.update_index.assert_called_once_with(self.liblary.bookcol)
            self.liblary.bookyear.update_index.assert_called_once_with(self.liblary.bookcol)
            self.liblary.bookauthor.update_index.assert_called_once_with(self.liblary.bookcol)
            self.liblary.bookgenre.update_index.assert_called_once_with(self.liblary.bookcol)
            self.liblary.booktitle.update_index.assert_called_once_with(self.liblary.bookcol)
        
    def test_add_random(self):

        self.liblary.bookcol.add_random_book = MagicMock()
        self.liblary.updata_indexs = MagicMock()

        self.liblary.add_random()

        self.liblary.bookcol.add_random_book.assert_called_once()
        self.liblary.updata_indexs.assert_called_once()

    def test_add(self):
        book_list = ["Отцы и дети", "Тургенеев", "Роман", 1876, 123456]
        self.liblary.bookcol.append = MagicMock()
        self.liblary.updata_indexs = MagicMock()

        with patch('src.Liblary.Book') as MockBook:
            mock_book_instance = MagicMock()
            MockBook.return_value = mock_book_instance
        
            self.liblary.add(book_list[0], book_list[1], book_list[2], book_list[3], book_list[-1])
        
            MockBook.assert_called_once_with(book_list[0], book_list[1], book_list[3], book_list[2], book_list[-1])
    
            self.liblary.bookcol.append.assert_called_once_with(mock_book_instance)
            self.liblary.updata_indexs.assert_called_once()

    def test_del(self):
        
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)
        
        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)
        
        self.liblary.updata_indexs = MagicMock()
        
        result = self.liblary.del_book(1)
        
        expected = '"Книга 2" - Автор 2 (2005), Жанр 2, ISBN: 222222'
        self.assertEqual(result, expected)
        
        self.assertEqual(len(self.liblary.bookcol), 2)
        self.assertEqual(self.liblary.bookcol[0], book1)
        self.assertEqual(self.liblary.bookcol[1], book3)
        
        self.liblary.updata_indexs.assert_called_once()

    def test_del_empty(self):
        result = self.liblary.del_book(0)
        self.assertEqual(result, "Empty")

    def test_del_error(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)
        
        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)
        
        with self.assertRaises(IndexError):
            self.liblary.del_book(9)

    def test_del_random(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.updata_indexs = MagicMock()

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        result = self.liblary.del_random()
        expected = '"Книга 2" - Автор 2 (2005), Жанр 2, ISBN: 222222, "Книга 1" - Автор 1 (2000), Жанр 1, ISBN: 111111, "Книга 3" - Автор 3 (2010), Жанр 3, ISBN: 333333'
        self.assertIn(result, expected)
        self.liblary.updata_indexs.assert_called_once()

    def test_del_random_empty(self):
        result = self.liblary.del_random()
        self.assertEqual(result, "Empty")

    def test_find_del_empty(self):
        result = self.liblary.find_del_author_title("Булгаков", "Мастер и Маргарита")
        self.assertEqual(result, "Empty")

    def test_find_del_error(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        with self.assertRaises(KeyError):
            self.liblary.find_del_author_title("Автор 1", "Книга 2")

    def test_find_del(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        self.liblary.updata_indexs = MagicMock()

        result = self.liblary.find_del_author_title("Автор 1", "Книга 1")
        expected = '"Книга 1" - Автор 1 (2000), Жанр 1, ISBN: 111111'
        
        self.assertEqual(result, expected)
        self.assertEqual(len(self.liblary.bookcol), 2)
        self.assertNotIn(book1, self.liblary.bookcol)
        self.assertIn(book2, self.liblary.bookcol)
        self.assertIn(book3, self.liblary.bookcol)
        self.liblary.updata_indexs.assert_called_once()

    def test_change_title(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()
        self.liblary.updata_indexs = MagicMock()

        result = self.liblary.change(0, "title", "Новая книга 1")

        self.assertEqual(result, "Book change")
        self.assertEqual(self.liblary.bookcol[0].title,  "Новая книга 1")
        self.liblary.updata_indexs.assert_called_once()

    def test_change_author(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()
        self.liblary.updata_indexs = MagicMock()

        result = self.liblary.change(0, "author", "Новый автор 1")

        self.assertEqual(result, "Book change")
        self.assertEqual(self.liblary.bookcol[0].author,  "Новый автор 1")
        self.liblary.updata_indexs.assert_called_once()

    def test_change_genre(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()
        self.liblary.updata_indexs = MagicMock()

        result = self.liblary.change(0, "genre", "Новый жанр 1")

        self.assertEqual(result, "Book change")
        self.assertEqual(self.liblary.bookcol[0].genre,  "Новый жанр 1")
        self.liblary.updata_indexs.assert_called_once()

    def test_change_year(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()
        self.liblary.updata_indexs = MagicMock()

        result = self.liblary.change(0, "year", 1000)

        self.assertEqual(result, "Book change")
        self.assertEqual(self.liblary.bookcol[0].year,  1000)
        self.liblary.updata_indexs.assert_called_once()

    def test_change_isbn(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()
        self.liblary.updata_indexs = MagicMock()

        result = self.liblary.change(0, "isbn", 1)

        self.assertEqual(result, "Book change")
        self.assertEqual(self.liblary.bookcol[0].isbn,  1)
        self.liblary.updata_indexs.assert_called_once()

    def test_change_empty(self):
        result = self.liblary.change(0, "isbn", 123)
        self.assertEqual(result, "Empty")

    def test_change_index_error(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        with self.assertRaises(IndexError):
            self.liblary.change(10, "isbn", 123)

    def test_change_no_argument_error(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        with self.assertRaises(ValueError):
            self.liblary.change(1, "key", 123)

    @patch("random.randint")
    def test_change_title_random(self, mock_randit):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()
        self.liblary.updata_indexs = MagicMock()
        mock_randit.return_value = 0

        result = self.liblary.change_random("title", "Новая книга 1")

        mock_randit.assert_called_once()
        self.assertEqual(result, "Book change")
        self.assertEqual(self.liblary.bookcol[0].title,  "Новая книга 1")
        self.liblary.updata_indexs.assert_called_once()

    @patch("random.randint")
    def test_change_author_random(self,mock_randit):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()
        self.liblary.updata_indexs = MagicMock()
        mock_randit.return_value = 0

        result = self.liblary.change_random("author", "Новый автор 1")

        mock_randit.assert_called_once()
        self.assertEqual(result, "Book change")
        self.assertEqual(self.liblary.bookcol[0].author,  "Новый автор 1")
        self.liblary.updata_indexs.assert_called_once()

    @patch("random.randint")
    def test_change_genre_random(self,mock_randit):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()
        self.liblary.updata_indexs = MagicMock()
        mock_randit.return_value = 0

        result = self.liblary.change_random("genre", "Новый жанр 1")

        mock_randit.assert_called_once()
        self.assertEqual(result, "Book change")
        self.assertEqual(self.liblary.bookcol[0].genre,  "Новый жанр 1")
        self.liblary.updata_indexs.assert_called_once()

    @patch("random.randint")
    def test_change_year_random(self,mock_randit):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()
        self.liblary.updata_indexs = MagicMock()
        mock_randit.return_value = 0

        result = self.liblary.change_random("year", 1000)

        mock_randit.assert_called_once()
        self.assertEqual(result, "Book change")
        self.assertEqual(self.liblary.bookcol[0].year,  1000)
        self.liblary.updata_indexs.assert_called_once()

    @patch("random.randint")
    def test_change_isbn_random(self,mock_randit):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()
        self.liblary.updata_indexs = MagicMock()
        mock_randit.return_value = 0

        result = self.liblary.change_random("isbn", 1)

        mock_randit.assert_called_once()
        self.assertEqual(result, "Book change")
        self.assertEqual(self.liblary.bookcol[0].isbn,  1)
        self.liblary.updata_indexs.assert_called_once()

    def test_change_empty_random(self):
        result = self.liblary.change_random("isbn", 123)
        self.assertEqual(result, "Empty")

    def test_find_author(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        result = self.liblary.find_author("Автор 1")
        expected = '"Книга 1" - Автор 1 (2000), Жанр 1, ISBN: 111111'

        self.assertEqual(result, expected)

    def test_find_author_empty(self):
        result = self.liblary.find_author("dfsdf")
        self.assertEqual(result, "Empty")

    def test_find_author_error(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        with self.assertRaises(KeyError):
            self.liblary.find_author("Автор 5")

    def test_find_isbn(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        result = self.liblary.find_isbn(111111)
        expected = '"Книга 1" - Автор 1 (2000), Жанр 1, ISBN: 111111'

        self.assertEqual(result, expected)

    def test_find_isbn_empty(self):
        result = self.liblary.find_isbn(111111)
        self.assertEqual(result, "Empty")

    def test_find_isbn_error(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        with self.assertRaises(KeyError):
            self.liblary.find_isbn(555555)

    def test_find_year(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        result = self.liblary.find_year(2000)
        expected = '"Книга 1" - Автор 1 (2000), Жанр 1, ISBN: 111111'

        self.assertEqual(result, expected)

    def test_find_year_empty(self):
        result = self.liblary.find_year(2000)
        self.assertEqual(result, "Empty")

    def test_find_year_error(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        with self.assertRaises(KeyError):
            self.liblary.find_year(2025)

    def test_find_title(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        result = self.liblary.find_title("Книга 1")
        expected = '"Книга 1" - Автор 1 (2000), Жанр 1, ISBN: 111111'

        self.assertEqual(result, expected)

    def test_find_title_empty(self):
        result = self.liblary.find_title("Книга 1")
        self.assertEqual(result, "Empty")

    def test_find_title_error(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        with self.assertRaises(KeyError):
            self.liblary.find_title("Книга 5")

    def test_find_genre(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        result = self.liblary.find_genre("Жанр 1")
        expected = '"Книга 1" - Автор 1 (2000), Жанр 1, ISBN: 111111'

        self.assertEqual(result, expected)

    def test_find_genre_empty(self):
        result = self.liblary.find_genre("Жанр 1")
        self.assertEqual(result, "Empty")

    def test_find_title_error(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        self.liblary.updata_indexs()

        with self.assertRaises(KeyError):
            self.liblary.find_genre("Жанр 5")

    def test_str(self):
        book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1", 111111)
        book2 = Book("Книга 2", "Автор 2", 2005, "Жанр 2", 222222)
        book3 = Book("Книга 3", "Автор 3", 2010, "Жанр 3", 333333)

        self.liblary.bookcol.append(book1)
        self.liblary.bookcol.append(book2)
        self.liblary.bookcol.append(book3)

        result = str(self.liblary)
        expected = 'Коллекция книг:\n1) "Книга 1" - Автор 1 (2000), Жанр 1, ISBN: 111111\n2) "Книга 2" - Автор 2 (2005), Жанр 2, ISBN: 222222\n3) "Книга 3" - Автор 3 (2010), Жанр 3, ISBN: 333333'
        
        self.assertEqual(result, expected)

    def test_str_empty(self):
        result = str(self.liblary)
        self.assertEqual(result, "Empty")