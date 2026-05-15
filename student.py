from utils import students

def add_student():
    print("\n--- CHỨC NĂNG: THÊM SINH VIÊN ---")
    
    # Nhập dữ liệu từ bàn phím
    id_sv = input("Nhập mã số sinh viên: ")
    
    # Kiểm tra trùng mã số sinh viên
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
    # Bước 1: Nhận input từ người dùng
    keyword = input("Nhập tên hoặc ID sinh viên cần tìm: ")
    print(f"Hệ thống đang tìm kiếm từ khóa: '{keyword}'...")
    global students_db 
    results = []
    
    for std in students_db:
        # Tìm theo ID (khớp hoàn toàn) hoặc Tên (có chứa từ khóa)
        if keyword == std['id'] or keyword.lower() in std['name'].lower():
            results.append(std)
    # Bước 3: In kết quả ra màn hình
    if not results:
        print(f"[-] Rất tiếc, không tìm thấy sinh viên nào khớp với '{keyword}'.")
    else:
        print(f"[+] Tuyệt vời! Tìm thấy {len(results)} kết quả:")
        for std in results:
             print(f"  > ID: {std['id']} | Tên: {std['name']} | Ngành: {std['major']}") 

def delete_student():
    print("--- Chức năng: Xóa sinh viên ---")

    student_id = input("Nhập mã sinh viên cần xóa: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print(f"Đã xóa sinh viên có mã {student_id} thành công!")
            return

    print("Không tìm thấy sinh viên cần xóa!")