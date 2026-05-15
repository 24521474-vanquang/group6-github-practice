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

def update_student():
    print("\n--- CHỨC NĂNG: SỬA THÔNG TIN SINH VIÊN ---")
    id_sv = input("Nhập mã số sinh viên cần sửa: ")
    
    # Tìm kiếm sinh viên trong danh sách
    for s in students:
        if s['id'] == id_sv:
            print(f"Đã tìm thấy sinh viên: {s['name']} (Ngành: {s['major']})")
            
            # Nhập thông tin mới
            new_name = input("Nhập tên mới (để trống nếu không đổi): ")
            new_major = input("Nhập ngành mới (để trống nếu không đổi): ")
            
            # Cập nhật nếu người dùng có nhập nội dung mới
            if new_name:
                s['name'] = new_name
            if new_major:
                s['major'] = new_major
                
            print("Cập nhật thông tin thành công!")
            return

    # Nếu chạy hết vòng lặp mà không thấy ID
    print(f"Không tìm thấy sinh viên có mã {id_sv}!")

def show_students():
    print("--- Chức năng: Hiển thị danh sách ---")
    # Thành viên 2 sẽ code ở đây

def search_student():
    print("--- Chức năng: Tìm kiếm sinh viên ---")
    # Thành viên 3 sẽ code ở đây

def delete_student():
    print("--- Chức năng: Xóa sinh viên ---")
    # Thành viên 4 sẽ code ở đây