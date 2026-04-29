# Bài tập lớn 2 CSDL Phân tán - Nhóm 9

## Giới thiệu
Triển khai cụm OrientDB phân tán trên 4 Node thông qua mạng LAN ảo Radmin VPN.

## 🛠 Yêu cầu hệ thống
* **Docker & Docker Compose** đã được cài đặt.
* **Radmin VPN**: Tất cả thành viên phải join vào cùng một Network.
* **Hệ điều hành**: Windows/macOS/Linux.

## 📁 Cấu trúc thư mục
* `docker-compose.yml`: Cấu hình Docker container.
* `hazelcast.xml`: Cấu hình kết nối TCP-IP giữa các Node qua IP Radmin.
* `default-distributed-db-config.json`: Cấu hình Replication (Nhân bản) và Quorum (Đồng thuận).

## 🚀 Hướng dẫn cài đặt cho thành viên

### Bước 1: Cập nhật IP Radmin
Mở file `hazelcast.xml` và đảm bảo danh sách `<tcp-ip>` chứa đúng địa chỉ IP Radmin của tất cả thành viên trong nhóm.

### Bước 2: Cấu hình Node cá nhân
Mở file `docker-compose.yml`, tìm đến dòng `ORIENTDB_NODE_NAME` và sửa thành tên định danh của bạn (ví dụ: `node_huy`).

### Bước 3: Mở Port Tường lửa (Firewall) hoặc tắt tường lửa
Đảm bảo máy tính cho phép truy cập các cổng sau:
* `2424`: Binary connection.
* `2480`: OrientDB Studio (HTTP).
* `5701`: Hazelcast clustering.

### Bước 4: Khởi chạy
Mở Terminal/PowerShell tại thư mục dự án và chạy lệnh:
```bash
docker-compose up -d
```

### Bước 5: Kiểm tra kết nối
Chạy lệnh sau để xem log và xác nhận Cluster đã nhận diện đủ thành viên:
```bash
docker logs -f orientdb-node
```
Nếu thấy dòng Members {size:4} là thành công.

Link truy cập: http://localhost:2480/studio/index.html#/

## 👨‍💻 Giảng viên hướng dẫn
- Thầy: Nguyễn Minh Nhựt 

## 👨‍💻 Thành viên thực hiện
- Nguyễn Văn Mạnh Huy - 23520641 
- Nguyễn Lê Bảo Ngọc - 23521030
- Lê Vĩnh Thái - 23521417
- Nguyễn Thành Khang - 23520698