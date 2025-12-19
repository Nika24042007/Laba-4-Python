from Liblary import Liblary
import re
from Simulation import Simulation

def main() -> None:
    """
    Главная функция где происходит выбор следущих действей пользователем
    """
    lib = Liblary()
    while (1):
        command = int(input("Введите номер команды: \n1.Рандомные команды \n2.Самостоятельный вабор команды \n3.Выход \n"))
        if command == 1:
            command = input("Введите кол-во шагов и сид через пробел (23 4): ")
            try:
                list_command = [int(i) for i in command.split()]
                l = len(list_command)
                if l == 0:
                    Simulation(lib)
                elif l == 1:
                    Simulation(lib, list_command[0])
                elif l == 2:
                    Simulation(lib, list_command[0], list_command[1])
                else:
                    print("Error: too many arguments")
            except:
                print(f"Error: uncorrect command")

        elif command == 2:
            command = input("Введите коменду из списка (add, del, get, find, change, add_random, print): ")
            if command == "add":
                command = input("Введите (название автор жанр год isbn)(все водить как в примере через пробел не меняя порядок, isbn и год долны бить целыми неотрицательными числами, название, автор и жанр должны быть в двойных кавычках): \n")
                title = re.search(r'^"(.*?)"', command)
                command = re.sub(r'^"(.*?)"',"", command)
                author = re.search(r'^"(.*?)"', command)
                command = re.sub(r'^"(.*?)"',"", command)
                genre = re.search(r'^"(.*?)"', command)
                command = re.sub(r'^"(.*?)"',"", command)
                list_command = command.split()
                try:
                    lib.add(title[0].strip()[1:-1], author[0].strip()[1:-1], genre[0].strip()[1:-1], int(list_command[0]), int(list_command[-1]))
                    print("Book add")
                except:
                    print("Error: uncorrect command")
                    
            elif command == "add_random":
                command = int(input("Введите сколько книг вы хотите добавить (целое неотрицательное число): "))
                for i in range(command):
                    lib.add_random()
                print("Random books add")

            elif command == "print":
                print(lib)

            elif command == "del":
                try:
                    command = int(input("Введите индекс удаляемой книги: "))
                    print(lib.del_book(command))
                    print("Book deleted")
                except Exception as e:
                    print(f"Error: {e}")

            elif command == "get":
                command = input("Введите название и автора желаемой книги через запятую (название, автор): \n")
                try:
                    list_command = command.split(",")
                    print(lib.find_del_author_title(list_command[-1].strip(), list_command[0].strip()))
                except Exception as e:
                    print(f"Error: {e}")

            elif command == "find":
                command = input("Введите по какому критерию нужно искать книгу (author, title, genre, isbn, year)(выбрать нужно только одно): \n")
                if command == "author":
                    command = input("Введите автора: ").strip()
                    try:
                        print(lib.find_author(command))
                    except Exception as e:
                        print(f'Error: {e}')
                elif command == "title":
                    command = input("Введите название: ").strip()
                    try:
                        print(lib.find_title(command))
                    except Exception as e:
                        print(f'Error: {e}')
                elif command == "genre":
                    command = input("Введите жанр: ").strip()
                    try:
                        print(lib.find_genre(command))
                    except Exception as e:
                        print(f'Error: {e}')
                elif command == "isbn":
                    command = int(input("Введите isbn: ").strip())
                    try:
                        print(lib.find_isbn(command))
                    except Exception as e:
                        print(f'Error: {e}')
                elif command == "year":
                    command = int(input("Введите год: ").strip())
                    try:
                        print(lib.find_year(command))
                    except Exception as e:
                        print(f'Error: {e}')
                else:
                    print("Error: uncorrect command")
                    
            elif command == "change":
                command = input('Введите индекс книги, в которой хотите что-то поменять, что надо поменять и на что(1, title, "Красная Шапочка")(название книги, жанр и атор пишется в двойных кавычках): \n')
                try:
                    list_command = command.split(", ")
                    if list_command[1] == "title" or list_command[1] == "genre" or list_command[1] == "author":
                        res = lib.change(int(list_command[0]), list_command[1], list_command[-1].strip()[1:-1])
                        if res == "Empty":
                            print(res)
                        else:
                            print("Book changed")
                    else:
                        res = lib.change(int(list_command[0]), list_command[1], int(list_command[-1]))
                        if res == "Empty":
                            print(res)
                        else:
                            print("Book changed")
                except Exception as e:
                    print(f'Error: {e}')
                    
            else:
                print("Error: no such command")
        elif command == 3:
            exit()
        else:
            print("No such command")


if __name__ == "__main__":
    main()
