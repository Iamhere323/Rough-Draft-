class Car:
    """Class to represent a car in the rental system"""
    
    def __init__(self, car_id, make, model, year, car_type, is_available=True):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.car_type = car_type  # e.g., 'SUV', 'Sedan', 'Truck'
        self.is_available = is_available
    
    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"[ID:{self.car_id}] {self.year} {self.make} {self.model} ({self.car_type}) - {status}"
