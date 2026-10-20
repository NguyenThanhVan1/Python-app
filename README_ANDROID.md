# Món Quà Nhỏ Dành Cho Em - Android

Thư mục này là bản Android native dùng Kivy. File APK được tạo bằng Buildozer
trong WSL/Ubuntu (Buildozer không chạy native ổn định trên Windows).

## Build APK trên Windows bằng WSL

1. Cài Ubuntu trong WSL nếu máy chưa có:

   ```powershell
   wsl --install -d Ubuntu
   ```

2. Mở Ubuntu, truy cập thư mục dự án Windows:

   ```bash
   cd /mnt/c/Users/ADMIN/Desktop/20/mobile_app
   chmod +x build_apk_wsl.sh
   ./build_apk_wsl.sh
   ```

3. APK debug sẽ nằm trong thư mục `bin/`. Chép file `.apk` sang điện thoại,
   mở file đó và cho phép cài ứng dụng từ nguồn không xác định khi Android hỏi.

## Chạy thử trên máy tính

```powershell
python -m pip install -r .\mobile_app\requirements.txt
python .\mobile_app\main.py
```

Ứng dụng không bắt buộc ảnh; album vẫn hoạt động bình thường khi chưa thêm ảnh.

## Chạy phiên bản web bằng Streamlit

Cài dependencies và khởi động web app:

```powershell
python -m pip install -r .\requirements.txt
python -m streamlit run .\app.py
```

Sau đó mở địa chỉ được Streamlit hiển thị (thường là
`http://localhost:8501`). Phiên bản web hỗ trợ tùy chỉnh tên, lời nhắn và tải
ảnh lên album trong phiên làm việc hiện tại.
