
#grant privilege for user
import tkinter as tk
import oracledb
from tkinter import *
from tkinter import messagebox



def grant_user_privilege(root, username, password, privilege, object, user,checkOption):   
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
        if(checkOption == 0):
                    sqlTxt = "GRANT " + privilege + " ON "+ object + " TO " + user
                    cursor.execute(sqlTxt)
                    messagebox.showinfo("Notification", ("Grant " + privilege + " ON "+ object + " TO " + user  + " success") )
        else:
                    sqlTxt = "GRANT " + privilege + " ON "+ object + " TO " + user + " WITH GRANT OPTION"
                    cursor.execute(sqlTxt)
                    messagebox.showinfo("Notification", ("Grant " + privilege + " ON "+ object + " TO " + user  + " WITH GRANT OPTION" + " success") )
    except oracledb.DatabaseError as e:
            if(checkOption == 0):
                messagebox.showerror("ERROR ", "Error can not "+ "Grant " + privilege + " ON "+ object + " TO " + user)
            else:
                  
                messagebox.showerror("ERROR ", "Error can not "+ "Grant " + privilege + " ON "+ object + " TO " + user + " WITH GRANT OPTION" )
def UI(username, password):  
    root = tk.Tk()
    root.title("Grant privileges for user")
    root.geometry("400x320")      
    privilege = tk.Label(root, text="Privilege")
    privilege.place(x=60, y = 40)
    privilege.config(font=("Arial", 12))
    privilege_entry = tk.Entry(root)
    privilege_entry.place(x=160, y = 45)


    object = tk.Label(root, text="Object")
    object.place(x=60, y = 80)
    object.config(font=("Arial", 12))
    object_entry = tk.Entry(root)
    object_entry.place(x=160, y = 85)



    username = tk.Label(root, text="Username")
    username.place(x=60, y = 120)
    username.config(font=("Arial", 12))
    username_entry = tk.Entry(root)
    username_entry.place(x=160, y = 125)

    check = IntVar()
    c = Checkbutton(root, text="With grant option", variable=check)
    c.place(x=160, y = 145)


    privilege_data =privilege_entry.get()
    object_data= object_entry.get()
    user_data = username_entry.get()
    def print_data():
        if(privilege_entry.get() =="" or object_entry.get() =="" or username_entry.get() ==""):
            print("please input in all the textbox")
        else:
            print(privilege_entry.get())
            print(object_entry.get())
            print(username_entry.get())
            print(check.get())
            grant_user_privilege(root,'sys','tan123',privilege_entry.get(), object_entry.get(), username_entry.get(),check.get()) 

    Execute_btn = tk.Button(root, text="Grant user privilege", command=print_data)# button Drop User
    Execute_btn.place(x= 180, y = 200)
    root.mainloop()
# UI('sys', 'tan123');

