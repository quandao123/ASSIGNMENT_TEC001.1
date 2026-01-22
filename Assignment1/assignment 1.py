#task 1
name = input("What is your name? ")
print(f"Hello, {name}”)

#task 2
import math

radius = input("Please enter the radius of the circle: ")
radius = float(radius)
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is {circumference}”)

#task 3
length = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")
length = float(length)
width = float(width)
area = length * width
print(f"The area of the rectangle is {area}")
area = float(area)
perimeter = length * 2 + width * 2
print(f"The perimeter of the rectangle is {perimeter}”)

 #task4
num1 = int(input ("Enter the first number: "))
num2 = int(input ("Enter the second number: "))
num3 = int(input ("Enter the third number: "))
sum = num1 + num2 + num3
print(f"The sum of {num1} and {num2} and {num3} is {sum}")
product = num1 * num2 * num3
print(f"The product of {num1} and {num2} and {num3} is {product}")
average = (num1 + num2 + num3) / 3
print(f"The average of {num1} and {num2} and {num3} is {average}”)

#task5
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

pounds_in_lots = pounds * 32
talents_in_lots = talents * 20 * 32
total_lots = lots + pounds_in_lots + talents_in_lots

total_grams = total_lots * 13.3


kilograms = int(total_grams // 1000)
grams = total_grams - (kilograms * 1000)

print("The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")

#task5
import random
d1 = random.randint(0, 9)
d2 = random.randint(0, 9)
d3 = random.randint(0, 9)
print(f"3-digit code: {d1}-{d2}-{d3}")
n1 = random.randint(1, 6)
n2 = random.randint(1, 6)
n3 = random.randint(1, 6)
n4 = random.randint(1, 6)
print(f"4-digit code: {n1}-{n2}-{n3}-{n4}")

