from Book import Book
from BookCollection import BookCollection
from BookIndex import BookIndex
import random

class Liblary:

    def __init__(self) -> None:
        """
        Инициализация списка и словарей
        
        """
        self.bookcol = BookCollection()
        self.bookisbn = BookIndex(self.bookcol, "isbn")
        self.bookyear = BookIndex(self.bookcol, "year")
        self.bookauthor = BookIndex(self.bookcol, "author")
        self.bookgenre = BookIndex(self.bookcol, "genre")
        self.booktitle = BookIndex(self.bookcol, "title")

    def add_random(self) ->None:
        """
        Добавление книги с рандомными параметрами в список
        """
        self.bookcol.add_random_book()
        
    def add(self, title: str, author: str, genre: str, year: int, isbn: int) -> None:
        """
        Добавление книги с задаными пользователем параметрами в список
        
        :param title: Название книги
        :param author: Автор книги
        :param genre: Жанр книги
        :param year: Год издания
        :param isbn: Унмкальный номер
        """
        self.bookcol.append(Book(title, author, year, genre, isbn))

    def del_book(self, index: int) -> str:
        """
        Удаление книги по индексу в списке, индекс задается пользователем
        
        :param index: Индекс книги
        :return: Книгу, которую идалили или ,если список был пуст, соощение о пустоте
        """
        l = len(self.bookcol)
        if l == 0:
            return "Empty"
        elif l-1 < index:
            raise IndexError("no such index")
        else:
            res = f'"{self.bookcol[index].title}" - {self.bookcol[index].author} ({self.bookcol[index].year}), {self.bookcol[index].genre}, ISBN: {self.bookcol[index].isbn}'
            del self.bookcol[index]
            return res

    def del_random(self) -> str:
        """
        Удаление рандомной книги
        
        :return: Книгу, которую идалили или ,если список был пуст, соощение о пустоте
        """
        l = len(self.bookcol)
        if l > 1:
            a = random.randint(0, l-1)
            res = f'"{self.bookcol[a].title}" - {self.bookcol[a].author} ({self.bookcol[a].year}), {self.bookcol[a].genre}, ISBN: {self.bookcol[a].isbn}'
            del self.bookcol[a]
            return res
        else:
            return "Empty"
    
    def find_del_author_title(self, author: str, title: str) -> str:
        """
        Получение книги из списка по заданому автору и названию
        
        :param author: Автор книги
        :param title: Название книги
        :return: Книга(и), которую(ые) нашли с данным автором и названием
        """
        l = len(self.bookcol)
        if l == 0:
            return "Empty"
        else:
            if author not in self.bookauthor.keys() or title not in self.booktitle.keys():
                raise KeyError("no such keys together")
            else:
                res = ''
                for book in self.bookauthor[author]:
                    if book.title == title:
                        res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'
                        self.bookcol.remove(book)
                return res.strip()

    def change(self, index: int, arg: str, new_arg: str) -> str:
        """
        Изменение любой информации о книги по желению пользователя, книгу выбирает пользователь по индексу
        
        :param index: Индекс книги, которую пользователь хочет изменить
        :param arg: Аргумент который хочет заменить пользователь
        :param new_arg: Новое название аргумента
        :retur: сообщение о выполненом действие или о пустоте списка
        """
        l = len(self.bookcol)
        if l == 0:
            return "Empty"
        else:
            if l-1 < index:
                raise IndexError("no such index")
            else:
                if arg is "title":
                    self.bookcol[index].title = new_arg
                    return "Book change"
                elif arg == "author":
                    self.bookcol[index].author = new_arg
                    return "Book change"
                elif arg == "genre":
                    self.bookcol[index].genre = new_arg
                    return "Book change"
                elif arg == "isbn":
                    self.bookcol[index].isbn = new_arg
                    return "Book change"
                elif arg == "year":
                    self.bookcol[index].year = new_arg
                    return "Book change"
                else:
                    raise ValueError("no such argument")
            
    def change_random(self, arg: str, new_arg: str) -> str:
        """
        Docstring for change_random
        
        :param arg: Аргумент который надо изменить
        :param new_arg: Новое название аргумента
        :retur: сообщение о выполненом действие или о пустоте списка
        """
        index = random.randint(0, len(self.bookcol)-1)
        l = len(self.bookcol)
        if l == 0:
            return "Empty"
        else:
            if arg == "title":
                self.bookcol[index].title = new_arg
                return "Book change"
            elif arg == "author":
                self.bookcol[index].author = new_arg
                return "Book change"
            elif arg == "genre":
                self.bookcol[index].genre = new_arg
                return "Book change"
            elif arg == "isbn":
                self.bookcol[index].isbn = new_arg
                return "Book change"
            elif arg == "year":
                self.bookcol[index].year = new_arg
                return "Book change"

    def find_author(self, author: str) -> str:
        """
        Поиск книг по автору
        
        :param author: Автор книги
        :return: строка из найденных книг или сообщение о пустоте списка
        """
        l = len(self.bookcol)
        if l == 0:
            return "Empty"
        else:
            if author not in self.bookauthor.keys():
                raise KeyError("no such  key")
            else:
                res = ''
                for book in self.bookauthor[author]:
                    res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'
            return res.strip()

    def find_isbn(self, isbn: int) -> str:
        """
        Поиск книг по уникальному номеру
        
        :param isbn: Уникальный номер
        :return: строка из найденых книг или сообщение о пустоте списка
        """
        l = len(self.bookcol)
        if l == 0:
            return "Empty"
        else:
            if isbn not in self.bookisbn.keys():
                raise KeyError("no such  key")
            else:
                res = ''
                for book in self.bookisbn[isbn]:
                    res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'
            return res.strip()
    
    def find_year(self, year: int) -> str:
        """
        Поиск книги по году выпуска
        
        :param year: Год выпуска книги
        :return: строка из найденых книг или сообщение о пустоте списка
        """
        l = len(self.bookcol)
        if l == 0:
            return "Empty"
        else:
            if year not in self.bookyear.keys():
                raise KeyError("no such  key")
            else:
                res = ''
                for book in self.bookyear[year]:
                    res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'
            return res.strip()

    def find_title(self, title: str) -> str:
        """
        Поиск книг по названию
        
        :param title: Название книги
        :return: строка из найденых книг или сообщение о пустоте списка
        """
        l = len(self.bookcol)
        if l == 0:
            return "Empty"
        else:
            if title not in self.booktitle.keys():
                raise KeyError("no such  key")
            else:
                res = ''
                for book in self.booktitle[title]:
                    res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'
            return res.strip()
    
    def find_genre(self, genre: str) -> str:
        """
        Поиск книг по жанру
        
        :param genre: Жанр книги
        :return: строка из найденых книг или сообщение о пустоте списка
        """
        l = len(self.bookcol)
        if l == 0:
            return "Empty"
        else:
            if genre not in self.bookgenre.keys():
                raise KeyError("no such  key")
            else:
                res = ''
                for book in self.bookgenre[genre]:
                    res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'
            return res.strip()
    
    def __str__(self) -> str:
        """
        Форматирование списка под нужный формат вывода при вызове команды print
        
        :return: строка которая будет выводиться
        """
        res = "Коллекция книг:\n"
        l = len(self.bookcol)
        if l == 0:
            return "Empty"
        else:
            for i, book in enumerate(self.bookcol, 1):
                res += f'{i}) "{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'

        # res += "ISBN:\n"
        # for key, value in self.bookisbn.items():
        #     res += f'{key}:\n'
        #     for book in self.bookisbn[key]:
        #         res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'

        # res += "AUTHOR:\n"
        # for key, value in self.bookauthor.items():
        #     res += f'{key}:\n'
        #     for book in self.bookauthor[key]:
        #         res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'

        # res += "YEAR:\n"
        # for key, value in self.bookyear.items():
        #     res += f'{key}:\n'
        #     for book in self.bookyear[key]:
        #         res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'

        # res += "GENRE:\n"
        # for key, value in self.bookgenre.items():
        #     res += f'{key}:\n'
        #     for book in self.bookgenre[key]:
        #         res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'
        
        # res += "TITLE:\n"
        # for key, value in self.booktitle.items():
        #     res += f'{key}:\n'
        #     for book in self.booktitle[key]:
        #         res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'

        return res.strip()
    
