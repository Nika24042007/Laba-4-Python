import unittest
from src.Simulation import Simulation
from src.Liblary import Liblary
from unittest.mock import patch, MagicMock

class TestSimulation(unittest.TestCase):
    def test_seed_step(self):
        mock_lib = MagicMock(spec=Liblary)
        with(patch("random.seed") as mock_seed,
             patch("random.randint") as mock_randint,
             patch("random.choice") as mock_choice):
            mock_choice.side_effect = ["add", "add"] 
            mock_randint.return_value = 2023
            
            Simulation(mock_lib, step=2, seed=42)
            
            mock_seed.assert_called_once_with(42)
            self.assertEqual(mock_lib.add_random.call_count, 2)

    def test_command_add(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
             patch('builtins.print') as mock_print):
            mock_choice.side_effect = ["add"]
            
            Simulation(mock_lib)
            
            mock_lib.add_random.assert_called_once()
            mock_print.assert_called_once_with("1) Book add")

    def test_command_del(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["del"]
            mock_lib.del_random.return_value = '"Книга" - Автор (2000), Жанр, ISBN: 123456'
            
            Simulation(mock_lib)
            
            mock_lib.del_random.assert_called_once()
            expected = '1) Book deleted: "Книга" - Автор (2000), Жанр, ISBN: 123456'
            mock_print.assert_called_once_with(expected)

    def test_command_del_empty(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["del"]
            mock_lib.del_random.return_value = "Empty"
            
            Simulation(mock_lib)
            
            mock_lib.del_random.assert_called_once()
            mock_print.assert_called_once_with("1) Try delet: Empty")

    def test_command_get(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["get", "Случайный автор", "Случайное название"]
            mock_lib.find_del_author_title.return_value = '"Найденная книга" - Автор (2000), Жанр, ISBN: 111111'

            Simulation(mock_lib)

            mock_lib.find_del_author_title.assert_called_once_with("Случайный автор", "Случайное название")
            mock_print.assert_called_once_with('1) Get: "Найденная книга" - Автор (2000), Жанр, ISBN: 111111')

    def test_command_get_error(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
             patch('builtins.print') as mock_print):
        
            mock_choice.side_effect = ["get", "Автор", "Название"]
            
            mock_lib.find_del_author_title.side_effect = KeyError("no such keys together")
            
            Simulation(mock_lib)
            mock_lib.find_del_author_title.assert_called_once_with("Автор", "Название")
            
            mock_print.assert_called_once_with("1) Try get: Error 'no such keys together'")

    def test_command_find_author(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["find", "author", "Автор"]
            
            mock_lib.find_author.return_value = "Book of this author"
            
            Simulation(mock_lib)
            
            mock_lib.find_author.assert_called_once_with("Автор")
            mock_print.assert_called_once_with("1) Find author:Book of this author")

    def test_command_find_title(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["find", "title", "Название"]
            
            mock_lib.find_title.return_value = "Book with this title"
            
            Simulation(mock_lib)
            
            mock_lib.find_title.assert_called_once_with("Название")
            mock_print.assert_called_once_with("1) Find title:Book with this title")

    def test_command_find_genre(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["find", "genre", "Жанр"]
            
            mock_lib.find_genre.return_value = "Book with this genre"
            
            Simulation(mock_lib)
            
            mock_lib.find_genre.assert_called_once_with("Жанр")
            mock_print.assert_called_once_with("1) Find genre:Book with this genre")

    def test_command_find_year(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
              patch("random.randint") as mock_randint, 
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["find", "year"]
            mock_randint.side_effect = [2023]
            
            mock_lib.find_year.return_value = "Book with this year"
            
            Simulation(mock_lib)
            
            mock_lib.find_year.assert_called_once_with(2023)
            mock_print.assert_called_once_with("1) Find year:Book with this year")

    def test_command_find_isbn(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
              patch("random.randint") as mock_randint, 
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["find", "isbn"]
            mock_randint.side_effect = [111111]
            
            mock_lib.find_isbn.return_value = "Book with this isbn"
            
            Simulation(mock_lib)
            
            mock_lib.find_isbn.assert_called_once_with(111111)
            mock_print.assert_called_once_with("1) Find isbn:Book with this isbn")

    def test_command_find_error(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
              patch("random.randint") as mock_randint, 
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["find", "isbn"]
            mock_randint.side_effect = [111111]
            
            mock_lib.find_isbn.side_effect = KeyError()
            
            Simulation(mock_lib)
            
            mock_lib.find_isbn.assert_called_once_with(111111)
            mock_print.assert_called_once_with("1) Try find isbn: Error ")

    def test_command_change_title(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["change", "title", "Новое название"]
            
            mock_lib.change_random.return_value = "Book change"
            
            Simulation(mock_lib)
            
            mock_lib.change_random.assert_called_once_with("title", "Новое название")
            mock_print.assert_called_once_with("1) Book changed")

    def test_command_change_author(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["change", "author", "Новый автор"]
            
            mock_lib.change_random.return_value = "Book change"
            
            Simulation(mock_lib)
            
            mock_lib.change_random.assert_called_once_with("author", "Новый автор")
            mock_print.assert_called_once_with("1) Book changed")

    def test_command_change_genre(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["change", "genre", "Новый жанр"]
            
            mock_lib.change_random.return_value = "Book change"
            
            Simulation(mock_lib)
            
            mock_lib.change_random.assert_called_once_with("genre", "Новый жанр")
            mock_print.assert_called_once_with("1) Book changed")

    def test_command_change_year(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
              patch('random.randint') as mock_randint,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["change", "year"]
            mock_randint.return_value = 2025
            
            mock_lib.change_random.return_value = "Book change"
            
            Simulation(mock_lib)
            
            mock_lib.change_random.assert_called_once_with("year", 2025)
            mock_print.assert_called_once_with("1) Book changed")

    def test_command_change_isbn(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
              patch('random.randint') as mock_randint,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["change", "isbn"]
            mock_randint.return_value = 111111
            
            mock_lib.change_random.return_value = "Book change"
            
            Simulation(mock_lib)
            
            mock_lib.change_random.assert_called_once_with("isbn", 111111)
            mock_print.assert_called_once_with("1) Book changed")

    def test_command_change_empty(self):
        mock_lib = MagicMock(spec=Liblary)
        with (patch('random.choice') as mock_choice,
              patch('random.randint') as mock_randint,
             patch('builtins.print') as mock_print):
            
            mock_choice.side_effect = ["change", "isbn"]
            mock_randint.return_value = 111111
            
            mock_lib.change_random.return_value = "Empty"
            
            Simulation(mock_lib)
            
            mock_lib.change_random.assert_called_once_with("isbn", 111111)
            mock_print.assert_called_once_with("1) Try change: Empty")