#==========Task1===========
class Elevator():
    def __init__(self, bottom, up ):
        self.bottom = bottom
        self.up = up
        self.current_floor = bottom
    def floor_up(self):
        self.current_floor += 1
        print(f"tầng {self.current_floor} ")
    def floor_down(self):
        self.current_floor -= 1
        print(f"tầng {self.current_floor}")
    def move_to_floor(self, n):
        if n > self.current_floor:
            print(f"Đi lên tầng {n}")
        elif n < self.current_floor:
            print(f"Đi xuống tầng {n}")
        while self.current_floor < n:
            self.floor_up()
        while self.current_floor > n:
            self.floor_down()
E = Elevator(0, 19)
print("Tòa nhà này có 18 tầng! ")
E.move_to_floor(int(input("Mời bạn nhập tầng mà bạn muốn tới: ")))



#2

class Elevator():
    def __init__(self, bottom, up):
        self.bottom = bottom
        self.up = up
        self.current_floor = bottom

    def floor_up(self):
        self.current_floor += 1
        print(f"Tầng {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Tầng {self.current_floor}")

    def move_to_floor(self, n):
        if n > self.current_floor:
            print(f"Đi lên tầng {n}")
        elif n < self.current_floor:
            print(f"Đi xuống tầng {n}")
        while self.current_floor < n:
            self.floor_up()
        while self.current_floor > n:
            self.floor_down()


class Building():
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(num_elevators):
            e = Elevator(bottom, top)
            self.elevators.append(e)

    def run_elevator(self, elevator_number, floor):
        elevator = self.elevators[elevator_number - 1]
        print(f"--- Thang máy số {elevator_number} ---")
        elevator.move_to_floor(floor)
        print()

b = Building(0, 19, 3)
print("Tòa nhà này có 18 tầng!\n")

tang1 = int(input("Thang máy 1 - Nhập tầng muốn tới: "))
b.run_elevator(1, tang1)

tang2 = int(input("Thang máy 2 - Nhập tầng muốn tới: "))
b.run_elevator(2, tang2)

# Quay về tầng 0
b.run_elevator(1, 0)
b.run_elevator(2, 0)

#3
class Elevator():
    def __init__(self, bottom, up):
        self.bottom = bottom
        self.up = up
        self.current_floor = bottom

    def floor_up(self):
        self.current_floor += 1
        print(f"Tầng {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Tầng {self.current_floor}")

    def move_to_floor(self, n):
        if n > self.current_floor:
            print(f"Đi lên tầng {n}")
        elif n < self.current_floor:
            print(f"Đi xuống tầng {n}")
        while self.current_floor < n:
            self.floor_up()
        while self.current_floor > n:
            self.floor_down()


class Building():
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(num_elevators):
            e = Elevator(bottom, top)
            self.elevators.append(e)

    def run_elevator(self, elevator_number, floor):
        elevator = self.elevators[elevator_number - 1]
        print(f"--- Thang máy số {elevator_number} ---")
        elevator.move_to_floor(floor)
        print()

    def fire_alarm(self):
        print(" BÁO ĐỘNG CHÁY!")
        for i in range(len(self.elevators)):  # Lặp qua tất cả thang máy
            print(f"--- Thang máy số {i+1} ---")
        self.elevators[i].move_to_floor(0)  # Về tầng nào?

b = Building(0, 19, 3)
print("Tòa nhà này có 18 tầng!\n")

tang1 = int(input("Thang máy 1 - Nhập tầng muốn tới: "))
b.run_elevator(1, tang1)

tang2 = int(input("Thang máy 2 - Nhập tầng muốn tới: "))
b.run_elevator(2, tang2)

# Quay về tầng 0
b.run_elevator(1, 0)
b.run_elevator(2, 0)

#4

import random
class car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list

    def hour_passes(self):
        for c in self.car_list:
            change = random.randint(-10, 15)
            c.accelerate(change)
            c.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Car':<10} {'Speed (km/h)':<15} {'Distance (km)':<15}")
        print("-" * 45)
        for c in self.car_list:
            print(f"{c.registration_number:<10} {c.current_speed:<15} {c.travelled_distance:<15.2f}")

    def race_finished(self):
        for c in self.car_list:
            if c.travelled_distance >= self.kilometers:
                return True
        return False


def main():
    cars = []
    for i in range(1, 11):
        reg_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(car(reg_number, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)
    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1

        if hours % 10 == 0:
            print(f"\nHour {hours}")
            race.print_status()
    print("\nRace finished")
    race.print_status()


if __name__ == "__main__":
    main()