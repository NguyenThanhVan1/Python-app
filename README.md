# Món quà 20/10

## Lưu album vĩnh viễn trên Streamlit Cloud

Streamlit Cloud có thể thay mới máy chủ sau khi ứng dụng ngủ, vì vậy thư mục
`album/` cục bộ không đảm bảo giữ ảnh mãi mãi. Ứng dụng hỗ trợ đồng bộ ảnh vào
thư mục `album/` của repository GitHub:

1. Tạo GitHub Personal Access Token có quyền `Contents: Read and write` trên
   repository `NguyenThanhVan1/Python-app`.
2. Trong Streamlit Cloud, mở **Settings → Secrets** và thêm:

   ```toml
   GITHUB_TOKEN = "github_pat_..."
   GITHUB_BRANCH = "main"
   ```

3. Khởi động lại ứng dụng. Ảnh mới và thông tin caption/thời gian sẽ được lưu
   vào GitHub và tự tải lại sau mỗi lần ứng dụng khởi động.

Trong mục **Album**, chọn ảnh, nhập caption, ngày và giờ chụp rồi bấm **Lưu ảnh
và thông tin**. Mỗi ảnh cũng có nút **Xóa ảnh**; thao tác này xóa cả file ảnh và
thông tin tương ứng trên GitHub.

Không đưa token vào mã nguồn hoặc commit token vào repository. Nếu chưa cấu hình
token, ứng dụng vẫn chạy nhưng ảnh chỉ được lưu tạm trên máy chủ.