# 2_read.py
from config import get_connection

def run_read():
    client = get_connection()
    print("--- [2] ĐANG THỰC HIỆN READ (TRUY VẤN DỮ LIỆU) ---")

    # Đọc thông tin Khách hàng (Lấy cả địa chỉ lồng nhau)
    kh_data = client.query("SELECT * FROM KHACH_HANG WHERE MaKH = 'KH0001'")
    if kh_data:
        kh = kh_data[0]
        # Xử lý lấy dữ liệu từ Embedded Document
        dia_chi_nhung = kh.DiaChi.get('SoNha', '') + ', ' + kh.DiaChi.get('TinhThanh', '')
        print(f"  [>] Khách hàng: {kh.TenKH} | Địa chỉ: {dia_chi_nhung}")
    else:
        print("  [!] Không tìm thấy Khách hàng KH0001")

    # Truy xuất Graph: Tìm tên sản phẩm từ mã Hóa đơn thông qua Cạnh BAO_GOM
    sp_mua = client.query("SELECT expand(out('BAO_GOM')) FROM HOA_DON WHERE MaHD = 'HD_MB_000001'")
    if sp_mua:
        print(f"  [>] Chi tiết Hóa đơn HD_MB_000001 đã mua sản phẩm: {sp_mua[0].TenSP}")
    else:
        print("  [!] Không tìm thấy Hóa đơn hoặc chưa có Cạnh nối")

    client.db_close()

if __name__ == "__main__":
    run_read()