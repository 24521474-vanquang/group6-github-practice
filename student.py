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

def delete_student():
    print("--- Chức năng: Xóa sinh viên ---")
    # Thành viên 4 sẽ code ở đây
    print("--- Chức năng: Xóa sinh viên ---")

    student_id = input("Nhập mã sinh viên cần xóa: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Đã xóa sinh viên thành công!")
            return

    print("Không tìm thấy sinh viên cần xóa!")