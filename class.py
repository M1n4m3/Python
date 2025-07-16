class Car:
    def _init_(self):
        self.name = "abcd"
        self.color = "blue"
        self.fuel_type = "diesel"

    def engine(self):
        print("Used to start the car")

    def breac(self):
        print("Used to stop the car")

# Create an object
car = Car()
car.engine()
car.breac()
