# (1) Phân tích và thiết kế giải pháp
# Phân tích Input/Output
# Input

# Người dùng nhập:
#   Số lượng chi nhánh → int
#   Số học viên đi học của từng lớp → int
#   Mỗi chi nhánh có:
#       2 lớp học

# Output
# Hệ thống in trạng thái lớp học

# Đề xuất giải pháp:
#   Vòng lặp ngoài để duyệt từng chi nhánh
#   Vòng lặp trong để duyệt 2 lớp học
#   Vòng lặp while để bắt nhập lại khi dữ liệu âm

# Pseudocode
# Nhập branch_count
# Lặp từng chi nhánh
#     In tên chi nhánh
#     Lặp 2 lớp học
#         Lặp vô hạn
#             Nhập student_count
#             Nếu student_count < 0
#                 In lỗi
#                 Nhập lại
#             Ngược lại
#                 Thoát vòng lặp
#         Nếu student_count == 0
#             In lớp vắng toàn bộ
#         Ngược lại nếu student_count >= 20
#             In lớp học ổn định
#         Ngược lại
#             In lớp cần được nhắc nhở


branch_count = int(input("Nhập số lượng chi nhánh: "))
for branch in range(1, branch_count + 1):

    print(f"\nChi nhánh {branch}:")

    for classroom in range(1, 3):

        while True:

            student_count = int(
                input(
                    f"Nhập số học viên đi học của lớp {classroom}: "
                )
            )
            if student_count < 0:
                print(
                    "Số học viên không hợp lệ. Vui lòng nhập lại."
                )

            else:
                break
        if student_count == 0:
            print(
                f"Chi nhánh {branch} - Lớp {classroom}: "
                "Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái."
            )
        elif student_count >= 20:
            print(
                f"Chi nhánh {branch} - Lớp {classroom}: "
                "Lớp học ổn định"
            )
        else:
            print(
                f"Chi nhánh {branch} - Lớp {classroom}: "
                "Lớp cần được nhắc nhở theo dõi"
            )