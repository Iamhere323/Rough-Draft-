from Car_class import *
from CarInventory_class import *
from Rental_class import *
from user_class import *

def load_inventory_from_file(filename, inventory):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.lower().startswith("car_id"):
                    continue  # skip headers or empty lines

                parts = line.split(',')
                if len(parts) != 6:
                    print(f"Skipping invalid line: {line}")
                    continue

                car_id, make, model, year, car_type, is_available = parts

                try:
                    car = Car(
                        car_id=int(car_id),
                        make=make,
                        model=model,
                        year=int(year),
                        car_type=car_type,
                        is_available=is_available.strip().lower() == 'true'
                    )
                    inventory.add_car(car)
                except ValueError:
                    print(f"Invalid data format in line: {line}")

    except FileNotFoundError:
        print(f"File not found: {filename}")

def register_user(users_db):
    print("\n--- Register New User ---")
    name = input("Enter your name: ")
    email = input("Enter your email: ").lower()
    if email in users_db:
        print("User with this email already exists. Try logging in.")
        return None
    user_id = len(users_db) + 1
    user = User(name, email, user_id)
    users_db[email] = user
    print(" Registration successful!")
    return user

def login_user(users_db):
    print("\n--- User Login ---")
    email = input("Enter your email: ").lower()
    user = users_db.get(email)
    if user:
        print(f" Welcome back, {user.name}!")
        return user
    else:
        print("No user found with that email. Try registering.")
        return None

def rent_car_to_user(user, inventory):
    inventory.view_available_cars()
    car_id = input("\nEnter the ID of the car you want to rent: ")
    try:
        car_id = int(car_id)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    car = inventory.rent_car(car_id)
    if car:
        try:
            duration_days = int(input("How many days would you like to rent the car? "))
            if duration_days <= 0:
                print("Rental duration must be at least 1 day.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")
            return

        rental = Rental(user, car, duration_days)
        user.add_rental(rental)
        print(f"\n{user.name}, you successfully rented:\n  {rental}")

def user_menu(user, inventory):
    while True:
        print(f"\n--- Welcome, {user.name} ---")
        print("1. View available cars")
        print("2. Rent a car")
        print("3. View my rental history")
        print("4. Logout")

        choice = input("Choose an option: ")

        if choice == '1':
            inventory.view_available_cars()
        elif choice == '2':
            rent_car_to_user(user, inventory)
        elif choice == '3':
            user.view_rentals()
        elif choice == '4':
            print(f"Logged out {user.name}")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    inventory = CarInventory()
    load_inventory_from_file("List_of_Rental_Cars.txt", inventory)

    users = {}

    while True:
        print("\n=== Car Rental System ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            user = login_user(users)
            if user:
                user_menu(user, inventory)
        elif choice == '2':
            user = register_user(users)
            if user:
                user_menu(user, inventory)
        elif choice == '3':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
