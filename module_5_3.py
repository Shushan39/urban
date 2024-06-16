class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


d1 = Building(5, '')
d2 = Building(6, '')
print(d1 == d2)

