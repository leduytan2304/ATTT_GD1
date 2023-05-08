
create or replace view  view_NV_NhanVien as 
    select n.MANV, n.TENNV, n.PHAI, n.NGAYSINH, n.DIACHI, n.SODT,
    CAST (decrypt_NhanVien(n.LUONG) AS nvarchar2 (255)) as LUONG, 
    CAST (decrypt_NhanVien(n.PHUCAP) AS nvarchar2 (255)) as PHUCAP, n.VAITRO, n.MANQL
    from nhanvien n;

create or replace view  view_NV_PhanCong as 
    select *
    from PhanCong;

Grant SELECT ON view_NV_NhanVien TO NhanVien;
grant SELECT ON view_NV_NhanVien to NhanVien;
grant SELECT ON view_NV_NhanVien to QLTrucTiep;
grant SELECT ON view_NV_NhanVien to TruongPhong;
grant SELECT ON view_NV_NhanVien to TaiChinh;
grant SELECT ON view_NV_NhanVien to NhanSu;
grant SELECT ON view_NV_NhanVien to TruongDeAn;
grant SELECT ON view_NV_NhanVien to BanGiamDoc;

grant SELECT ON view_NV_PhanCong to NhanVien;
grant SELECT ON view_NV_PhanCong to QLTrucTiep;
grant SELECT ON view_NV_PhanCong to TruongPhong;
grant SELECT ON view_NV_PhanCong to TaiChinh;
grant SELECT ON view_NV_PhanCong to NhanSu;
grant SELECT ON view_NV_PhanCong to TruongDeAn;
grant SELECT ON view_NV_PhanCong to BanGiamDoc;

Grant UPDATE (DIACHI,NGAYSINH,SODT) ON view_NV_NhanVien TO NhanVien;
grant UPDATE (DIACHI,NGAYSINH,SODT) ON view_NV_NhanVien to QLTrucTiep;
grant UPDATE (DIACHI,NGAYSINH,SODT) ON view_NV_NhanVien to TruongPhong;
grant UPDATE (DIACHI,NGAYSINH,SODT) ON view_NV_NhanVien to TaiChinh;
grant UPDATE (DIACHI,NGAYSINH,SODT) ON view_NV_NhanVien to NhanSu;
grant UPDATE (DIACHI,NGAYSINH,SODT) ON view_NV_NhanVien to TruongDeAn;
grant UPDATE (DIACHI,NGAYSINH,SODT) ON view_NV_NhanVien to BanGiamDoc;

grant SELECT ON PHONGBAN to NhanVien;
grant SELECT ON PHONGBAN to QLTrucTiep;
grant SELECT ON PHONGBAN to TruongPhong;
grant SELECT ON PHONGBAN to TaiChinh;
grant SELECT ON PHONGBAN to NhanSu;
grant SELECT ON PHONGBAN to TruongDeAn;
grant SELECT ON PHONGBAN to BanGiamDoc;
  
grant SELECT ON DEAN to NhanVien;
grant SELECT ON DEAN to QLTrucTiep;
grant SELECT ON DEAN to TruongPhong;
grant SELECT ON DEAN to TaiChinh;
grant SELECT ON DEAN to NhanSu;
grant SELECT ON DEAN to TruongDeAn;
grant SELECT ON DEAN to BanGiamDoc;