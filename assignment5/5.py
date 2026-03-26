#1

numbers = []
while True :
    user_num = input("Yêu cầu bạn nhập 1 dãy số: ")
    if user_num == "":
        break
    else:
        numbers.append(float(user_num))
numbers.sort(reverse = True)
print("5 số lớn nhất:", numbers[:5])

#2
prime_num = int(input("Mời bạn nhập số bất kỳ: "))
for i in range(2, prime_num):
    if prime_num % i == 0:
        print(f"Số {prime_num} không phải số nguyên tố ")
        break
else:
    print(f"Số {prime_num} là số nguyên tố ")

#3
cities = []
for i in range(5):
    user_city = input("Mời bạn nhập tên thành phố của bạn: ")
    user_city.lower()
    cities.append(user_city)
for city in cities:
    print("Danh sách các thành phố mà bạn đã nhập!:")

#4
def in_total(nums):
    total = 0
    for num in nums:
        total += num
    return total
user_list = []
for i in range(7):
    user_input = input("Mời bạn nhập list số của bạn: ")
    if user_input == "":
        break
    user_list.append(float(user_input))
tong = in_total(user_list)
print(f"Tổng các số trong danh sách: {tong}")

#5
def sort_odd_num(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list
list_numbers = []
for i in range(7):
    user_nums = input("Mời bạn nhập danh sách list số")
    if user_nums =="":
        break
    list_numbers.append(int(user_nums))
remove_odd_list = sort_odd_num(list_numbers)
print(f"list gốc: {list_numbers}")
print(f"list số chẵn: {remove_odd_list}")