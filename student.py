from utils import students

def add_student():
    print("--- Chức năng: Thêm sinh viên ---")
    # Thành viên 1 sẽ code ở đây

def show_students():
    print("--- Chức năng: Hiển thị danh sách ---")
    
    # 1. Kiểm tra xem danh sách có dữ liệu hay không
    if len(students) == 0:
        print(">> Hiện tại chưa có sinh viên nào trong danh sách!")
        return # Thoát hàm sớm nếu không có dữ liệu

    # 2. In tiêu đề của bảng dữ liệu cho đẹp mắt (sử dụng f-string định dạng khoảng cách)
    print(f"{'Mã SV':<10} | {'Họ và Tên':<25} | {'Điểm':<5}")
    print("-" * 47) # In đường kẻ ngang

    # 3. Dùng vòng lặp for để duyệt qua từng sinh viên trong danh sách
    for sv in students:
        # Lấy dữ liệu an toàn bằng phương thức .get() đề phòng thiếu key
        ma_sv = sv.get("id", "N/A")
        ten = sv.get("name", "N/A")
        diem = sv.get("score", "N/A")
        
        # In thông tin từng sinh viên ra màn hình
        print(f"{ma_sv:<10} | {ten:<25} | {diem:<5}")
        
    print("-" * 47) # In đường kẻ ngang kết thúc bảng=

def search_student():
    print("--- Chức năng: Tìm kiếm sinh viên ---")
    # Thành viên 3 sẽ code ở đây

def delete_student():
    print("--- Chức năng: Xóa sinh viên ---")
    # Thành viên 4 sẽ code ở đây