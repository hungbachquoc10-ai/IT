import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
class Race:
    def __init__(self, name, distance_km, cars_list):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars_list
    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Reg. Number':<12} | {'Max Speed':<10} | {'Current Speed':<15} | {'Distance (km)':<15}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.registration_number:<12} | {car.max_speed:<10} | {car.current_speed:<15} | {car.travelled_distance:<15.1f}")

    def race_finished(self):
        # Check if any car has reached the goal distance
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False
participating_cars = []
for i in range(1, 11):
    participating_cars.append(Car(f"ABC-{i}", random.randint(150, 200)))
grand_derby = Race("Grand Demolition Derby", 8000, participating_cars)
hours_elapsed = 0
while not grand_derby.race_finished():
    grand_derby.hour_passes()
    hours_elapsed += 1
    if hours_elapsed % 10 == 0:
        print(f"\n--- Progress after {hours_elapsed} hours ---")
        grand_derby.print_status()
print(f"\n*** RACE FINISHED! Final results after {hours_elapsed} hours ***")
grand_derby.print_status()