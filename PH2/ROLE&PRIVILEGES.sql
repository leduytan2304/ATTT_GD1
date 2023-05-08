alter session set "_ORACLE_SCRIPT"=true;

create user nv1 identified by 1;
create user nv2 identified by 1;
create user nv3 identified by 1;
create user nv4 identified by 1;
create user nv5 identified by 1;
create user nv6 identified by 1;
create user nv7 identified by 1;
create user nv8 identified by 1;
create user nv9 identified by 1;
create user nv10 identified by 1;
create user nv11 identified by 1;
create user nv12 identified by 1;
create user nv13 identified by 1;
create user nv14 identified by 1;
create user nv15 identified by 1;
create user nv16 identified by 1;
create user nv17 identified by 1;
create user nv18 identified by 1;
create user nv19 identified by 1;

create role NhanVien;
create role QLTrucTiep;
create role TruongPhong;
create role TaiChinh;
create role NhanSu;
create role TruongDeAn;
create role BanGiamDoc;

grant NhanVien to nv10, nv8, nv7, nv9, nv12;
grant QLTrucTiep to nv2, nv4, nv13, nv3;
grant NhanVien to nv2, nv4, nv13, nv3;
grant TruongPhong to nv1, nv5, nv11, nv6;
grant TaiChinh to nv17, nv18;
grant NhanSu to nv14, nv15;
grant TruongDeAn to nv16;
grant BanGiamDoc to nv19;

grant create session to NhanVien;
grant create session to QLTrucTiep;
grant create session to TruongPhong;
grant create session to TaiChinh;
grant create session to NhanSu;
grant create session to TruongDeAn;
grant create session to BanGiamDoc;