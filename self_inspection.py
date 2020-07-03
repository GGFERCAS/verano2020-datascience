
class Car:
    def __init__(self, name, speed):
        self = {
        self.name = name
        self.position = 0
        self.speed = speed
        }
        return self
    
    def move(self):
        self.position += self.speed
        print(self.name+  "is a now at position"  + str(self.position))

gonzalos_car = Car("Gonzalo", 100)

gonzalos_car.move()
gonzalos_car.move()

diegos_car = Car("Diego", 50)

diegos_car = Car()
diegos_car = Car()