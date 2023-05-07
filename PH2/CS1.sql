
create or replace view  view_NV_NhanVien as 
    select n.MANV, n.TENNV, n.PHAI, n.NGAYSINH, n.DIACHI, n.SODT,
    CAST (decrypt_NhanVien(n.LUONG) AS nvarchar2 (255)) as LUONG, 
    CAST (decrypt_NhanVien(n.PHUCAP) AS nvarchar2 (255)) as PHUCAP, n.VAITRO, n.MANQL
    from nhanvien n;

create or replace view  view_NV_PhanCong as 
    select *
    from PhanCong;

Grant SELECT ON view_NV_NhanVien TO NhanVien;
Grant SELECT ON view_NV_PhanCong TO NhanVien;
Grant UPDATE(NGAYSINH, DIACHI, SODT) ON view_NhanVien TO NhanVien;
Grant SELECT ON PHONGBAN TO NhanVien;
Grant SELECT ON DEAN TO NhanVien;