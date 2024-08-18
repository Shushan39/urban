# Необходимо имитировать ситуацию с посещением гостями кафе.
# Создайте 3 класса: Table, Guest и Cafe.
# Класс Table:
# Объекты этого класса должны создаваться следующим способом - Table(1)
# Обладать атрибутами number - номер стола и guest - гость, который сидит за
# этим столом (по умолчанию None)
# Класс Guest:
# Должен наследоваться от класса Thread (быть потоком).
# Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
# Обладать атрибутом name - имя гостя.
# Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
# Класс Cafe:
# Объекты этого класса должны создаваться следующим способом - Guest(Table(1),
# Table(2),....)
# Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в
# этом кафе (любая коллекция).
# Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
# Метод guest_arrival(self, *guests):
# Должен принимать неограниченное кол-во гостей (объектов класса Guest).
# Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest),
# запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол
# номер <номер стола>".
# Если же свободных столов для посадки не осталось, то помещать гостя в очередь
# queue и выводить сообщение "<имя гостя> в очереди".
# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
# Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы
# один стол занят.
# Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил
# работу - метод is_alive), то вывести строки "<имя гостя за текущим столом>
# покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий
# стол освобождается (table.guest = None).
# Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None),
# то текущему столу присваивается гость взятый из очереди (queue.get()).
# Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а)
# за стол номер <номер стола>"
# Далее запустить поток этого гостя (start)
# Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
# Table - стол, хранит информацию о находящемся за ним гостем (Guest).
# Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
# Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация
# прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).


import threading
import random
import time
from queue import Queue


# Класс Table (Стол)
class Table:
    def __init__(self, number):
        """
               Инициализация стола с заданным номером.
               Изначально за столом никто не сидит (guest = None).
               """
        self.number = number
        self.guest = None


# Класс Guest (Гость) - поток
class Guest(threading.Thread):
    def __init__(self, name):
        """
                Инициализация гостя с заданным именем.
                Гость является потоком, поэтому наследуется от threading.Thread.
                """
        super().__init__()
        self.name = name

    def run(self):
        """
               Метод run выполняется при запуске потока.
               Имитация процесса еды с ожиданием от 3 до 10 секунд.
               """
        time_to_eat = random.randint(3, 10)
        time.sleep(time_to_eat)


# Класс Cafe (Кафе)
class Cafe:
    def __init__(self, *tables):
        """
            Инициализация кафе с определённым количеством столов.
            Также создаётся очередь для гостей, если не хватает столов.
            """
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        """
               Метод для прибытия гостей.
               Если есть свободный стол, то гость садится за стол и запускается его поток.
               Если свободных столов нет, то гость помещается в очередь.
               """
        for guest in guests:
            # Поиск свободного стола
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table is not None:
                # Посадка гостя за стол
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                # Гость в очереди
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        """
                Метод для обслуживания гостей.
                Обслуживание продолжается до тех пор, пока есть гости за столами или в очереди.
                """
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


# Пример использования
if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]

    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()