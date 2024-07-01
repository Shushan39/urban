class Horse:
    """ Класс описывает лошадь"""

    def __init__(self):
        self.x_distance = 0  # пройденный путь
        self.sound = 'Frrr'  # звук, который издаёт лошадь

    def run(self, dx):
        """ Увеличивает пройденное расстояние на dx. """
        self.x_distance += dx


class Eagle:
    """ Класс описывающий орла """

    def __init__(self):
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл

    def fly(self, dy):
        """ Увеличивает высоту полёта на dy. """
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    """ Класс описывающий пегаса.
    Наследуется от Horse и Eagle в том же порядке. """

    def __init__(self):
        Horse.__init__(self)  # вызываем конструктор Horse
        Eagle.__init__(self)  # вызываем конструктор Eagle

    def move(self, dx, dy):
        """ Двигает пегаса: увеличивает пройденный путь и высоту полёта. """
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        """ Возвращает текущее положение пегаса в виде кортежа (x_distance, y_distance). """
        return self.x_distance, self.y_distance

    def voice(self):
        """ Печатает звук, который издаёт пегас. """
        print(self.sound)


# Создание объекта класса Pegasus и проверка работы методов
p1 = Pegasus()

print(p1.get_pos())  # вывод: (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # вывод: (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # вывод: (5, 35)

p1.voice()  # вывод: I train, eat, sleep, and repeat
