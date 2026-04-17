def count_lines(filepath):# định nghĩa hàm
    with open(filepath, 'r') as f:# mở file rồi đọc đặt tên là f, with để tự dộng đóng file sau khi cong
        dem = 0
        for line in f:  # duyệt từng dòng trong file
            if line.strip():  # nếu dòng đó không trống (strip() xóa khoảng trắng + \n)
                dem += 1  # thì đếm +1
        return dem

ket_qua = count_lines('mbox-short.txt') #gọi hàm với file , luu kết qua vao biến kết quả
print(f"Số dòng có nội dung: {ket_qua}")
