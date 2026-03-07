#1
numbers = []
while True:
    user_num = input("Mời bạn nhập 1 dãy số(Enter để thoát): ")
    #Người dùng không nhập gì hết thì tự động thoát vòng lặp
    if user_num == "" :
        break
    numbers.append(float(user_num))
#Sắp xếp số theo thứ tự giảm dần
numbers.sort(reverse = True)
first_5 = numbers[:5]
print("5 số lớn nhất bạn đã nhập: ", first_5)

#2

seasons = ("Spring", "Summer","Autumn", "winter")
month = int(input("Mời bạn nhập tháng(1-12): "))

if month == 12 or month == 1 or month == 2:
    season = seasons[3]
elif month == 3  or month == 4 or month == 5:
    season = seasons[0]
elif month == 6 or month == 7 or month == 8:
    season = seasons[1]
elif month == 9 or month == 10 or month == 11:
    season = seasons[2]
else:
    season = None
    print("Không xác định được tháng của bạn!")
print(f"\n tháng {month} của bạn nằm trong mùa {season}")

#3
names = set()
while True:
    name = input("Mời bạn nhập tên: ")
    if names == "":
        break

    elif name in names:
        print("Existing Name!")
    else:
        print("New Name!")
        names.add(name)
print("\nDanh sách tên đã nhập")
for n in names:
    print(n)

#T4
def word_frequency(text):
    text = text.lower()

    words = text.split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
text = input("Mời bạn nhập văn bản:")
result = word_frequency(text)
print("\nTần xuất xuất hiện các chữ trong văn bản")
for word, count in result.items():
    print(f" '{word}': {count} lần ")

#5
def eliminate_odd(numbers):
    even_num = []
    for num in numbers:
        if num % 2 == 0:
            even_num.append(num)
    return even_num

user_input = input("Mời bạn nhập số của bạn: ")
user_list = [int(x) for x in user_input.split()]
cut_down_list = eliminate_odd(user_list)
print(f"Danh sách gốc: {user_list}")
print(f"Danh sách rút gọn: {cut_down_list}")

#6
import random
def tinh_pi(diem):
    n = 0
    for _ in range(diem):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 +y**2 < 1:
            n += 1

    xap_xi_pi = 4 * n / diem
    return xap_xi_pi
diem = float(input("Bạn hãy nhập số điểm ngẫu nhiên muốn tạo: "))
result = tinh_pi(diem)
print(f"\nSố điểm đã tạo: {diem}")
print(f"Xấp xỉ của pi: {result}")
print(f"Giá trị thực của π: 3.14159265358979...")