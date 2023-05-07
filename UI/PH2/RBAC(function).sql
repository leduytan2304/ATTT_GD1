--CS#3
--them function insert PHANCONG
DROP PROCEDURE INSERT_PHANCONG;
CREATE OR REPLACE PROCEDURE INSERT_PHANCONG
(
    MANV_IN VARCHAR2,
    MADA_IN VARCHAR2,
    THOIGIAN_IN date
)
AS
    vaitro_nv varchar2(255);
    login_user varchar2(255);
    check_nhanvien NUMBER;
    check_dean NUMBER;
    manv_check varchar2(255);
BEGIN
    login_user := SYS_CONTEXT('userenv', 'SESSION_USER');
    SELECT NV.VAITRO INTO vaitro_nv 
    FROM USERNAME USN, NHANVIEN NV
    WHERE USN.user_name = login_user and USN.MANV = NV.MANV;
    
    SELECT USN.MANV INTO manv_check 
    FROM USERNAME USN
    WHERE USN.user_name = login_user;
    if (vaitro_nv <> 'Truong phong') then
          return;
    elsif (MANV_IN = manv_check ) then
        return;
    else
        SELECT COUNT(*) INTO check_nhanvien
        FROM USERNAME USN, NHANVIEN NV, PHONGBAN PB
        WHERE USN.user_name = login_user
        AND USN.MANV = PB.TRPHG
        AND PB.MAPB = NV.PHG
        AND NV.MANV = MANV_IN;
        
        SELECT COUNT(*) INTO check_dean
        FROM DEAN DA
        WHERE DA.MADA = MADA_IN;

        if (check_nhanvien = 0) then
            return;
        elsif (check_dean = 0) then
            return;
        else
            INSERT INTO PHANCONG(MANV, MADA, THOIGIAN)
            VALUES(MANV_IN, MADA_IN, THOIGIAN_IN);
            COMMIT;
        end if;
    end if;
END;


--tao functuon delete phancong
drop procedure DELETE_PHANCONG;
CREATE OR REPLACE PROCEDURE DELETE_PHANCONG
(
    MANV_IN VARCHAR2,
    MADA_IN VARCHAR2
)
AS
    vaitro_nv varchar2(255);
    login_user varchar2(255);
    check_nhanvien NUMBER;
    check_dean_1 NUMBER;
    check_dean_2 NUMBER;
    manv_check varchar2(255);
BEGIN
    login_user := SYS_CONTEXT('userenv', 'SESSION_USER');
    SELECT NV.VAITRO INTO vaitro_nv 
    FROM USERNAME USN, NHANVIEN NV
    WHERE USN.user_name = login_user and USN.MANV = NV.MANV;
    
    SELECT USN.MANV INTO manv_check 
    FROM USERNAME USN
    WHERE USN.user_name = login_user;
    if (vaitro_nv <> 'Truong phong') then
          return;
    elsif (MANV_IN = manv_check ) then
        return;
    else
        SELECT COUNT(*) INTO check_nhanvien
        FROM USERNAME USN, NHANVIEN NV, PHONGBAN PB
        WHERE USN.user_name = login_user
        AND USN.MANV = PB.TRPHG
        AND PB.MAPB = NV.PHG
        AND NV.MANV = MANV_IN;
        
        SELECT COUNT(*) INTO check_dean_1
        FROM DEAN DA
        WHERE DA.MADA = MADA_IN;
        
        SELECT COUNT(*) INTO check_dean_2
        FROM PHANCONG PC
        WHERE PC.MANV = MANV_IN AND PC.MADA = MADA_IN;

        if (check_nhanvien = 0) then
            return;
        elsif (check_dean_1 = 0) then
            return;
        elsif (check_dean_2 = 0) then
            return;
        else
            DELETE PHANCONG WHERE MANV = MANV_IN AND MADA = MADA_IN;
            COMMIT;
        end if;
    end if;
END;

--tao functuon update phancong
drop procedure UPDATE_PHANCONG;
CREATE OR REPLACE PROCEDURE UPDATE_PHANCONG
(
    MANV_IN VARCHAR2,
    MADA_IN VARCHAR2, 
    THOIGIAN_IN DATE
)
AS
    vaitro_nv varchar2(255);
    login_user varchar2(255);
    check_nhanvien NUMBER;
    check_dean_1 NUMBER;
    check_dean_2 NUMBER;
    manv_check varchar2(255);
BEGIN
    login_user := SYS_CONTEXT('userenv', 'SESSION_USER');
    SELECT NV.VAITRO INTO vaitro_nv 
    FROM USERNAME USN, NHANVIEN NV
    WHERE USN.user_name = login_user and USN.MANV = NV.MANV;
    
    SELECT USN.MANV INTO manv_check 
    FROM USERNAME USN
    WHERE USN.user_name = login_user;
    if (vaitro_nv <> 'Truong phong') then
          return;
    elsif (MANV_IN = manv_check ) then
        return;
    else
        SELECT COUNT(*) INTO check_nhanvien
        FROM USERNAME USN, NHANVIEN NV, PHONGBAN PB
        WHERE USN.user_name = login_user
        AND USN.MANV = PB.TRPHG
        AND PB.MAPB = NV.PHG
        AND NV.MANV = MANV_IN;
        
        SELECT COUNT(*) INTO check_dean_1
        FROM DEAN DA
        WHERE DA.MADA = MADA_IN;
        
        SELECT COUNT(*) INTO check_dean_2
        FROM PHANCONG PC
        WHERE PC.MANV = MANV_IN AND PC.MADA = MADA_IN;

        if (check_nhanvien = 0) then
            return;
        elsif (check_dean_1 = 0) then
            return;
        elsif (check_dean_2 = 0) then 
            return;
        else
            update PHANCONG set THOIGIAN = THOIGIAN_IN where MANV = MANV_IN and MADA = MADA_IN;
            COMMIT;
        end if;
    end if;
END;


--grant quyen chay function cho truong phong
GRANT EXECUTE ON INSERT_PHANCONG TO truongphong;
GRANT EXECUTE ON DELETE_PHANCONG TO truongphong;
GRANT EXECUTE ON UPDATE_PHANCONG TO truongphong;