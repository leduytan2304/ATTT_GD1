select * from system.phongban;


select * from system.DEAN;


select * from system.view_decrypt_NHANVIEN_LUONG;

update system.view_decrypt_NHANVIEN_LUONG set NGAYSINH = TO_DATE('01-01-1990', 'DD-MM-YYYY') where MANV = 'NV0001';


select * from system.View_Select_PhanCong_Info;

select * from system.View_TruongPhong_Select_NhanVien_Info;

call system.INSERT_PHANCONG('NV0009','DA0001',NULL);

EXECUTE system.DELETE_PHANCONG('NV0009', 'DA0001');

EXECUTE system.UPDATE_PHANCONG('NV0003', 'DA0005', TO_DATE('24-12-2022', 'DD-MM-YYYY'));
