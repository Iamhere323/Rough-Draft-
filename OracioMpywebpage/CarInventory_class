class CarInventory:
    
    def __init__(self):
        self.cars = {}  # Key: car_id, Value: Car instance
    
    def add_car(self, car):
        if car.car_id in self.cars:
            print(f"Car ID {car.car_id} already exists.")
        else:
            self.cars[car.car_id] = car
            #print(f"Car added: {car}")
    
    def view_available_cars(self):
        available_cars = [car for car in self.cars.values() if car.is_available]
        if not available_cars:
            print("No cars available at the moment.")
        else:
            print("\nAvailable Cars:")
            for car in available_cars:
                print(f"  - {car}")
    
    def rent_car(self, car_id):
        car = self.cars.get(car_id)
        if car and car.is_available:
            car.is_available = False
            print(f"Car {car_id} has been rented.")
            return car
        elif car:
            print(f"Car {car_id} is already rented.")
        else:
            print(f"Car ID {car_id} does not exist.")
        return None
    
    def return_car(self, car_id):
        car = self.cars.get(car_id)
        if car and not car.is_available:
            car.is_available = True
            print(f"Car {car_id} has been returned.")
        elif car:
            print(f"Car {car_id} was not rented.")
        else:
            print(f"Car ID {car_id} not found.")
