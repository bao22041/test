# ✅ Test Cases – Chức năng Đăng Nhập

| STT | Mô tả | Dữ liệu đầu vào | Các bước | Kết quả mong đợi |
|-----|------|------------------|----------|-------------------|
| TC01 | Đăng nhập thành công | Email: user@example.com <br> Password: 123456 | 1. Truy cập /login <br> 2. Nhập thông tin <br> 3. Nhấn Login | Chuyển đến trang chủ |
| TC02 | Thiếu mật khẩu | Email: user@example.com <br> Password: *(trống)* | Như trên | Hiện lỗi "Mật khẩu không được bỏ trống" |
| TC03 | Sai mật khẩu | Email: user@example.com <br> Password: sai123 | Như trên | Hiện lỗi "Sai tài khoản hoặc mật khẩu" |
