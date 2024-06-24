class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'green', 'yellow', 'black', ]

    def __init__(self, model, engine_power, color, owner):
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color.lower()  # Приводим цвет к нижнему регистру
        self.owner = owner

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        info = [self.get_model(), self.get_horsepower(), self.get_color(),
                f"Владелец: {self.owner}"]
        print("\n".join(info))

    def set_color(self, new_color):
        new_color_lower = str(new_color.lower())  # преобразуем новый цвет к нижнему регистру
        if new_color_lower in self.__COLOR_VARIANTS:
            self.__color = new_color_lower
            print(new_color)
        else:
            print(f"Нельзя сменить цвет на {new_color}.")
        




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, model, engine_power, color, owner):
        super().__init__(model, engine_power, color, owner)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
