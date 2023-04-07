#drop role
import tkinter as tk
import oracledb
from tkinter import *
from tkinter import messagebox


def drop_role(root, username, password, role):   
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
       
        sqlTxt = "Drop role " + role 
        cursor.execute(sqlTxt)
        messagebox.showinfo("Notification", ("Drop role " + role  + " sucess"))
       
    except oracledb.DatabaseError as e:                  
                messagebox.showerror("Fail!", e)

def UI(username, password):  
    root = tk.Tk()
    root.title("Drop role")
    root.geometry("400x150")       

    role = tk.Label(root, text="Role")
    role.place(x=60, y = 40)
    role.config(font=("Arial", 12))
    role_entry = tk.Entry(root)
    role_entry.place(x=120, y = 42)

    def print_data():
        if(role_entry.get() ==""):
            print("Please input role name")
        else:
            print(role_entry.get())
            drop_role(root, username, password, role_entry.get()) 


    Execute_btn = tk.Button(root, text="Drop role", command=print_data) 
    Execute_btn.place(x= 150, y = 80)
    root.mainloop()


