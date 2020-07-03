
class Car:

    def create_new():
        position = 0
        speed = 10
        return position, speed


    def move(position, speed):
        position += speed
        print("Car is now at position " + str(position))
        return position, speed


gonzalos_car = Car
gonzalos_info = gonzalos_car.create_new()



gonzalos_info = gonzalos_car.move(*gonzalos_info)
gonzalos_info = gonzalos_car.move(*gonzalos_info)
gonzalos_info = gonzalos_car.move(*gonzalos_info)


diegos_car = Car
diegos_info = diegos_car.create_new()



diegos_info = diegos_car.move(*diegos_info)
diegos_info = diegos_car.move(*diegos_info)
diegos_info = diegos_car.move(*diegos_info)



