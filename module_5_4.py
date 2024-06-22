class Building:
    total = 0

    def __init__(self):
        Building.total += 1


# создаем 40 объектов класса
for i in range(40):
    building = Building()

print(Building.total)
