class Car:

    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed

my_car = Car("Italy", "Fiat 500", 2022, 70.5)
my_car.accelerate()
my_car.accelerate()
my_car.brake()
print(my_car.get_speed())
