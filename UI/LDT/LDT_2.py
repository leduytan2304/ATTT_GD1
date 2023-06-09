
#grant privilege for user
import tkinter as tk
import oracledb
from tkinter import *
from tkinter import messagebox



def login_user_privilege( username, password, privilege, object, role):   
    try:
        dsn = {
                "host": "localhost",
                "port": "1521",
                "sid": "xe",
                "user": username,
                "password": password
                }
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()
        print("Login success")
        
        sqlTxt = "GRANT  " + privilege + " ON "+ object + " TO " + role
        cursor.execute(sqlTxt)
        print("Login successssssssss")
        messagebox.showinfo("Notification", ("Grant " + privilege + " ON "+ object + " TO " + role  + " success") )
    except oracledb.DatabaseError as e:
        messagebox.showerror("ERROR ", "Error can not "+ "Grant " + privilege + " ON "+ object + " TO " + role + " WITH GRANT OPTION" )
#SELECT * FROM ROLE_TAB_PRIVS where TABLE_NAME ='NHANVIEN'      
def UI(username_login, password_login):   
    root = tk.Tk()
    root.title("Grant Role for role")
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

    username = tk.Label(root, text="ROLE")
    username.place(x=60, y = 120)
    username.config(font=("Arial", 12))
    username_entry = tk.Entry(root)
    username_entry.place(x=160, y = 125)

    # check = IntVar()
    # c = Checkbutton(root, text="With grant option", variable=check)
    # c.place(x=160, y = 145)


    privilege_data =privilege_entry.get()
    object_data= object_entry.get()
    user_data = username_entry.get()
    def print_data():
        if(privilege_entry.get() =="" or object_entry.get() =="" or username_entry.get() ==""):
            print("please input in all the textbox")
        else:
            privilege_data =privilege_entry.get()
            object_data= object_entry.get()
            user_data = username_entry.get()
            print(privilege_entry.get())
            print(object_entry.get())
            print(username_entry.get())
            print(username_login)
            
            login_user_privilege(username_login,password_login,privilege_entry.get(), object_entry.get(), username_entry.get()) 


    Execute_btn = tk.Button(root, text="Grant privileges", command=print_data)# button Drop User
    Execute_btn.place(x= 180, y = 200)
    root.mainloop()
#UI('system', 'tan123');

