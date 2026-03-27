class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")
    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print(f"Error: Floor {target_floor} does not exist!")
            return
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
if __name__ == "__main__":
    h = Elevator(0, 10)
    print(f"Welcome! The elevator is currently at floor {h.current_floor}.")
    print(f"This building has floors from {h.bottom_floor} to {h.top_floor}.")
    try:
        user_choice = int(input("\nEnter the floor "))
        print(f"\nMoving to floor {user_choice}...")
        h.go_to_floor(user_choice)
        print(f"\nReturning to the bottom floor ({h.bottom_floor})...")
        h.go_to_floor(h.bottom_floor)
        print("Finished!")
    except ValueError:
        print("Invalid input! Please enter a number for the floor.")