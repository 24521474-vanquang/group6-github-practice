from utils import students

def add_student():
    print("\n--- CHỨC NĂNG: THÊM SINH VIÊN ---")
    
    # Nhập dữ liệu từ bàn phím
    id_sv = input("Nhập mã số sinh viên: ")
    
    # Kiểm tra trùng mã số sinh viên (bổ trợ thêm cho logic)
    for s in students:
        if s['id'] == id_sv:
            print("Lỗi: Mã sinh viên này đã tồn tại!")
            return

    name = input("Nhập tên sinh viên: ")
    major = input("Nhập ngành học: ")

    # Tạo dictionary mới và thêm vào danh sách 
    new_student = {
        "id": id_sv,
        "name": name,
        "major": major
    }
    
    students.append(new_student)
    print(f"Chúc mừng! Đã thêm sinh viên {name} thành công.")

def show_students():
    print("--- Chức năng: Hiển thị danh sách ---")
    # Thành viên 2 sẽ code ở đây

def search_student():
    print("--- Chức năng: Tìm kiếm sinh viên ---")
    # Thành viên 3 sẽ code ở đây

def delete_student():
    print("--- Chức năng: Xóa sinh viên ---")
    # Thành viên 4 sẽ code ở đây