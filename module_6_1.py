# Родительский класс Animal
class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


# Дочерний класс Mammal, наследуется от Animal
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)


# Дочерний класс Predator, наследуется от Animal
class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)


# Родительский класс Plant
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


# Дочерний класс Flower, наследуется от Plant
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


# Дочерний класс Fruit, наследуется от Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределение атрибута edible для Fruit


# Пример использования классов
if __name__ == "__main__":
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
