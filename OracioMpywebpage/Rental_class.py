from datetime import datetime, timedelta

class Rental:

    def __init__(self, user, car, duration_days):
        self.user = user
        self.car = car
        self.duration_days = duration_days
        self.start_date = datetime.now()
        self.return_date = self.start_date + timedelta(days=duration_days)

    def __str__(self):
        return (
            f"{self.car.year} {self.car.make} {self.car.model} "
            f"({self.car.car_type}) | Duration: {self.duration_days} days "
            f"| From {self.start_date.date()} to {self.return_date.date()}"
        )
