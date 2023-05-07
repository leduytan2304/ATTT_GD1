<<<<<<< HEAD
--CS#3
--tao view xem nhan vien thuoc phong ban cua truong phong
drop view View_TruongPhong_Select_NhanVien_Info;
CREATE OR REPLACE VIEW View_TruongPhong_Select_NhanVien_Info AS
SELECT NV.MANV, NV.TENNV, NV.PHAI, NV.NGAYSINH, NV.DIACHI, NV.SODT, NV.VAITRO, NV.MANQL, NV.PHG
FROM NHANVIEN NV, PHONGBAN PB, USERNAME USN
WHERE USN.user_name = SYS_CONTEXT ('USERENV', 'SESSION_USER')
AND PB.TRPHG = USN.MANV
AND PB.MAPB = NV.PHG;

--grant quyen xem thong tin tren view xem thong tin nhan vien thuoc phong ban cua truong phong
GRANT SELECT ON View_TruongPhong_Select_NhanVien_Info to truongphong;
=======

--CS#3
--tao view xem nhan vien thuoc phong ban cua truong phong
drop view View_TruongPhong_Select_NhanVien_Info;
CREATE OR REPLACE VIEW View_TruongPhong_Select_NhanVien_Info AS
SELECT NV.MANV, NV.TENNV, NV.PHAI, NV.NGAYSINH, NV.DIACHI, NV.SODT, NV.VAITRO, NV.MANQL, NV.PHG
FROM NHANVIEN NV, PHONGBAN PB, USERNAME USN
WHERE USN.user_name = SYS_CONTEXT ('USERENV', 'SESSION_USER')
AND PB.TRPHG = USN.MANV
AND PB.MAPB = NV.PHG;

--grant quyen xem thong tin tren view xem thong tin nhan vien thuoc phong ban cua truong phong
GRANT SELECT ON View_TruongPhong_Select_NhanVien_Info to truongphong;
>>>>>>> f142fc1cc3f69272582a645d061eeb53397560ec
