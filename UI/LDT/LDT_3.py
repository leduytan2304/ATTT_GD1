
#grant privilege for user
import tkinter as tk
import oracledb
from tkinter import *
from tkinter import messagebox



def Grant_role_for_user(root, username, password, role, user):   
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
       
        sqlTxt = "GRANT  " + role + " TO " + user
        cursor.execute(sqlTxt)
        messagebox.showinfo("Notification", ("Grant " + role  + " TO " + user  + " success") )
       
                    
    except oracledb.DatabaseError as e:                  
                messagebox.showerror("ERROR ", "Error can not "+ "Grant " + role +" TO " + user)
def UI(username, password):  
    root = tk.Tk()
    root.title("Grant privileges for user")
    root.geometry("400x320")       
    role = tk.Label(root, text="Role")
    role.place(x=60, y = 40)
    role.config(font=("Arial", 12))
    role_entry = tk.Entry(root)
    role_entry.place(x=160, y = 45)

    username = tk.Label(root, text="User")
    username.place(x=60, y = 120)
    username.config(font=("Arial", 12))
    username_entry = tk.Entry(root)
    username_entry.place(x=160, y = 125)

    privilege_data =role_entry.get()

    user_data = username_entry.get()
    def print_data():
        if(role_entry.get() ==""  or username_entry.get() ==""):
            print("please input in all the textbox")
        else:
            print(role_entry.get())
            print(role_entry.get())
            print(username_entry.get())
            Grant_role_for_user(root,'sys','tan123',role_entry.get(),  username_entry.get()) 


    Execute_btn = tk.Button(root, text="Grant role", command=print_data)# button Drop User
    Execute_btn.place(x= 180, y = 200)
    #SELECT GRANTEE,GRANTED_ROLE FROM DBA_ROLE_PRIVS WHERE GRANTED_ROLE = 'DATAENTRY'
    root.mainloop()
#UI('sys', 'tan123');
