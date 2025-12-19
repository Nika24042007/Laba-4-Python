from collections import UserList
from Book import Book

class BookCollection(UserList):
    def __init__(self) -> None:
        """
        Создание списка, куда будут добавляться все книги и тут же они бубуд храниться
        """
        super().__init__()

    def add_random_book(self):
        """
        Добавление книги с рандомными параметрами в список
        """
        book = Book()
        book.random_book()
        self.append(book)
    
    def __str__(self) -> str:
        """
        Подготовка формата строки для печати
        
        :return: строка, которая будет напечатана при использование команды print
        """
        if not self:
            return "Коллекция книг пуста"
        
        result = "Коллекция книг:\n"
        for i, book in enumerate(self, 1):
            result += f'{i}) "{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'
        return result.strip()
    
    def getiem_format(self, index: int|slice) -> str:
        """
        Форматирование объектов с определенным индексам под нужный формат вывода
        
        :param index: индекс объекта в списке или срез списка
        :return: форматированого объекта(ов) в виде строки
        """
        if isinstance(index, slice):
            result = ""
            for i in range(index.start, index.stop+1):
                book = super().__getitem__(i)
                result += f'{i+1}) "{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'
            return result.strip()
        else:
            book = super().__getitem__(index)
            return f'{index+1}) "{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'
    
