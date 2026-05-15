from utils import students

def add_student():
    print("--- Chức năng: Thêm sinh viên ---")
    # Thành viên 1 sẽ code ở đây

def show_students():
    print("--- Chức năng: Hiển thị danh sách ---")
    
    if len(students) == 0:
        print(">> Hiện tại chưa có sinh viên nào trong danh sách!")
        return 

    print(f"{'Mã SV':<10} | {'Họ và Tên':<25} | {'Điểm':<5}")
    print("-" * 47) 

    # MỚI SỬA: Sắp xếp danh sách dựa vào key "id" trước khi lặp
    sorted_students = sorted(students, key=lambda x: x.get("id", ""))

    # Đổi students thành sorted_students ở vòng lặp for
    for sv in sorted_students:
        ma_sv = sv.get("id", "N/A")
        ten = sv.get("name", "N/A")
        diem = sv.get("score", "N/A")
        print(f"{ma_sv:<10} | {ten:<25} | {diem:<5}")
        
    print("-" * 47) 
    print(f"Tổng số lượng sinh viên trong danh sách: {len(students)}")

def search_student():
    print("--- Chức năng: Tìm kiếm sinh viên ---")
    # Thành viên 3 sẽ code ở đây

def delete_student():
    print("--- Chức năng: Xóa sinh viên ---")
    # Thành viên 4 sẽ code ở đây