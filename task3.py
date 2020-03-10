class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self, distance):
        self.distance = distance
        self.odometer += distance

    def __subtract_fuel(self, distance):
        self.fuel -= distance/10

    def drive(self, distance):
        if distance//10 > self.fuel:
            print("Need more fuel, please, fill more!")
        else:
            print("Let's drive!")
            self.__add_distance(distance)
            print(f'Машина {self.make} {self.model} {self.year} года проехала {self.odometer} км')
            self.__subtract_fuel(distance)
            print(f'В баке осталось {self.fuel} л')


car_1 = Car('BMW', 'X6', 2019)
car_1.drive(300)
print('\n')

car_2 = Car('Toyota', 'RAV4', 2018)
car_2.drive(800)

