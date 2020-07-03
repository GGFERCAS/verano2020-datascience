
class Car:
    def create_new(name, speed):
        car_info = {
            "name": name,
            "position": 0,
            "speed": speed,
        }
        return car_info
    
    def move(car_info):
        car_info["position"] += car_info["speed"]
        print(car_info["name"] + " is a now at position " + str(car_info["position"]))

gonzalos_car = Car
gonzalos_info = gonzalos_car.create_new("Gonzalo", 100)


gonzalos_car.move(gonzalos_info)
gonzalos_car.move(gonzalos_info)


