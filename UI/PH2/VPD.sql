--CS#3
--function xem nhan vien thuoc phong ban
drop function Select_View_TruongPhong_NV;
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

--drop policy
begin
  DBMS_RLS.DROP_POLICY(
    object_schema   => 'system',
    object_name     => 'View_TruongPhong_Select_NhanVien_Info',
    policy_name     => 'VPD_View_TruongPhong_Select_NhanVien_Info');
end;