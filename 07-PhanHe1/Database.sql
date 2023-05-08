--chuyen date thanh dang dd-mm-yyyy
ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MM-YYYY';
--cho phep tao user
alter session set "_ORACLE_SCRIPT"=true;



--neu ton tai bang NHANVIEN, thuc hien DROP TABLE NHANVIEN
DECLARE
    exist_check_07 INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO exist_check_07
    FROM USER_OBJECTS
    WHERE OBJECT_NAME = 'NHANVIEN' AND OBJECT_TYPE = 'TABLE'; --- Kiem tra co TABLE nao trung ten nay khong
    IF exist_check_07> 0 THEN --- Neu bien count khac khong tuc la co ton tai
        EXECUTE IMMEDIATE 'DROP TABLE NHANVIEN'; --- Thuc hien lenh DROP TABLE
        dbms_output.put_line( 'Table droppped' );
    END IF;
END;
/
--neu ton tai bang PHONGBAN, thuc hien DROP TABLE PHONGBAN
DECLARE
    exist_check_07 INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO exist_check_07
    FROM USER_OBJECTS
    WHERE OBJECT_NAME = 'PHONGBAN' AND OBJECT_TYPE = 'TABLE'; --- Kiem tra co TABLE nao trung ten nay khong
    IF exist_check_07> 0 THEN --- Neu bien count khac khong tuc la co ton tai
        EXECUTE IMMEDIATE 'DROP TABLE PHONGBAN'; --- Thuc hien lenh DROP TABLE
        dbms_output.put_line( 'Table droppped' );
    END IF;
END;
/

--neu ton tai bang DEAN, thuc hien DROP TABLE DEAN
DECLARE
    exist_check_07 INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO exist_check_07
    FROM USER_OBJECTS
    WHERE OBJECT_NAME = 'DEAN' AND OBJECT_TYPE = 'TABLE'; --- Kiem tra co TABLE nao trung ten nay khong
    IF exist_check_07> 0 THEN --- Neu bien count khac khong tuc la co ton tai
        EXECUTE IMMEDIATE 'DROP TABLE DEAN'; --- Thuc hien lenh DROP TABLE
        dbms_output.put_line( 'Table droppped' );
    END IF;
END;
/


--neu ton tai bang PHANCONG, thuc hien DROP TABLE PHANCONG
DECLARE
    exist_check_07 INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO exist_check_07
    FROM USER_OBJECTS
    WHERE OBJECT_NAME = 'PHANCONG' AND OBJECT_TYPE = 'TABLE'; --- Kiem tra co TABLE nao trung ten nay khong
    IF exist_check_07> 0 THEN --- Neu bien count khac khong tuc la co ton tai
        EXECUTE IMMEDIATE 'DROP TABLE PHANCONG'; --- Thuc hien lenh DROP TABLE
        dbms_output.put_line( 'Table droppped' );
    END IF;
END;
/




--tao bang NHANVIEN
CREATE TABLE NHANVIEN (
   MANV VARCHAR2(10) NOT NULL PRIMARY KEY,
   TENNV VARCHAR2(30),
   PHAI VARCHAR2(10),
   NGAYSINH DATE,
   DIACHI VARCHAR2(50),
    SODT NUMBER(12),
   LUONG NUMBER(10),
   PHUCAP NUMBER(10),
   VAITRO VARCHAR2(12),
   MANQL VARCHAR2(10),
    PHG VARCHAR2(12)
);
--tao bang PHONGBAN
CREATE TABLE PHONGBAN
(
    MAPB VARCHAR2(10),
    TENPB VARCHAR2(15),
    TRPHG VARCHAR(15)
);
--tao bang DEAN
CREATE TABLE DEAN
(
    MADA VARCHAR2(10),
    TENDA VARCHAR2(15),
    NGAYDB DATE,
    PHONG VARCHAR2(10)
);
--tao bang PHANCONG
CREATE TABLE PHANCONG
(
    MANV VARCHAR2(10),
    MADA VARCHAR2(15),
    THOIGIAN DATE
);
--tao ham proc kiem tra user co ton tai, neu co drop user
DECLARE
    exist_user_check INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO exist_user_check
     FROM DBA_USERS
    where USERNAME = 'BETH'; --- Kiem tra co TABLE nao trung ten nay khong
    IF exist_user_check> 0 THEN --- Neu bien count khac khong tuc la co ton tai
        EXECUTE IMMEDIATE 'DROP USER Beth'; --- Thuc hien lenh DROP user
        dbms_output.put_line( 'User droppped' );
    END IF;
END;
/

--tao user 
CREATE USER Beth IDENTIFIED BY BETH
/
--them du lieu vao bang
insert into NHANVIEN (MANV, TENNV, PHAI, NGAYSINH, DIACHI, SODT, LUONG, PHUCAP, VAITRO, MANQL, PHG) 
values (1,'Le Duy Tan' , 'Nam',TO_DATE('23-04-2002', 'DD-MM-YYYY'),'038, Nguyen Van Cu', 0964717217, 5000000, 300000, 'SINH VIEN','537', '1' )
/
insert into NHANVIEN (MANV, TENNV, PHAI, NGAYSINH, DIACHI, SODT, LUONG, PHUCAP, VAITRO, MANQL, PHG)
values (2,'Phan Thanh Minh' , 'Nam',TO_DATE('23-04-2002', 'DD-MM-YYYY'),'038, Nguyen Van Cu', 0964717217, 5000000, 300000, 'SINH VIEN','537', '1' )
/
insert into NHANVIEN (MANV, TENNV, PHAI, NGAYSINH, DIACHI, SODT, LUONG, PHUCAP, VAITRO, MANQL, PHG)
values (3,'Kha Vinh Dat' , 'Nam',TO_DATE('23-04-2002', 'DD-MM-YYYY'),'038, Nguyen Van Cu', 0964717217, 5000000, 300000, 'SINH VIEN','537', '1' )
/
insert into NHANVIEN (MANV, TENNV, PHAI, NGAYSINH, DIACHI, SODT, LUONG, PHUCAP, VAITRO, MANQL, PHG)
values (4,'Nguyen Thanh Dat' , 'Nam',TO_DATE('23-04-2002', 'DD-MM-YYYY'),'038, Nguyen Van Cu', 0964717217, 5000000, 300000, 'SINH VIEN','537', '1' )
