--Xem quyen cua user
drop view check_privilege_user;
CREATE OR REPLACE VIEW check_privilege_user as
select A.*
from (select grantee username,
             granted_role privilege,
             '--' owner,
             '--' table_name,
             '--' column_name,
             admin_option admin_option,
             'ROLE' access_type
      from dba_role_privs RP
      join dba_roles R on RP.granted_role = R.role
      where grantee in (select username from dba_users)
      union
      select grantee username,
             privilege privilege,
             '--' owner,
             '--' table_name,
             '--' column_name,
             admin_option admin_option,
             'SYSTEM' access_type
      from dba_sys_privs
      where grantee in (select username from dba_users)
      union
      select grantee username,
             privilege privilege,
             owner owner,
             table_name table_name,
             '--' colum_name,
             grantable admin_option,
             'TABLE' access_type
      from dba_tab_privs
      where grantee in (select username from dba_users)
      union
      select DP.grantee username,
             privilege privilege,
             owner owner,
             table_name table_name,
             column_name column_name,
             '--' admin_option,
             'ROLE' access_type
      from role_tab_privs RP, dba_role_privs DP
      where RP.role = DP.granted_role and DP.grantee in (select username from dba_users)
      union
      select grantee username,
             privilege privilege,
             grantable admin_option,
             owner owner,
             table_name table_name,
             column_name column_name,
             'COLUMN' access_type
      from dba_col_privs
      where grantee in (select username from dba_users)) A
order by username, A.table_name, case
                                    when A.access_type = 'SYSTEM' then 1
                                    when A.access_type = 'TABLE' then 2
                                    when A.access_type = 'COLUMN' then 3
                                    when A.access_type = 'ROLE' then 4
                                 end,
                                 case
                                    when A.privilege in ('EXECUTE') then 1
                                    when A.privilege in ('SELECT', 'INSERT', 'DELETE') then 3
                                    else 2
                                 end,
                                 A.column_name, A.privilege;
                        
grant select on check_privilege_user to system;


--xem quyen cua role
CREATE OR REPLACE VIEW check_privilege_role as                                
select A.*
from (select grantee role,
             granted_role privilege,
             '--' owner,
             '--' table_name,
             '--' column_name,
             admin_option admin_option,
             'ROLE' access_type
        from dba_role_privs RP
        join dba_roles R on RP.granted_role = R.role
        where grantee in (select role from dba_roles)
        union
        select grantee role,
                privilege privilege,
                '--' owner,
                '--' table_name,
                '--' column_name,
                admin_option admin_option,
                'SYSTEM' access_type
        from dba_sys_privs
        where grantee in (select role from dba_roles)
        union
        select grantee role,
                privilege privilege,
                owner owner,
                table_name table_name,
                '--' column_name,
                grantable admin_option,
                'TABLE' access_type
        from dba_tab_privs
        where grantee in (select role from dba_roles)
        union
        select DP.grantee role,
                privilege privilege,
                owner owner,
                table_name table_name,
                column_name column_name,
                '--' admin_option,
                'ROLE' access_type
        from role_tab_privs RP, dba_role_privs DP
        where RP.role = DP.granted_role and DP.grantee in (select role from dba_roles)
        union 
        select grantee role,
                privilege privilege,
                grantable admin_option,
                owner owner,
                table_name table_name,
                column_name column_name,
                'COLUMN' access_type
        from dba_col_privs
        where grantee in (select role from dba_roles)) A
order by role, A.table_name, case
                                when A.access_type = 'SYSTEM' then 1
                                when A.access_type = 'TABLE' then 2
                                when A.access_type = 'COLUMN' then 3
                                when A.access_type = 'ROLE' then 4
                            end,
                            case
                                when A.privilege in ('EXECUTE') then 1
                                when A.privilege in ('SELECT','INSERT','DELETE') then 3
                                else 2
                            end,
                            A.column_name, A.privilege;
            
grant select on check_privilege_role to system;