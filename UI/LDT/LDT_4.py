
#grant privilege for user
import tkinter as tk
import oracledb
from tkinter import *
from tkinter import messagebox



def Grant_role_for_user(root, username, password, role, column,table, user):   
    try:
        dsn = {
                "host": "localhost",
                "port": "1521",
                "sid": "xe",
                "user": username,
                "password": password,
                "mode": oracledb.SYSDBA }
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()
        print("Login success")
        
        #cursor.execute("alter session set \"_ORACLE_SCRIPT\"=true;")
        cursor.execute("select * from NHANVIEN")
        rows = cursor.fetchall()

        for row in rows:
            print(row)
        if(role == "insert" or role == "Insert" or role == "INSERT" or role == "delete" or role == "Delete" or role == "DELETE"):
            messagebox.showerror("ERROR ", "Error can not "+ "Grant " + role +" on columns " + column + " ON "+ table +  " TO " + user)
        else:    
            sqlTxt = "Grant " + role + "("+ column+ ")" + " ON "+ table + " TO " + user 
            #GRANT UPDATE (TENNV) ON employees TO temp;
            cursor.execute(sqlTxt)
            messagebox.showinfo("Notification", ("Grant " + role + "("+ column+ ")" + " ON "+ table + " TO " + user  + " sucess") )

                    
    except oracledb.DatabaseError as e:                  
                messagebox.showerror("ERROR ", "Error can not "+ "GRANT " + role + "(" + column +")" + " ON "+ table + " TO " + user)
def UI(username, password):  
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
           
            Grant_role_for_user(root,'sys','tan123',privileges_entry.get(),column_entry.get(), table_entry.get(),  username_entry.get()) 


    Execute_btn = tk.Button(root, text="Grant role on columns", command=print_data)# button Drop User
    Execute_btn.place(x= 180, y = 200)
    #SELECT GRANTEE,GRANTED_ROLE FROM DBA_ROLE_PRIVS WHERE GRANTED_ROLE = 'DATAENTRY'
    root.mainloop()
#UI('sys', 'tan123');
