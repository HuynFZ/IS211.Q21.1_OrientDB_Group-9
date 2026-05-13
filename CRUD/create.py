# 1_create.py
from config import get_connection

def run_create():
    client = get_connection()
    print("--- [1] ĐANG THỰC HIỆN CREATE (THÊM DỮ LIỆU) ---")

    # 1. Tạo Khách hàng
    client.command("""
        CREATE VERTEX KHACH_HANG CONTENT {
            "MaKH": "KH0001",
            "TenKH": "Lê Hữu Oanh",
            "SoDienThoai": "0960770941",
            "DiemTichLuy": 653,
            "DiaChi": {
                "@class": "DiaChiDetail",
                "SoNha": "Số 464 Đường số 27",
                "TinhThanh": "Việt Nam"
            }
        }
    """)

    # 2. Tạo Sản phẩm & Hóa đơn
    client.command("CREATE VERTEX SACH_VPP SET MaSP = 'SP0001', TenSP = 'Cây Cam Ngọt Của Tôi', GiaBan = 230000")
    client.command("CREATE VERTEX HOA_DON SET MaHD = 'HD_MB_000001', TongTien = 2300000")

    # 3. Nối Cạnh
    client.command("""
        CREATE EDGE CUA_KHACH_HANG 
        FROM (SELECT FROM HOA_DON WHERE MaHD = 'HD_MB_000001') 
        TO (SELECT FROM KHACH_HANG WHERE MaKH = 'KH0001')
    """)
    client.command("""
        CREATE EDGE BAO_GOM 
        FROM (SELECT FROM HOA_DON WHERE MaHD = 'HD_MB_000001') 
        TO (SELECT FROM SACH_VPP WHERE MaSP = 'SP0001')
        SET SoLuong = 10, DonGia = 230000, ThanhTien = 2300000
    """)
    
    print("  [+] Đã tạo xong Khách hàng, Sản phẩm, Hóa đơn và Nối Cạnh thành công.")
    client.db_close()

if __name__ == "__main__":
    run_create()