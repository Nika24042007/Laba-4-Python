from collections import UserDict


class BookIndex(UserDict):
    def __init__(self, list_books: list, key: str) -> None:
        """
        Инициализация словаря
        
        :param list_books: список из объектов класса Book
        :param key: параметр, который будет являться ключом для словаря
        """
        super().__init__()
        self.key_type = key
        self.build_index(list_books)

    def  build_index(self, list_books: list) ->None:
        """
        Создание словаря из объектов списка с задаными ключами
        
        :param list_books: список из объектов класса Book
        """
        self.data.clear()
    
        for item in list_books:
            if self.key_type == "isbn":
                if item.isbn not in self.data:
                    self.data[item.isbn] = []
                self.data[item.isbn].append(item)
            elif self.key_type == "year":
                if item.year not in self.data:
                    self.data[item.year] = []
                self.data[item.year].append(item)
            elif self.key_type == "author":
                if item.author not in self.data:
                    self.data[item.author] = []
                self.data[item.author].append(item)
            elif self.key_type == "genre":
                if item.genre not in self.data:
                    self.data[item.genre] = []
                self.data[item.genre].append(item)
            elif self.key_type == "title":
                if item.title not in self.data:
                    self.data[item.title] = []
                self.data[item.title].append(item)
    
    def __str__(self) -> str:
        """
        Форматирование словаря в строку для выводы при использование команды print
        
        :return: строка, которая будет выводиться
        """
        res = ""
        for key, value in self.data.items():
            res += f'{key}:\n'
            for book in self.data[key]:
                res += f'"{book.title}" - {book.author} ({book.year}), {book.genre}, ISBN: {book.isbn}\n'

        return res.strip()
    


