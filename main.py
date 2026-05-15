import student

def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm sinh viên")
        print("4. Xóa sinh viên")
        print("0. Thoát")
        
        choice = input("Chọn chức năng (0-4): ")
        
        if choice == '1':
            student.add_student()
        elif choice == '2':
            student.show_students()
        elif choice == '3':
            student.search_student()
        elif choice == '4':
            student.delete_student()
        elif choice == '0':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()