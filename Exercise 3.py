class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"  Moving up: floor {self.current}")
    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"  Moving down: floor {self.current}")
    def go_to_floor(self, target):
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
    def fire_alarm(self):
        print("\nFIRE ALARM ACTIVATED!")
        print("All elevators are returning to the bottom floor immediately.")
        for i, elevator in enumerate(self.elevators, start=1):
            print(f"\nEvacuating Elevator #{i}:")
            elevator.go_to_floor(self.bottom)
        print("\n All elevators are now at the bottom floor. ")
def main():
    print("Building Architect & Operator")
    try:
        bot = int(input("Enter bottom floor: "))
        top = int(input("Enter top floor: "))
        count = int(input("Number of elevators: "))
        my_building = Building(bot, top, count)
        while True:
            print(f"\nOptions: [1-{count}] = Move | 'f' = Fire Alarm | 'q' = Quit")
            choice = input("Your command: ").lower()
            if choice == 'q':
                break
            elif choice == 'f':
                my_building.fire_alarm()
            else:
                elevator_id = int(choice)
                target_floor = int(input(f"Target floor for Elevator #{elevator_id}: "))
                my_building.run_elevator(elevator_id, target_floor)
    except (ValueError, IndexError):
        print("\nInvalid input. Please use the numbers or commands provided.")
if __name__ == "__main__":
    main()