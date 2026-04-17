#1---------------------------------1----------------------------------
def count_lines(filepath):# định nghĩa hàm
    with open(filepath, 'r') as f:# mở file rồi đọc đặt tên là f, with để tự dộng đóng file sau khi cong
        dem = 0
        for line in f:  # duyệt từng dòng trong file
            if line.strip():  # nếu dòng đó không trống (strip() xóa khoảng trắng + \n)
                dem += 1  # thì đếm +1
        return dem

ket_qua = count_lines('mbox-short.txt') #gọi hàm với file , luu kết qua vao biến kết quả
print(f"Số dòng có nội dung: {ket_qua}")

#____________________2______________________2___________________
def find_keyword_lines(filepath, keyword):
    line_numbers = []
    try:

        with open(filepath, 'r', encoding='utf-8') as f:# Mở file với encoding utf-8 để đọc được các ký tự đặc biệt nếu có
            for i, line in enumerate(f, start=1): # start=1 để số dòng bắt đầu từ 1 thay vì 0, enumerate giúp lấy cả số dòng (i) và nội dung dòng (line)
                if keyword in line: # Kiểm tra từ khóa có xuất hiện trong dòng không
                    line_numbers.append(i)

    except FileNotFoundError:
        print(f"error: file not found '{filepath}'")
    except Exception as e:
        print(f"error: {e}")

    return line_numbers


# 1. nhập từ khóa từ bàn phím
file_name = 'mbox-short.txt'
key = input("input your key: ")

# 2. Gọi hàm đã viết ở trên
result = find_keyword_lines(file_name, key)


if isinstance(result, list):
    if len(result) > 0:
        print(f"found '{key}' at {len(result)}.")
    else:
        print(f"can not find'{key}' in file.")
#
#__________________3__________________________________3
def process_mbox_to_upper(input_file):
    try:
        # Mở file gốc để đọc
        with open(input_file, 'r', encoding='utf-8') as f_in:
            content = f_in.read()  # Đọc toàn bộ nội dung

        #  Chuyển nội dung thành chữ in hoa
        upper_content = content.upper()  # Chuyển đổi mọi ký tự


        with open('output.txt', 'w', encoding='utf-8') as f_out:#  Ghi vào file output, nó sẽ tự tạo 1 file mới
            f_out.write(upper_content)

        print("done! check file 'output.txt' for the result.")

    except FileNotFoundError:
        print(f"error: file not found '{input_file}'.")
    except Exception as e:
        print(f"error : {e}")


# Chạy hàm
process_mbox_to_upper('mbox-short.txt')
#________________________4_________________________4
def tinh_diem_trung_binh(duong_dan_file):
    tong_diem = 0
    so_luong = 0

    try:
        with open(duong_dan_file, 'r', encoding='utf-8') as f:
            for dong in f:
                # Loại bỏ khoảng trắng thừa và bỏ qua dòng trống
                dong = dong.strip()
                if not dong:
                    continue

                # Tách tên và điểm bằng dấu phẩy
                parts = dong.split(',')

                if len(parts) == 2:
                    try:
                        diem = float(parts[1])  # Chuyển điểm sang số thực
                        tong_diem += diem
                        so_luong += 1
                    except ValueError:
                        print(f"Bỏ qua dòng lỗi định dạng số: {dong}")

        # Tính trung bình
        if so_luong > 0:
            trung_binh = tong_diem / so_luong
            return trung_binh
        else:
            return 0

    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file.")
        return None


#run
file_name = 'diem_so.txt'
ket_qua = tinh_diem_trung_binh(file_name)

if ket_qua is not None:
    print(f"Điểm trung bình của tất cả sinh viên là: {ket_qua:.2f}")
