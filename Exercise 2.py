class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"  ...Moving up: floor {self.current}")
    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"  ...Moving down: floor {self.current}")
    def go_to_floor(self, target):
        if target > self.top or target < self.bottom:
            print(f"  !! Error: Floor {target} is out of reach !!")
            return
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()
        print(f"  >> Arrived at floor {self.current} <<")
class Building:
    def __init__(self, bottom, top, count):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(count)]
    def run_elevator(self, num, floor):
        if 1 <= num <= len(self.elevators):
            print(f"\n[Commanding Elevator #{num} to floor {floor}]")
            self.elevators[num - 1].go_to_floor(floor)
        else:
            print(f"!! Error: Elevator {num} doesn't exist !!")
def main():
    print("--- Welcome to the Building Architect & Operator ---")
    try:
        bot = int(input("Enter the bottom floor number (e.g., 0): "))
        top = int(input("Enter the top floor number: "))
        count = int(input("How many elevators should the building have? "))
        
        my_building = Building(bot, top, count)
        print(f"\nBuilding created with {count} elevators (Floors {bot} to {top}).")
        while True:
            print(f"\n--- Options: [1-{count}] to pick elevator | 'q' to quit ---")
            choice = input("Which elevator would you like to move? ").lower()
            if choice == 'q':
                print("Closing the simulation. Goodbye!")
                break
            elevator_id = int(choice)
            target_floor = int(input(f"Which floor should Elevator #{elevator_id} go to? "))
            my_building.run_elevator(elevator_id, target_floor)
    except ValueError:
        print("\nInvalid input. Please enter numbers only.")
if __name__ == "__main__":
    main()