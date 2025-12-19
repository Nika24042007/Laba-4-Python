from Liblary import Liblary
import random
from constants import BOOK_AUTHOR, BOOK_NAME, BOOK_GENRE

def Simulation(lib: object, step: int = 1, seed: int = 0) -> None:
    """
    Симуляция пользовательских действий работы с библиотекой
    
    :param lib: Объект класса Liblary
    :param step: сколько шагов должна проиграть симуляция
    :param seed: сид по умолччанию ноль
    """
    if seed != 0:
        random.seed(seed)
    command_list = ["add", "del", "get", "find", "change"]
    for i in range (step):
        command = random.choice(command_list)

        if command == "add":
            lib.add_random()
            print(f"{i+1}) Book add")
            
        elif command == "del":
            delet = lib.del_random()
            if delet == "Empty":
                print(str(i+1) + ") Try delet: "+ delet)
            else:
                print(f"{i+1}) Book deleted: {delet}")

        elif command == "get":
            author = random.choice(BOOK_AUTHOR)
            title = random.choice(BOOK_NAME)
            try:
                print(str(i+1) + ") Get: "+lib.find_del_author_title(author, title))
            except Exception as e:
                print(f"{i+1}) Try get: Error {e}")

        elif command == "find":
            args = ["author", "title", "genre", "year", "isbn"]
            a = random.choice(args)
            if a == "title":
                title = random.choice(BOOK_NAME)
                try:
                    print(str(i+1)+ ") Find title:" +lib.find_title(title))
                except Exception as e:
                    print(f"{i+1}) Try find title: Error {e}")
            elif a == "author":
                author = random.choice(BOOK_AUTHOR)
                try:
                    print(str(i+1)+ ") Find author:" +lib.find_author(author))
                except Exception as e:
                    print(f"{i+1}) Try find author: Error {e}")
            elif a == "genre":
                genre = random.choice(BOOK_GENRE)
                try:
                    print(str(i+1)+ ") Find genre:" +lib.find_genre(genre))
                except Exception as e:
                    print(f"{i+1}) Try find genre: Error {e}")
            elif a == "year":
                year = random.randint(1000,2025)
                try:
                    print(str(i+1)+ ") Find year:" +lib.find_year(year))
                except Exception as e:
                    print(f"{i+1}) Try find year: Error {e}")
            elif a == "isbn":
                isbn = random.randint(0,1000000)
                try:
                    print(str(i+1)+ ") Find isbn:" +lib.find_isbn(isbn))
                except Exception as e:
                    print(f"{i+1}) Try find isbn: Error {e}")

        elif command == "change":
            args = ["author", "title", "genre", "year", "isbn"]
            a = random.choice(args)
            ans = 0
            if a == "author":
                ans = lib.change_random(a, random.choice(BOOK_AUTHOR))
            elif a == "title":
                ans = lib.change_random(a, random.choice(BOOK_NAME))
            elif a == "genre":
                ans = lib.change_random(a, random.choice(BOOK_GENRE))
            elif a == "year":
                ans = lib.change_random(a, random.randint(1000, 2025))
            elif a == "isbn":
                ans = lib.change_random(a, random.randint(0, 1000000))
            if ans == "Empty":
                print(str(i+1)+ ") Try change: " +ans)
            else:
                print(f"{i+1}) Book changed")

