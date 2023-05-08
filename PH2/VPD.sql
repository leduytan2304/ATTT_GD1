--- CS#1 ---
CREATE OR REPLACE FUNCTION policy_NhanVien (p_schema IN VARCHAR2, p_object IN VARCHAR2)
RETURN VARCHAR2 IS
  v_condition VARCHAR2(4000);
BEGIN
    if (user = 'SYS' or user = 'SYSTEM') then
        RETURN NULL;
    else 
        v_condition := 'MANV = (SELECT MANV FROM USERNAME WHERE UPPER(user_name) = user)';
        RETURN v_condition;
    end if;
END;

BEGIN
  DBMS_RLS.ADD_POLICY (
    object_schema   => 'system',
    object_name     => 'view_NV_NhanVien',
    policy_name     => 'policy_NhanVien',
    function_schema => 'system',
    policy_function => 'policy_NhanVien',
    statement_types => 'SELECT,UPDATE',
    update_check    => TRUE
  );
END;

BEGIN
  DBMS_RLS.ADD_POLICY (
    object_schema   => 'system',
    object_name     => 'view_NV_PhanCong',
    policy_name     => 'policy_NhanVien',
    function_schema => 'system',
    policy_function => 'policy_NhanVien',
    statement_types => 'SELECT',
    update_check    => TRUE
  );
END;


CREATE OR REPLACE FUNCTION policy_QuanLy (p_schema IN VARCHAR2, p_object IN VARCHAR2)
RETURN VARCHAR2 IS
  v_condition VARCHAR2(4000);
BEGIN
    if (user = 'SYS' or user = 'SYSTEM') then
        RETURN NULL;
    else 
        v_condition := 'MANQL = (SELECT MANV FROM USERNAME WHERE UPPER(user_name) = user)';
        RETURN v_condition;
    end if;
END;

BEGIN
  DBMS_RLS.ADD_POLICY (
    object_schema   => 'system',
    object_name     => 'view_QuanLy',
    policy_name     => 'policy_QuanLy',
    function_schema => 'system',
    policy_function => 'policy_QuanLy',
    statement_types => 'SELECT',
    update_check    => TRUE
  );
END;

--- CS#2 ---
CREATE OR REPLACE FUNCTION policy_QuanLy (p_schema IN VARCHAR2, p_object IN VARCHAR2)
RETURN VARCHAR2 IS
  v_condition VARCHAR2(4000);
BEGIN
    if (user = 'SYS' or user = 'SYSTEM') then
        RETURN NULL;
    else 
        v_condition := 'MANQL = (SELECT MANV FROM USERNAME WHERE UPPER(user_name) = user)';
        RETURN v_condition;
    end if;
END;

BEGIN
  DBMS_RLS.ADD_POLICY (
    object_schema   => 'system',
    object_name     => 'view_QuanLy',
    policy_name     => 'policy_QuanLy',
    function_schema => 'system',
    policy_function => 'policy_QuanLy',
    statement_types => 'SELECT',
    update_check    => TRUE
  );
END;

--- CS#3 ---
create or replace function Select_View_TruongPhong_NV(p_schema IN VARCHAR2, p_object IN VARCHAR2)
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
            return 'MANV != '''||login_user||'''';
        end if;
    end;
end;

--tao policy xem thong tin nhan vien thuoc phong ban cua truong phong
BEGIN
  DBMS_RLS.ADD_POLICY(
    object_schema   => 'system',
    object_name     => 'View_TruongPhong_Select_NhanVien_Info',
    policy_name     => 'VPD_View_TruongPhong_Select_NhanVien_Info',
    function_schema => 'system',
    policy_function => 'Select_View_TruongPhong_NV',
    statement_types => 'SELECT',
    update_check    => FALSE,
    enable          => TRUE
  );
END;

--tao vpd cho view phan cong
BEGIN
  DBMS_RLS.ADD_POLICY (
    object_schema   => 'system',
    object_name     => 'view_NV_PhanCong',
    policy_name     => 'PHANCONG_Select_Info',
    function_schema => 'system',
    policy_function => 'policy_NhanVien',
    statement_types => 'SELECT',
    update_check    => TRUE
  );
END;



--- CS#4 ---
CREATE OR REPLACE FUNCTION policy_Select_Update_NhanVien 
(p_schema IN VARCHAR2, 
p_object IN VARCHAR2)
RETURN VARCHAR2 
AS
BEGIN
    IF USER = 'nv17' THEN
        RETURN '1=0';
    ELSE
        RETURN NULL;
    END IF;
END;
/
--tao policy cho Theota
BEGIN
  DBMS_RLS.ADD_POLICY (
    object_schema   => 'system',
    object_name     => 'NHANVIEN',
    policy_name     => 'policy_Select_Update_NhanVien',
    function_schema => 'system',
    policy_function => 'policy_Select_Update_NhanVien',
    statement_types => 'SELECT, UPDATE',
    update_check    => TRUE,
    enable          => TRUE
  );
END;
/