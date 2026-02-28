#1
import re
inout = input('nhập tên khoá học:')
if re.match(r'^[A-Z]{3}\d{3}$', inout):
    print(True)
else:
        print(False)
#2
def hex_color(color):
    if len(color) !=7 or color[0] != "#":
        return False
    hex_num = color[1:]
    for char in hex_num:
        if not (char.isdigit() or char.lower() in "abcdef"):
            return False
    return True
color_code = input("Mời bạn nhập mã màu: ")
if hex_color(color_code):
    print("mã màu của bạn hợp lệ!")
else:
    print("Mã màu của bạn không hợp lệ!")

#3
def sum_num_in_text(text):
    numbers = re.findall(r'\d+', text)
    total = sum(int(num) for num in numbers)
    return total
paragraph = input("Mời bạn nhập văn bản:")
result = sum_num_in_text(paragraph)
print("Tổng các số tìm được: ", result)

#4
def redact_phone_numbers(text):
    pattern = r'(\b\d{10}\b|\+84\d+)'
    result = re.sub(pattern, '[REDACTED]', text)
    return result
document = input("Yêu cầu bạn nhập Sdt:")
hidden_num = redact_phone_numbers(document)
print("Sau khi ẩn số điện thoại:")
print(hidden_num)