from constants import BOOK_AUTHOR, BOOK_GENRE,BOOK_NAME
import random

class Book:
    def __init__(self, title: str ="", author: str="", year: int=0, genre: str="", isbn: int=0) -> None:
        """
        Создание книги по заданым пользователем параметрам
        
        :param title: Название книги
        :param author: Автор книги
        :param year: Год выпуска книги
        :param genre: Жанр книги
        :param isbn: Уникальный номер
        """
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    
    def random_book(self):
        """
        Создание книги с рандомными параметрами
        """
        self.title = random.choice(BOOK_NAME)
        self.author = random.choice(BOOK_AUTHOR)
        self.year = random.randint(1000,2025)
        self.genre = random.choice(BOOK_GENRE)
        self.isbn= random.randint(0,1000000)
        return self
    
