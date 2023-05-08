--xem thong tin phan cong cua minh
drop view view_NV_PhanCong;
CREATE OR REPLACE VIEW view_NV_PhanCong AS
SELECT PC.*
FROM PHANCONG PC

--grant quyen xem view phan cong cho cac role
grant select on view_NV_PhanCong to nhanvien;
grant select on view_NV_PhanCong to qltructiep;
grant select on view_NV_PhanCong to truongphong;
grant select on view_NV_PhanCong to taichinh;
grant select on view_NV_PhanCong to nhansu;
grant select on view_NV_PhanCong to truongdean;

--tao vpd cho view phan cong
BEGIN
  DBMS_RLS.ADD_POLICY (
    object_schema   => 'system',
    object_name     => 'view_NV_PhanCong',
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
        object_name     => 'view_NV_PhanCong',
        policy_name     => 'PHANCONG_Select_Info');

end;
