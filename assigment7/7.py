class car:
    #1
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    # 2
    def accelerate(self, change):
        self.current_speed = self.current_speed + change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    # 3
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


my_car = car("ABC-123", 142)
print("=" * 10, "Task1", "=" * 10)
print(f"biển số xe đăng kí: {my_car.registration_number}")
print(f"Giới hạn tốc độ xe: {my_car.maximum_speed}")
print(f"tốc độ hiện tại của xe: {my_car.current_speed}")
print(f"quảng đường xe đã đi: {my_car.travelled_distance}")
print(f"tốc độ hiện tại của xe: {my_car.current_speed}")
print("=" * 10, "Task2", "=" * 10)
my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)
print(f"tốc độ hiện tại của xe sau khi tăng tốc {my_car.current_speed}")
my_car.accelerate(-200)
print(f"tốc độ hiện tại của xe sau khi phanh khẩn cấp : {my_car.current_speed}")
print("=" * 10, "Task3", "=" * 10)
my_car.drive(1.5)
print(f"Quảng đường xe đã đi được: {my_car.travelled_distance} km ")

# 4
import random

cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(car(reg_number, max_speed))

race_over = False
while not race_over:
    for c in cars:
        change = random.randint(-10, 15)
        c.accelerate(change)
        c.drive(1)

    for c in cars:
        if c.travelled_distance >= 10000:
            race_over = True

print(f"{'Biển số':<10} {'Tốc độ tối đa':>15} {'Tốc độ hiện tại':>17} {'Quãng đường':>13}")
print("-" * 60)
for c in cars:
    print(f"{c.registration_number:<10} {c.maximum_speed:>15} {c.current_speed:>17} {c.travelled_distance:>13.1f}")