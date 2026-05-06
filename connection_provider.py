import pyorient

# Thông tin kết nối (Thay IP bằng IP Radmin của máy giữ DB chính)
HOST = '26.x.x.x' 
PORT = 2424  # Cổng Binary mặc định của OrientDB
USER = 'root'
PASS = 'admin' # Mật khẩu đặt lúc chạy server.bat lần đầu
DB_NAME = 'BaiTapPhanTan'

def get_client():
    try:
        client = pyorient.OrientDB(HOST, PORT)
        client.connect(USER, PASS)
        print(f"Kết nối thành công đến Server {HOST}")
        
        # Mở Database
        client.db_open(DB_NAME, USER, PASS)
        return client
    except Exception as e:
        print(f"Lỗi kết nối: {e}")
        return None