ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MM-YYYY';
DROP TABLE NHANVIEN;
create table NHANVIEN
(
    MANV VARCHAR2(10),
    TENNV VARCHAR2(50),
    PHAI VARCHAR2(10),
    NGAYSINH DATE,
    DIACHI VARCHAR2(50),
    SODT NUMBER(12),
    LUONG VARCHAR2(4000),
    PHUCAP VARCHAR2(4000),
    VAITRO VARCHAR2(20),
    MANQL VARCHAR2(10),
    PHG VARCHAR2(10),
    CONSTRAINT nv_pk PRIMARY KEY (MANV)
);


DROP TABLE PHONGBAN;
create table PHONGBAN
(
    MAPB VARCHAR2(10),
    TENPB VARCHAR2(50),
    TRPHG VARCHAR2(10),
    CONSTRAINT pb_pk PRIMARY KEY (MAPB)
);

DROP TABLE DEAN;
create table DEAN
(
    MADA VARCHAR2(10),
    TENDA VARCHAR2(50),
    NGAYBD DATE, 
    PHONG VARCHAR2(10),
    CONSTRAINT da_pk PRIMARY KEY (MADA)
);

DROP TABLE PHANCONG;
create table PHANCONG 
(
    MANV VARCHAR2(10),
    MADA VARCHAR2(10),
    THOIGIAN DATE,
    CONSTRAINT pc_pk PRIMARY KEY (MANV, MADA)
);

DROP TABLE USERNAME;
create table USERNAME
(
    user_name VARCHAR2(10),
    MANV VARCHAR2(10),
    
    CONSTRAINT usn_pk PRIMARY KEY (user_name, MANV)
);

alter table USERNAME
add constraint fk_usn_nv
    foreign key(MANV)
    references NHANVIEN(MANV);

alter table NHANVIEN
add constraint fk_manql
    foreign key(MANQL)
    references NHANVIEN(MANV);

alter table NHANVIEN
add constraint fk_phg
    foreign key(PHG)
    references PHONGBAN(MAPB);

alter table PHONGBAN
add constraint fk_trphg
    foreign key(TRPHG)
    references NHANVIEN(MANV);

alter table DEAN
add constraint fk_phong
    foreign key(PHONG)
    references PHONGBAN(MAPB);

alter table PHANCONG
add constraint fk_nv_pc
    foreign key(MANV)
    references NHANVIEN(MANV);

alter table PHANCONG
add constraint fk_nv_da
    foreign key(MADA)
    references DEAN(MADA);

--trigger ma hoa luong
drop trigger ENCRYPT_NHANVIEN_LUONG;
CREATE OR REPLACE TRIGGER ENCRYPT_NHANVIEN_LUONG
BEFORE INSERT OR UPDATE ON NHANVIEN
FOR EACH ROW
DECLARE
    input_string VARCHAR2(200);
    encrypted_raw RAW (2000); -- stores encrypted binary text
    v_key raw(128) := utl_i18n.string_to_raw( 'ATBMCQ-05', 'AL32UTF8' );
    encryption_type PLS_INTEGER := SYS.DBMS_CRYPTO.ENCRYPT_DES + SYS.DBMS_CRYPTO.CHAIN_CBC + SYS.DBMS_CRYPTO.PAD_PKCS5;
BEGIN
    input_string := TO_CHAR(:new.LUONG);
    encrypted_raw := DBMS_CRYPTO.ENCRYPT
          (
             src => UTL_I18N.STRING_TO_RAW (input_string,'AL32UTF8'),
             typ => encryption_type,
             key => v_key
         );
    input_string := RAWTOHEX(encrypted_raw);
    :new.LUONG := TO_NCHAR(input_string);
END;

--trigger ma hoa phu cap
drop trigger ENCRYPT_NHANVIEN_PHUCAP;
CREATE OR REPLACE TRIGGER ENCRYPT_NHANVIEN_PHUCAP
BEFORE INSERT OR UPDATE ON NHANVIEN
FOR EACH ROW
DECLARE
    input_string VARCHAR2(200);
    encrypted_raw RAW (2000); -- stores encrypted binary text
    v_key raw(128) := utl_i18n.string_to_raw( 'ATBMCQ-05', 'AL32UTF8' );
    encryption_type PLS_INTEGER := SYS.DBMS_CRYPTO.ENCRYPT_DES + SYS.DBMS_CRYPTO.CHAIN_CBC + SYS.DBMS_CRYPTO.PAD_PKCS5;
BEGIN
    input_string := TO_CHAR(:new.PHUCAP);
    encrypted_raw := DBMS_CRYPTO.ENCRYPT
          (
             src => UTL_I18N.STRING_TO_RAW (input_string,'AL32UTF8'),
             typ => encryption_type,
             key => v_key
         );
    input_string := RAWTOHEX(encrypted_raw);
    :new.PHUCAP := TO_NCHAR(input_string);
END;

--function giai ma
drop function decrypt_LUONG_PHUCAP;
create or replace function decrypt_LUONG_PHUCAP (p_data in nvarchar2)  
    return varchar2  
as
	input_string VARCHAR2(200);
    output_string VARCHAR2 (200);
    decrypted_raw RAW (2000); -- stores decrypted binary text
    v_key raw(128) := utl_i18n.string_to_raw( 'ATBMCQ-05', 'AL32UTF8' );
    encryption_type PLS_INTEGER := SYS.DBMS_CRYPTO.ENCRYPT_DES + SYS.DBMS_CRYPTO.CHAIN_CBC + SYS.DBMS_CRYPTO.PAD_PKCS5;
begin
	input_string := TO_CHAR(p_data);  
    decrypted_raw := DBMS_CRYPTO.Decrypt
        (
            src => HEXTORAW(input_string),
            typ => encryption_type,
            key => v_key
        );
    input_string := UTL_I18N.RAW_TO_CHAR (decrypted_raw, 'AL32UTF8');
	output_string := TO_CHAR(input_string);
    return output_string; 
end;

-- view xem bang NHANVIEN da giai ma
drop view view_decrypt_NHANVIEN_LUONG;
create or replace view  view_decrypt_NHANVIEN_LUONG as 
    select nv.MANV, nv.TENNV, nv.PHAI, nv.NGAYSINH, nv.DIACHI, nv.SODT, CAST (decrypt_LUONG_PHUCAP(nv.LUONG) AS varchar2 (4000)) LUONG, 
    CAST (decrypt_LUONG_PHUCAP(nv.PHUCAP) AS varchar2 (4000)) PHUCAP, nv.VAITRO, nv.MANQL, nv.PHG
    from NHANVIEN nv;

insert all
    into PHONGBAN (MAPB, TENPB, TRPHG) values ('PB001', 'Ke toan', NULL)
    into PHONGBAN (MAPB, TENPB, TRPHG) values ('PB002', 'Hanh chinh', NULL)
    into PHONGBAN (MAPB, TENPB, TRPHG) values ('PB003', 'Nhan su', NULL)
    into PHONGBAN (MAPB, TENPB, TRPHG) values ('PB004', 'Marketing', NULL)
select * from dual;


insert all
    into NHANVIEN values ('NV0001', 'Nguyen Van A', 'Nam', TO_DATE('01-01-1990', 'DD-MM-YYYY'), NULL, NULL, '7000', '700', 'Truong phong', NULL, 'PB001')
    into NHANVIEN values ('NV0005', 'Kha Vinh F', 'Nam', TO_DATE('05-05-1991', 'DD-MM-YYYY'), NULL, NULL, '7200', '700', 'Truong phong', NULL, 'PB002')
    into NHANVIEN values ('NV00011', 'Tran Kieu G', 'Nu', TO_DATE('11-11-1988', 'DD-MM-YYYY'), NULL, NULL, '7100', '700', 'Truong phong', NULL, 'PB003')
    into NHANVIEN values ('NV0006', 'Dinh Tien H', 'Nam', TO_DATE('06-06-1988', 'DD-MM-YYYY'), NULL, NULL, '7000', '700', 'Truong phong', NULL, 'PB004')
    into NHANVIEN values ('NV0002', 'Nguyen Mai B', 'Nu', TO_DATE('03-03-1995', 'DD-MM-YYYY'), NULL, NULL, '5500', '500', 'QL truc tiep', NULL, 'PB003')
    into NHANVIEN values ('NV0004', 'Dinh Phan D', 'Nam', TO_DATE('04-04-1995', 'DD-MM-YYYY'), NULL, NULL, '5300', '500', 'QL truc tiep', NULL, 'PB001')
    into NHANVIEN values ('NV00013', 'Phan Thi E', 'Nu', TO_DATE('13-01-1994', 'DD-MM-YYYY'), NULL, NULL, '5500', '500', 'QL truc tiep', NULL, 'PB004')
    into NHANVIEN values ('NV0003', 'Nguyen Tien I', 'Nam', TO_DATE('03-03-1993', 'DD-MM-YYYY'), NULL, NULL, '3000', '500', 'QL truc tiep', NULL, 'PB002')
    into NHANVIEN values ('NV00010', 'Tran Hoang J', 'Nam', TO_DATE('10-10-1998', 'DD-MM-YYYY'), NULL, NULL, '4000', '300', 'Nhan vien', 'NV0002', 'PB003')
    into NHANVIEN values ('NV0008', 'Do Thi K', 'Nu', TO_DATE('08-08-1997', 'DD-MM-YYYY'), NULL, NULL, '4100', '700', 'Nhan vien', 'NV00013', 'PB004')
    into NHANVIEN values ('NV0007', 'Nguyen Van L', 'Nam', TO_DATE('07-07-1998', 'DD-MM-YYYY'), NULL, NULL, '4000', '300', 'Nhan vien', 'NV00013', 'PB004')
    into NHANVIEN values ('NV0009', 'Mai Tuyet M', 'Nu', TO_DATE('09-09-1999', 'DD-MM-YYYY'), NULL, NULL, '3900', '300', 'Nhan vien', 'NV0004', 'PB001')
    into NHANVIEN values ('NV00012', 'Hoang Kieu N', 'Nu', TO_DATE('12-12-1997', 'DD-MM-YYYY'), NULL, NULL, '4100', '300', 'Nhan vien', 'NV0003', 'PB002')
    into NHANVIEN values ('NV00017', 'Nguyen Hoang O', 'Nam', TO_DATE('06-01-1997', 'DD-MM-YYYY'), NULL, NULL, '4000', '300', 'Tai chinh', 'NV0004', 'PB001')
    into NHANVIEN values ('NV00014', 'Do Minh P', 'Nam', TO_DATE('15-08-1996', 'DD-MM-YYYY'), NULL, NULL, '4100', '700', 'Nhan su', 'NV0002', 'PB003')
    into NHANVIEN values ('NV00016', 'Nguyen Van Q', 'Nam', TO_DATE('25-02-1997', 'DD-MM-YYYY'), NULL, NULL, '4000', '300', 'Truong de an', 'NV0003', 'PB002')
    into NHANVIEN values ('NV00015', 'Mai Van S', 'Nu', TO_DATE('31-03-1998', 'DD-MM-YYYY'), NULL, NULL, '3900', '300', 'Nhan su', 'NV0002', 'PB003')
    into NHANVIEN values ('NV00018', 'Hoang Minh T', 'Nu', TO_DATE('02-12-1997', 'DD-MM-YYYY'), NULL, NULL, '4100', '300', 'Tai chinh', 'NV0004', 'PB001')
    into NHANVIEN values ('NV00019', 'Phan Mai U', 'Nu', TO_DATE('12-01-1986', 'DD-MM-YYYY'), NULL, NULL, '10000', '1000', 'Ban giam doc', NULL, NULL)
select * from dual;

update PHONGBAN set TRPHG = 'NV0001' where MAPB = 'PB001';
update PHONGBAN set TRPHG = 'NV0005' where MAPB = 'PB002';
update PHONGBAN set TRPHG = 'NV00011' where MAPB = 'PB003';
update PHONGBAN set TRPHG = 'NV0006' where MAPB = 'PB004';


insert all
    into DEAN values ('DA0001', 'De an 1', TO_DATE('12-12-2022', 'DD-MM-YYYY'), 'PB003')
    into DEAN values ('DA0002', 'De an 2', TO_DATE('03-02-2023', 'DD-MM-YYYY'), 'PB001')
    into DEAN values ('DA0003', 'De an 3', TO_DATE('01-05-2023', 'DD-MM-YYYY'), 'PB004')
    into DEAN values ('DA0004', 'De an 4', TO_DATE('02-02-2023', 'DD-MM-YYYY'), 'PB002')
    into DEAN values ('DA0005', 'De an 5', TO_DATE('14-11-2022', 'DD-MM-YYYY'), 'PB001')
select * from dual;

insert all
    into PHANCONG values ('NV0004', 'DA0004', TO_DATE('02-02-2023', 'DD-MM-YYYY'))
    into PHANCONG values ('NV00010', 'DA0001', TO_DATE('12-12-2022', 'DD-MM-YYYY'))
    into PHANCONG values ('NV0008', 'DA0003', TO_DATE('01-05-2023', 'DD-MM-YYYY'))
    into PHANCONG values ('NV0009', 'DA0002', TO_DATE('03-02-2023', 'DD-MM-YYYY'))
    into PHANCONG values ('NV00013', 'DA0005', TO_DATE('14-11-2022', 'DD-MM-YYYY'))
    into PHANCONG values ('NV00012', 'DA0002', TO_DATE('03-02-2023', 'DD-MM-YYYY'))
    into PHANCONG values ('NV0002', 'DA0004', TO_DATE('02-02-2023', 'DD-MM-YYYY'))
    into PHANCONG values ('NV0007', 'DA0001', TO_DATE('12-12-2022', 'DD-MM-YYYY'))
    into PHANCONG values ('NV0003', 'DA0005', TO_DATE('14-11-2022', 'DD-MM-YYYY'))
select * from dual;
    
insert all
    into USERNAME values ('NV1', 'NV0001')
    into USERNAME values ('NV2', 'NV0002')
    into USERNAME values ('NV3', 'NV0003')
    into USERNAME values ('NV4', 'NV0004')
    into USERNAME values ('NV5', 'NV0005')
    into USERNAME values ('NV6', 'NV0006')
    into USERNAME values ('NV7', 'NV0007')
    into USERNAME values ('NV8', 'NV0008')
    into USERNAME values ('NV9', 'NV0009')
    into USERNAME values ('NV10', 'NV00010')
    into USERNAME values ('NV11', 'NV00011')
    into USERNAME values ('NV12', 'NV00012')
    into USERNAME values ('NV13', 'NV00013')
    into USERNAME values ('NV14', 'NV00014')
    into USERNAME values ('NV15', 'NV00015')
    into USERNAME values ('NV16', 'NV00016')
    into USERNAME values ('NV17', 'NV00017')
    into USERNAME values ('NV18', 'NV00018')
    into USERNAME values ('NV19', 'NV00019')
select * from dual;



alter session set "_ORACLE_SCRIPT"=true;

--tao user
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

--tao role
create role NhanVien;
create role QLTrucTiep;
create role TruongPhong;
create role TaiChinh;
create role NhanSu;
create role TruongDeAn;
create role BanGiamDoc;

--gan role
grant NhanVien to nv10, nv8, nv7, nv9, nv12;
grant QLTrucTiep to nv2, nv4, nv13, nv3;
grant TruongPhong to nv1, nv5, nv11, nv6;
grant TaiChinh to nv17, nv18;
grant NhanSu to nv14, nv15;
grant TruongDeAn to nv16;
grant BanGiamDoc to nv19;



--cs3
alter session set "_ORACLE_SCRIPT"=true;

grant create session to public

--gan quyen xem nhan vien
grant SELECT ON NHANVIEN to nhanvien;
grant SELECT ON NHANVIEN to qltructiep;
grant SELECT ON NHANVIEN to truongphong;
grant SELECT ON NHANVIEN to taichinh;
grant SELECT ON NHANVIEN to nhansu;
grant SELECT ON NHANVIEN to truongdean;

--gan quyen xem phan cong
grant SELECT ON PHANCONG to nhanvien;
grant SELECT ON PHANCONG to qltructiep;
grant SELECT ON PHANCONG to truongphong;
grant SELECT ON PHANCONG to taichinh;
grant SELECT ON PHANCONG to nhansu;
grant SELECT ON PHANCONG to truongdean;

--gan quyen xem phong ban
grant SELECT ON PHONGBAN to nhanvien;
grant SELECT ON PHONGBAN to qltructiep;
grant SELECT ON PHONGBAN to truongphong;
grant SELECT ON PHONGBAN to taichinh;
grant SELECT ON PHONGBAN to nhansu;
grant SELECT ON PHONGBAN to truongdean;

--gan quyen xem de an
grant SELECT ON DEAN to nhanvien;
grant SELECT ON DEAN to qltructiep;
grant SELECT ON DEAN to truongphong;
grant SELECT ON DEAN to taichinh;
grant SELECT ON DEAN to nhansu;
grant SELECT ON DEAN to truongdean;

--gan quyen xem view nhan vien(xem thong tin cua chinh minh)
grant select on view_decrypt_NHANVIEN_LUONG to nhanvien;
grant select on view_decrypt_NHANVIEN_LUONG to qltructiep;
grant select on view_decrypt_NHANVIEN_LUONG to truongphong;
grant select on view_decrypt_NHANVIEN_LUONG to taichinh;
grant select on view_decrypt_NHANVIEN_LUONG to nhansu;
grant select on view_decrypt_NHANVIEN_LUONG to truongdean;

--cach chay: select * from system.view_decrypt_NHANVIEN_LUONG;


--tra ve ma nhan vien khi dang nhap
drop function Select_NhanVien;
create or replace function Select_NhanVien(p_schema IN VARCHAR2, p_object IN VARCHAR2)
return varchar2
is
    login_user varchar2(255);
begin
    declare temp varchar2(10);
    begin
        temp := SYS_CONTEXT('userenv', 'SESSION_USER');
        if temp = 'SYS' or temp = 'SYSTEM' then
            login_user := '1=1';
            return login_user;
        else
            select MANV into login_user from system.USERNAME where user_name = temp;
            return 'MANV = '''||login_user||'''';
        end if;
    end;
end;

--xem thong tin nhan vien cua chinh minh
BEGIN
  DBMS_RLS.ADD_POLICY (
    object_schema   => 'system',
    object_name     => 'view_decrypt_NHANVIEN_LUONG',
    policy_name     => 'NHANVIEN_Select_Info',
    function_schema => 'system',
    policy_function => 'Select_NhanVien',
    statement_types => 'SELECT',
    update_check    => TRUE
  );
END;

--drop policy
begin
    DBMS_RLS.DROP_POLICY (
        object_schema   => 'system',
        object_name     => 'View_Select_NhanVien_Info',
        policy_name     => 'NHANVIEN_Select_Info');
end;

--grant quyen update tren cac cot cua nhan vien
grant update (NGAYSINH, DIACHI, SODT) on NHANVIEN to NhanVien;
grant update (NGAYSINH, DIACHI, SODT) on NHANVIEN to qltructiep;
grant update (NGAYSINH, DIACHI, SODT) on NHANVIEN to truongphong;
grant update (NGAYSINH, DIACHI, SODT) on NHANVIEN to taichinh;
grant update (NGAYSINH, DIACHI, SODT) on NHANVIEN to nhansu;
grant update (NGAYSINH, DIACHI, SODT) on NHANVIEN to truongdean;


--update thong tin cua minh
BEGIN
  DBMS_RLS.ADD_POLICY (
    object_schema   => 'system',
    object_name     => 'NHANVIEN',
    policy_name     => 'NHANVIEN_Update_Col',
    function_schema => 'system',
    policy_function => 'Select_NhanVien',
    statement_types => 'UPDATE',
    update_check    => TRUE
  );
END;

--drop policy update
begin
    DBMS_RLS.DROP_POLICY (
        object_schema   => 'system',
        object_name     => 'NHANVIEN',
        policy_name     => 'NHANVIEN_Update_Col');
end;


--xem thong tin phan cong cua minh
drop view View_Select_PhanCong_Info;
CREATE OR REPLACE VIEW View_Select_PhanCong_Info AS
SELECT PC.*
FROM PHANCONG PC

--cach chay: select * from system.View_Select_PhanCong_Info;

BEGIN
  DBMS_RLS.ADD_POLICY (
    object_schema   => 'system',
    object_name     => 'View_Select_PhanCong_Info',
    policy_name     => 'PHANCONG_Select_Info',
    function_schema => 'system',
    policy_function => 'Select_NhanVien',
    statement_types => 'SELECT',
    update_check    => TRUE
  );
END;

--grant quyen xem view phan cong
grant select on View_Select_PhanCong_Info to nhanvien;
grant select on View_Select_PhanCong_Info to qltructiep;
grant select on View_Select_PhanCong_Info to truongphong;
grant select on View_Select_PhanCong_Info to taichinh;
grant select on View_Select_PhanCong_Info to nhansu;
grant select on View_Select_PhanCong_Info to truongdean;

--drop policy
begin
    DBMS_RLS.DROP_POLICY (
        object_schema   => 'system',
        object_name     => 'PHANCONG',
        policy_name     => 'PHANCONG_Select_Info');
end;
