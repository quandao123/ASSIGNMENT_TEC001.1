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

