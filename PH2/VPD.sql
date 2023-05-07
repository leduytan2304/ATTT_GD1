
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
    object_name     => 'view_NhanVien',
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
    object_name     => 'view_NVPhanCong',
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