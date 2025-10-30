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

    def display_all_vehicles_with_details(self): #Display all vehicles with comprehensive details in a formatted table#
        #Checks whether your dictionary self.cars (which stores all Car objects) is empty.If yes → print a message and exit early (return).
        if not self.cars:
            print("No vehicles in inventory.")
            return
        
        # decorative for when user clicks on option
        print("\n" + "="*90)
        print(" "*30 + "VEHICLE INVENTORY")
        print("="*90)

        #format is the header row

        print(f"{'ID':<6} {'Year':<6} {'Make':<15} {'Model':<20} {'Type':<15} {'Status':<12}")
        print("-"*90)

        available_count = 0 # tracks avaiable cars
        rented_count = 0 # tracks unavaible cars    

        for car in self.cars.values(): # for loop to track the status of avaiable car uses method values to show all the Car object in the inventory
            status = "✓ Available" if car.is_available else "✗ Rented" # checks status 
            print(f"{car.car_id:<6} {car.year:<6} {car.make:<15} "  
                f"{car.model:<20} {car.car_type:<15} {status:<12}")
            
            if car.is_available:
                available_count += 1
            else:
                rented_count += 1
    
    # Summary
        print("-"*90)
        print(f"\nTotal Vehicles: {len(self.cars)} | Available: {available_count} | Rented: {rented_count}")
        print("="*90 + "\n")



    def display_available_vehicles_detailed(self):
        """Display only available vehicles with full details"""
        print("\n" + "="*90)
        print(" "*27 + "AVAILABLE VEHICLES")
        print("="*90)
        
        # Header
        print(f"{'ID':<6} {'Year':<6} {'Make':<15} {'Model':<20} {'Type':<15}")
        print("-"*90)
        
        available_count = 0
        
        # Display each available car
        for car in self.cars.values():
            if car.is_available:
                print(f"{car.car_id:<6} {car.year:<6} {car.make:<15} "
                    f"{car.model:<20} {car.car_type:<15}")
                available_count += 1
        
        if available_count == 0:
            print("No cars available at the moment.")
        
        print("-"*90)
        print(f"\nTotal Available: {available_count}")
        print("="*90 + "\n")
    
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
