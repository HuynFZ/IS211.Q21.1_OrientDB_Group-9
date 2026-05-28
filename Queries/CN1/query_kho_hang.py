from connection_provider import get_client

try:
    # Lấy client đã được kết nối và mở sẵn DB BTL2
    client = get_client()
    
    if client:
        print("\n--- [MÁY 1 - CN1] TRUY VẤN KIỂM TRA ĐIỀU CHUYỂN KHO ---")

        # Câu truy vấn ép trỏ thẳng vào các Cluster phân mảnh vật lý của từng CN
        query = """
        MATCH 
          {class: sach_vpp, as: sp} <-BAO_GOM_CN1- {cluster: co_trong_kho_cn1, as: kho_cn1, where: (SoLuongTon < 5)},
          {as: sp} <-BAO_GOM_CN2- {cluster: co_trong_kho_cn2, as: kho_cn2, where: (SoLuongTon > 10)}
        RETURN 
          sp.MaSP AS MaSanPham, 
          sp.TenSP AS TenSanPham, 
          kho_cn1.SoLuongTon AS Ton_CN1, 
          kho_cn2.SoLuongTon AS Ton_CN2
        """
        
        results = client.command(query)
        
        if not results:
            print("-> Trạng thái: Cân bằng kho. Không có sản phẩm nào cần điều chuyển.")
        else:
            print(f"{'Mã SP':<10} | {'Tên Sản Phẩm':<30} | {'Tồn CN1':<10} | {'Tồn CN2':<10}")
            print("-" * 70)
            for record in results:
                print(f"{record.MaSanPham:<10} | {record.TenSanPham:<30} | {record.Ton_CN1:<10} | {record.Ton_CN2:<10}")

        # Đóng kết nối an toàn sau khi hoàn tất
        client.db_close()
        print("-------------------------------------------------------")

except Exception as e:
    print(f"Lỗi hệ thống khi truy vấn kho: {e}")