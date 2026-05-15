from utils import students

def add_student():
    print("--- Chức năng: Thêm sinh viên ---")
    # Thành viên 1 sẽ code ở đây

def show_students():
    print("--- Chức năng: Hiển thị danh sách ---")
    # Thành viên 2 sẽ code ở đây

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
    # Thành viên 4 sẽ code ở đây