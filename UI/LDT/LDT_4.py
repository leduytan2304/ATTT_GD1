
#grant privilege for user
import tkinter as tk
import oracledb
from tkinter import *
from tkinter import messagebox
import random



def Grant_role_for_user( username, password, role, column,table, user):   
    try:
        dsn = {
                "host": "localhost",
                "port": "1521",
                "sid": "xe",
                "user": username,
                "password": password}
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()
        print("Login success")
        
        #cursor.execute("alter session set \"_ORACLE_SCRIPT\"=true;")
        cursor.execute("select * from NHANVIEN")
        rows = cursor.fetchall()

        for row in rows:
            print(row)
        if(role == "Insert" or role == "INSERT" or role == "insert" or role == "delete" or role == "Delete" or role == "DELETE"):
            messagebox.showerror("ERROR ", "Error can not "+ "Grant " + role +" on columns " + column + " ON "+ table +  " TO " + user)
        if(role == "update" or role == "Update" or role == "UPDATE"):    
            sqlTxt = "Grant " + role + "("+ column+ ")" + " ON "+ table + " TO " + user 
            #GRANT UPDATE (TENNV) ON employees TO temp;
            cursor.execute(sqlTxt)
            messagebox.showinfo("Notification", ("Grant " + role + "("+ column+ ")" + " ON "+ table + " TO " + user  + " success") )
        else:
           
            ramdon_number = random.randint(1, 10000) 
            sqlTxt1 ="CREATE VIEW " +  "view_name"+ str(ramdon_number)+ " AS SELECT "+ column +" FROM NHANVIEN"
            #sqlTxt1 = "CREATE VIEW view_nameTENNVNHANVIEN AS SELECT TENNV FROM NHANVIEN"
            print("first: " + sqlTxt1 ) 
            cursor.execute(sqlTxt1)               
            sqlTxt2 ="GRANT SELECT ON "+  "view_name" + str(ramdon_number) + " TO " + user;      
            print("second: " + sqlTxt2 ) 
            cursor.execute(sqlTxt2)
            messagebox.showinfo("Notification", ("Grant " + role + "("+ column+ ")" + " ON "+ table + " TO " + user  + " success") )
    except oracledb.DatabaseError as e:                  
                messagebox.showerror("ERROR ", "Error can not "+ "GRANT " + role + "(" + column +")" + " ON "+ table + " TO " + user)
def UI(username_login, password_login):  
    root = tk.Tk()
    root.title("Grant privileges on column for user")
    root.geometry("400x320")       
    privileges = tk.Label(root, text="Privileges")
    privileges.place(x=60, y = 40)
    privileges.config(font=("Arial", 12))
    privileges_entry = tk.Entry(root)
    privileges_entry.place(x=160, y = 45)


    column = tk.Label(root, text="Columns")
    column.place(x=60, y = 80)
    column.config(font=("Arial", 12))
    column_entry = tk.Entry(root)
    column_entry.place(x=160, y = 90)

    table = tk.Label(root, text="Object")
    table.place(x=60, y = 120)
    table.config(font=("Arial", 12))
    table_entry = tk.Entry(root)
    table_entry.place(x=160, y = 125)
   

    username = tk.Label(root, text="User")
    username.place(x=60, y = 160)
    username.config(font=("Arial", 12))
    username_entry = tk.Entry(root)
    username_entry.place(x=160, y = 170)

    privilege_data =privileges_entry.get()

    user_data = username_entry.get()
    def print_data():
        if(privileges_entry.get() ==""  or username_entry.get() ==""):
            print("please input in all the textbox")
        else:
            print(privileges_entry.get())
            print(column_entry.get())
            print(table_entry.get())
            print(username_entry.get())
            Grant_role_for_user(username_login,password_login,privileges_entry.get(),column_entry.get(), table_entry.get(),  username_entry.get()) 


    Execute_btn = tk.Button(root, text="Grant role on columns", command=print_data)# button Drop User
    Execute_btn.place(x= 180, y = 200)
    #SELECT GRANTEE,GRANTED_ROLE FROM DBA_ROLE_PRIVS WHERE GRANTED_ROLE = 'DATAENTRY'
    root.mainloop()
UI('system', 'tan123');
