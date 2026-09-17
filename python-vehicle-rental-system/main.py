class Vehicle:
    def __init__(self, vehicle_number, brand, model, rental_price_per_day):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day

    def display_vehicle(self):
        print(f"Vehicle Number   : {self.vehicle_number}")
        print(f"Brand            : {self.brand}")
        print(f"Model            : {self.model}")
        print(f"Rental Price/Day : ₹{self.rental_price_per_day}")

    def calculate_rent(self, days):
        if not Vehicle.is_valid_rental_duration(days):
            raise ValueError("Rental duration must be greater than zero.")

        return self.rental_price_per_day * days

    @staticmethod
    def is_valid_rental_duration(days):
        return days > 0


class Car(Vehicle):
    def __init__(
        self,
        vehicle_number,
        brand,
        model,
        rental_price_per_day,
        number_of_seats
    ):
        super().__init__(
            vehicle_number,
            brand,
            model,
            rental_price_per_day
        )
        self.number_of_seats = number_of_seats

    def display_vehicle(self):
        super().display_vehicle()
        print(f"Number of Seats  : {self.number_of_seats}")


class Bike(Vehicle):
    def __init__(
        self,
        vehicle_number,
        brand,
        model,
        rental_price_per_day,
        engine_capacity
    ):
        super().__init__(
            vehicle_number,
            brand,
            model,
            rental_price_per_day
        )
        self.engine_capacity = engine_capacity

    def display_vehicle(self):
        super().display_vehicle()
        print(f"Engine Capacity  : {self.engine_capacity} cc")


def display_rental_details(vehicle, days):
    print(f"\n===== {vehicle.brand} {vehicle.model} =====")
    vehicle.display_vehicle()
    print(f"Rental Duration  : {days} days")
    print(f"Total Rent       : ₹{vehicle.calculate_rent(days)}")


# Create at least 2 cars
car1 = Car("CAR101", "Toyota", "Innova", 2500, 7)
car2 = Car("CAR102", "Hyundai", "Creta", 2000, 5)

# Create at least 2 bikes
bike1 = Bike("BIKE101", "Royal Enfield", "Classic 350", 800, 350)
bike2 = Bike("BIKE102", "Honda", "Activa 6G", 500, 110)


# Demonstrate the complete system
display_rental_details(car1, 3)
display_rental_details(car2, 2)
display_rental_details(bike1, 4)
display_rental_details(bike2, 5)


# Demonstrate static method validation
print("\n===== RENTAL DURATION VALIDATION =====")
print(f"5 days  : {Vehicle.is_valid_rental_duration(5)}")
print(f"0 days  : {Vehicle.is_valid_rental_duration(0)}")
print(f"-2 days : {Vehicle.is_valid_rental_duration(-2)}")
