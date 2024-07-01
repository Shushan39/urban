import math


class Figure:
    sides_count = 0

    def __init__(self, sides, color):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = sides

        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def _is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def _is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__([radius], color)
        self.__radius = radius

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, radius):
        # Для круга можно рассматривать  радиус как  стороны
        if self._is_valid_sides(radius):
            self._Figure__sides = [radius]
            self.__radius = radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, side1, side2, side3):
        super().__init__([side1, side2, side3], color)
        self.__height = self.calculate_height()

    def calculate_height(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        height = 2 * area / a
        return height

    def get_square(self):
        a, b, c = self.get_sides()
        return 0.5 * a * self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__([side_length] * self.sides_count, color)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self._Figure__sides = list(new_sides)
            # Изменяем
            # защищенный атрибут __sides напрямую

    def get_sides(self):
        return self._Figure__sides


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
