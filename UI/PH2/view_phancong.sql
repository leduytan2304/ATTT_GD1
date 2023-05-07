--xem thong tin phan cong cua minh
drop view View_Select_PhanCong_Info;
CREATE OR REPLACE VIEW View_Select_PhanCong_Info AS
SELECT PC.*
FROM PHANCONG PC

--grant quyen xem view phan cong cho cac role
grant select on View_Select_PhanCong_Info to nhanvien;
grant select on View_Select_PhanCong_Info to qltructiep;
grant select on View_Select_PhanCong_Info to truongphong;
grant select on View_Select_PhanCong_Info to taichinh;
grant select on View_Select_PhanCong_Info to nhansu;
grant select on View_Select_PhanCong_Info to truongdean;

--tao vpd cho view phan cong
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

--drop policy
begin
    DBMS_RLS.DROP_POLICY (
        object_schema   => 'system',
        object_name     => 'PHANCONG',
        policy_name     => 'PHANCONG_Select_Info');
end;
