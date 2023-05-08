ALTER SESSION SET "_ORACLE_SCRIPT"=TRUE; 
ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MM-YYYY';

alter table PHONGBAN
drop constraint fk_trphg;

create
-- drop
table NHANVIEN
(
    MANV VARCHAR2(10),
    TENNV VARCHAR2(50),
    PHAI VARCHAR2(10),
    NGAYSINH DATE,
    DIACHI VARCHAR2(50),
    SODT NUMBER(12),
    LUONG VARCHAR(4000),
    PHUCAP VARCHAR(4000),
    VAITRO VARCHAR2(20),
    MANQL VARCHAR2(10),
    PHG VARCHAR2(10),
    CONSTRAINT nv_pk PRIMARY KEY (MANV)
);

create
-- drop
table PHONGBAN
(
    MAPB VARCHAR2(10),
    TENPB VARCHAR2(50),
    TRPHG VARCHAR2(10),
    CONSTRAINT pb_pk PRIMARY KEY (MAPB)
);

create
--drop
table DEAN
(
    MADA VARCHAR2(10),
    TENDA VARCHAR2(50),
    NGAYBD DATE, 
    PHONG VARCHAR2(10),
    CONSTRAINT da_pk PRIMARY KEY (MADA)
);

create
--drop 
table PHANCONG 
(
    MANV VARCHAR2(10),
    MADA VARCHAR2(10),
    THOIGIAN DATE,
    CONSTRAINT pc_pk PRIMARY KEY (MANV, MADA)
);

create
--drop
table USERNAME
(
    user_name VARCHAR2(10),
    MANV VARCHAR2(10),
    
    CONSTRAINT usn_pk PRIMARY KEY (user_name, MANV)
);


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
    
alter table USERNAME
add constraint fk_usn_nv
    foreign key(MANV)
    references NHANVIEN(MANV);

-- ma hoa khi insert luong
CREATE OR REPLACE TRIGGER ENCRYPT_NHANVIEN_LUONG_INSERT
BEFORE INSERT ON NHANVIEN
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
    :new.LUONG := input_string;
END;

-- ma hoa khi update luong
CREATE OR REPLACE TRIGGER ENCRYPT_NHANVIEN_LUONG_UPDATE
BEFORE UPDATE ON NHANVIEN
FOR EACH ROW
WHEN (new.LUONG != old.LUONG)
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
    :new.LUONG := input_string;
END;
/

-- ma hoa khi insert phu cap
CREATE OR REPLACE TRIGGER ENCRYPT_NHANVIEN_PHUCAP_INSERT
BEFORE INSERT ON NHANVIEN
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
    :new.PHUCAP := input_string;
END;

-- ma hoa khi update phu cap
CREATE OR REPLACE TRIGGER ENCRYPT_NHANVIEN_PHUCAP_UPDATE
BEFORE UPDATE ON NHANVIEN
FOR EACH ROW
WHEN (new.PHUCAP != old.PHUCAP)
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
    :new.PHUCAP := input_string;
END;


insert all
    into PHONGBAN (MAPB, TENPB, TRPHG) values ('PB001', 'Ke toan', NULL)
    into PHONGBAN (MAPB, TENPB, TRPHG) values ('PB002', 'Hanh chinh', NULL)
    into PHONGBAN (MAPB, TENPB, TRPHG) values ('PB003', 'Nhan su', NULL)
    into PHONGBAN (MAPB, TENPB, TRPHG) values ('PB004', 'Marketing', NULL)
select * from dual;

insert all
    into NHANVIEN values ('NV0001', 'Nguyen Van A', 'Nam', TO_DATE('01-01-1990', 'DD-MM-YYYY'), NULL, NULL, 7000, 700, 'Truong phong', NULL, 'PB001')
    into NHANVIEN values ('NV0005', 'Kha Vinh F', 'Nam', TO_DATE('05-05-1991', 'DD-MM-YYYY'), NULL, NULL, 7200, 700, 'Truong phong', NULL, 'PB002')
    into NHANVIEN values ('NV00011', 'Tran Kieu G', 'Nu', TO_DATE('11-11-1988', 'DD-MM-YYYY'), NULL, NULL, 7100, 700, 'Truong phong', NULL, 'PB003')
    into NHANVIEN values ('NV0006', 'Dinh Tien H', 'Nam', TO_DATE('06-06-1988', 'DD-MM-YYYY'), NULL, NULL, 7000, 700, 'Truong phong', NULL, 'PB004')
    into NHANVIEN values ('NV0002', 'Nguyen Mai B', 'Nu', TO_DATE('03-03-1995', 'DD-MM-YYYY'), NULL, NULL, 5500, 500, 'QL truc tiep', NULL, 'PB003')
    into NHANVIEN values ('NV0004', 'Dinh Phan D', 'Nam', TO_DATE('04-04-1995', 'DD-MM-YYYY'), NULL, NULL, 5300, 500, 'QL truc tiep', NULL, 'PB001')
    into NHANVIEN values ('NV0013', 'Phan Thi E', 'Nu', TO_DATE('13-01-1994', 'DD-MM-YYYY'), NULL, NULL, 5500, 500, 'QL truc tiep', NULL, 'PB004')
    into NHANVIEN values ('NV0003', 'Nguyen Tien I', 'Nam', TO_DATE('03-03-1993', 'DD-MM-YYYY'), NULL, NULL, 5300, 500, 'QL truc tiep', NULL, 'PB002')
    into NHANVIEN values ('NV00010', 'Tran Hoang J', 'Nam', TO_DATE('10-10-1998', 'DD-MM-YYYY'), NULL, NULL, 4000, 300, 'Nhan vien', 'NV0002', 'PB003')
    into NHANVIEN values ('NV0008', 'Do Thi K', 'Nu', TO_DATE('08-08-1997', 'DD-MM-YYYY'), NULL, NULL, 4100, 700, 'Nhan vien', 'NV0013', 'PB004')
    into NHANVIEN values ('NV0007', 'Nguyen Van L', 'Nam', TO_DATE('07-07-1998', 'DD-MM-YYYY'), NULL, NULL, 4000, 300, 'Nhan vien', 'NV0013', 'PB004')
    into NHANVIEN values ('NV0009', 'Mai Tuyet M', 'Nu', TO_DATE('09-09-1999', 'DD-MM-YYYY'), NULL, NULL, 3900, 300, 'Nhan vien', 'NV0004', 'PB001')
    into NHANVIEN values ('NV00012', 'Hoang Kieu N', 'Nu', TO_DATE('12-12-1997', 'DD-MM-YYYY'), NULL, NULL, 4100, 300, 'Nhan vien', 'NV0003', 'PB002')
    into NHANVIEN values ('NV00017', 'Nguyen Hoang O', 'Nam', TO_DATE('06-01-1997', 'DD-MM-YYYY'), NULL, NULL, 4000, 300, 'Tai chinh', 'NV0004', 'PB001')
    into NHANVIEN values ('NV00014', 'Do Minh P', 'Nam', TO_DATE('15-08-1996', 'DD-MM-YYYY'), NULL, NULL, 4100, 700, 'Nhan su', 'NV0002', 'PB003')
    into NHANVIEN values ('NV00016', 'Nguyen Van Q', 'Nam', TO_DATE('25-02-1997', 'DD-MM-YYYY'), NULL, NULL, 4000, 300, 'Truong de an', 'NV0003', 'PB002')
    into NHANVIEN values ('NV00015', 'Mai Van S', 'Nu', TO_DATE('31-03-1998', 'DD-MM-YYYY'), NULL, NULL, 3900, 300, 'Nhan su', 'NV0002', 'PB003')
    into NHANVIEN values ('NV00018', 'Hoang Minh T', 'Nu', TO_DATE('02-12-1997', 'DD-MM-YYYY'), NULL, NULL, 4100, 300, 'Tai chinh', 'NV0004', 'PB001')
    into NHANVIEN values ('NV00019', 'Phan Mai U', 'Nu', TO_DATE('12-01-1986', 'DD-MM-YYYY'), NULL, NULL, 10000, 1000, 'Ban giam doc', NULL, NULL)
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
    into PHANCONG values ('NV0013', 'DA0005', TO_DATE('14-11-2022', 'DD-MM-YYYY'))
    into PHANCONG values ('NV00012', 'DA0002', TO_DATE('03-02-2023', 'DD-MM-YYYY'))
    into PHANCONG values ('NV0002', 'DA0004', TO_DATE('02-02-2023', 'DD-MM-YYYY'))
    into PHANCONG values ('NV0007', 'DA0001', TO_DATE('12-12-2022', 'DD-MM-YYYY'))
    into PHANCONG values ('NV0003', 'DA0005', TO_DATE('14-11-2022', 'DD-MM-YYYY'))
select * from dual;

insert all
    into USERNAME values ('nv1', 'NV0001')
    into USERNAME values ('nv2', 'NV0002')
    into USERNAME values ('nv3', 'NV0003')
    into USERNAME values ('nv4', 'NV0004')
    into USERNAME values ('nv5', 'NV0005')
    into USERNAME values ('nv6', 'NV0006')
    into USERNAME values ('nv7', 'NV0007')
    into USERNAME values ('nv8', 'NV0008')
    into USERNAME values ('nv9', 'NV0009')
    into USERNAME values ('nv10', 'NV00010')
    into USERNAME values ('nv11', 'NV00011')
    into USERNAME values ('nv12', 'NV00012')
    into USERNAME values ('nv13', 'NV0013')
    into USERNAME values ('nv14', 'NV00014')
    into USERNAME values ('nv15', 'NV00015')
    into USERNAME values ('nv16', 'NV00016')
    into USERNAME values ('nv17', 'NV00017')
    into USERNAME values ('nv18', 'NV00018')
    into USERNAME values ('nv19', 'NV00019')
select * from dual;