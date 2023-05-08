create or replace view  view_QL_NhanVien as 
    select nv.MANV,nv.TENNV,nv.PHAI,nv.NGAYSINH,nv.DIACHI,nv.SODT,nv.VAITRO,nv.MANQL
    from nhanvien nv, username un
    where Upper(un.user_name) = user  and un.MANV = nv.manql;

create or replace view  view_QL_PhanCong as 
    select pc.*
    from nhanvien nv, username un, phancong pc
    where Upper(un.user_name) = user and un.MANV = nv.MANQL and nv.MANV = pc.MANV;
------------
grant select on view_QL_NhanVien to QLTrucTiep;
grant select on view_QL_PhanCong to QLTrucTiep;
grant select on username to QLTrucTiep;
