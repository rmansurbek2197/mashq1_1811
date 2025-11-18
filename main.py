class Car:
    def __init__(self, fuel_level):
        self.__fuel_level = fuel_level

    @property
    def fuel(self):
        return self.__fuel_level

    @fuel.setter
    def fuel(self, value):
        if 0 <= value <= 100:
            self.__fuel_level = value
        else:
            raise ValueError("Yoqilg'i 0 va 100 oralig'ida bo'lishi kerak")


car = Car(50)
print(car.fuel)

car.fuel = 80
print(car.fuel)

car.fuel = 150
