# Món Quà Nhỏ Dành Cho Em

Ứng dụng web được xây dựng bằng Streamlit.

## Chạy local

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Deploy lên Streamlit Community Cloud

1. Đẩy các file `app.py`, `requirements.txt` và `README.md` lên một repository
   trên GitHub.
2. Mở [share.streamlit.io](https://share.streamlit.io/) và đăng nhập bằng GitHub.
3. Chọn repository, branch và file chính `app.py`.
4. Bấm **Deploy**.

Streamlit Cloud sẽ tự động cài dependency từ `requirements.txt`.

## Tính năng

- Trang chào mừng và điều hướng giữa các phần của món quà.
- Tùy chỉnh tên người nhận, tên người tặng và lời nhắn riêng.
- Bức thư, lời nhắn yêu thương và lời kết.
- Tải ảnh lên album trong phiên sử dụng hiện tại.

