import tkinter as tk
import oracledb


from tkinter import *

        
root = tk.Tk()
root.title("Oracle Login")
root.geometry("300x200")

def on_enter(event):
    Role.config(bg ='#343434', fg = '#ffffff', )  
    #print("hi")
def on_leave(event):
    #print("hi#")
    Role.config(bg ='#343434', fg = '#ffffff', ) 

def login():
    username = username_entry.get()
    password = password_entry.get()
    try:
            dsn = {
            "host": "localhost",
            "port": "1521",
            "sid": "xe",
            "user": username,
            "password": password,
            "mode": oracledb.SYSDBA }
            connection = oracledb.connect(**dsn)
            print("Login success")
            return True
    except oracledb.DatabaseError as e:
            print("Login fail")
            return False
def afterLoginUI(newRoot):
     pass
     

def afterLogin():
    root.destroy()
    newRoot = Tk()
    newRoot.title("Hệ thống quản lý bệnh viện")
    newRoot.geometry("400x400")
    my_menu = Menu(newRoot)
    newRoot.config(menu = my_menu)

    def our_command():
        pass

    role = Menu(my_menu)

    my_menu.add_cascade(label ="Role", menu = role)
    role.add_command(label ="Create",command = our_command)
    role.add_command(label ="Drop",command = our_command)
    role.add_command(label ="Grant",command = newRoot.quit)
    role.add_command(label ="Revoke",command = newRoot.quit)

    privileges = Menu(my_menu)

    my_menu.add_cascade(label ="Privilege", menu = privileges)
    privileges.add_command(label ="Grant User Object Privilege",command = our_command)
    privileges.add_command(label ="Grant Role Privilege",command = newRoot.quit)
    privileges.add_command(label ="Grant Role Privilege for user",command = newRoot.quit)
    privileges.add_command(label ="Grant Role Privilege for user",command = newRoot.quit)

    Check_privilege = Menu(my_menu)

    my_menu.add_cascade(label ="Check Privilege", menu = Check_privilege)
    Check_privilege.add_command(label ="Check privilege of User", command = our_command)
    Check_privilege.add_command(label ="Check privilege of Role",command = newRoot.quit)
    newRoot.mainloop()








username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
login_button = tk.Button(root, text="Login", command=afterLogin)
login_button.pack()

    



        
  





root.mainloop()

    
