import os
from termcolor import colored
import time

class Car:

    def __init__(self, custom_speed):
        self.position = 0
        self.speed = custom_speed

    def drive(self):
        self.position += self.speed
    
    def print_info(self):
        print("Car is current at:", self.position, "with an speed of:", self.speed, end='\r')

    def __add__(self, other):
        return Car(self.speed + other.custom_speed)

    def __repr__(self):
        return "Car with speed " + str(self.speed)
    
    def __call__(self):
        return "You called the car you crazy person"


# nicos_car = Car()
# diegos_car = Car()
gonzalos_car = Car(0)

start_time = time.time()
for i in range(1, 200):
    time.time()
    gonzalos_car.speed = i
    gonzalos_car.drive()
    gonzalos_car.print_info()
    time.sleep(1)
    if gonzalos_car.speed >= 100:
        end_time = time.time()
        final_time = end_time - start_time
        print('\n', final_time)
        break
print()

# gonzalos_car.print_info()
# gonzalos_car.drive()
# gonzalos_car.drive()
# gonzalos_car.print_info()