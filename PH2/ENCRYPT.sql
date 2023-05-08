create or replace function decrypt_NhanVien (p_data in nvarchar2)  
    return varchar2  
as
	input_string VARCHAR2(200);
    output_string NVARCHAR2 (200);
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
	output_string := TO_NCHAR(input_string);
    return output_string; 
end; 
