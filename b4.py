# PHÂN TÍCH INPUT / OUTPUT

# Input:
# patient_id  -> nhập từ bàn phím -> mặc định kiểu str
# temp        -> nhập từ bàn phím -> mặc định kiểu str
# heart_rate  -> nhập từ bàn phím -> mặc định kiểu str

# Output mong muốn:
# patient_id  -> giữ nguyên kiểu str
# temp        -> chuyển sang float
# heart_rate  -> chuyển sang int

# GIẢI PHÁP 1
# Ép kiểu trực tiếp khi nhập
# Ưu điểm:
# - Code ngắn gọn
# - Ít biến
# - Tiết kiệm bộ nhớ

# Nhược điểm:
# - Khó debug khi nhập sai
# - Khó kiểm tra dữ liệu trước khi ép kiểu

# GIẢI PHÁP 2
# Lưu dữ liệu dạng chuỗi rồi mới ép kiểu
# Ưu điểm:
# - Dễ kiểm tra dữ liệu
# - Dễ debug
# - An toàn hơn cho hệ thống bệnh viện

# Nhược điểm:
# - Dùng nhiều biến hơn
# - Code dài hơn


# Chọn giải pháp 2 vì:
# - Hệ thống bệnh viện cần độ chính xác cao
# - Dễ kiểm tra dữ liệu trước xử lý
# - Hạn chế lỗi nhập sai
# - Dễ bảo trì và nâng cấp hệ thống
# TRIỂN KHAI CODE


# Nhập mã bệnh nhân
patient_id = input("Nhập mã bệnh nhân: ")

# Nhập dữ liệu dạng chuỗi
temp_str = input("Nhập nhiệt độ cơ thể: ")
heart_rate_str = input("Nhịp tim: ")
temp = float(temp_str)
heart_rate = int(heart_rate_str)

print("--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print("Mã bệnh nhân:", patient_id)
print("Nhiệt độ cơ thể:", temp)
print("==> Kiểu dữ liệu hệ thống ghi nhận:", type(temp))
print("Nhịp tim:", heart_rate, "nhịp/phút")
print("==> Kiểu dữ liệu hệ thống ghi nhận:", type(heart_rate))
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")
