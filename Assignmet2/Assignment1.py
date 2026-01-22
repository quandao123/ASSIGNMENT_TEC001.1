#task 1
def zander():
    size_limit=42
    length = float(input('enter the length of zander:'))
    if length >= size_limit:
        print('too big, good to go')
    else:
        print(f'too small your zander need more {size_limit-length}cm to go')
zander()
#task 2
def a_room():
    room = input('enter the cabin class:')
    if room == 'A'or room == 'a':
        print('above the car deck, equipped with a window.')
    elif room == 'B' or room == 'b':
        print('windowless cabin above the car deck.')
    elif room == 'C'or room == 'c':
        print('windowless cabin below the car deck.')
    elif room == 'LUX'or room == 'lux':
        print('upper-deck cabin with a balcony.')
    else:
        print(' room not found')
a_room()

#task 3
def health():
    gender=str(input('enter your gender(female/male): '))
    hemoglobin=int(input('enter your hemoglobin: '))
    if gender=='female':
       if hemoglobin > 155:
           print('too high')
       elif hemoglobin < 117:
           print('too low')
       else:
           print('too good')
    if gender=='male':
        if hemoglobin > 167:
            print('too high')
        elif hemoglobin < 134:
            print('too low')
        else:
            print('too good')
health()

#task 4
def leap():
    year=int(input('enter your year: '))
    if year%4==0 or year%100!=0 and year%400==0:
            print('yes this is leap year')
    else:
        print('this is not leap year')
leap()

#task 5

import math
def unit_price(diameter, price):
    area_m2 = (math.pi * (diameter / 2)**2) / 10000
    return price / area_m2
d1 = float(input("Pizza 1 diameter (cm): "))
p1 = float(input("Pizza 1 price ($): "))
d2 = float(input("Pizza 2 diameter (cm): "))
p2 = float(input("Pizza 2 price ($): "))
u1, u2 = unit_price(d1, p1), unit_price(d2, p2)
print(f"Unit Price: P1={u1:.2f}usd/m2 vs P2={u2:.2f}usd/m2")
if u1 < u2:
    print("Pizza 1 is better value.")
elif u2 < u1:
    print("Pizza 2 is better value.")
else:
    print("Same value.")


