import tkinter as tk
import oracledb
import TreeView as tv
from tkinter import *
from tkinter import messagebox
import PTM.PTM_1 as crl
import PTM.PTM_2 as drl
from functools import partial

        
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
        cursor = connection.cursor()
        print("Login success")
        cursor.execute("select username, user_id, account_status, created from DBA_users")
        rows = cursor.fetchall()

        for row in rows:
            print(row)
        root.destroy()
        cursor.close()
        connection.close()
        afterLogin(username, password)
    except oracledb.DatabaseError as e:
        print("Login fail")
        return False
    

def afterLoginUI(newRoot):
    pass
     

def afterLogin(username, password):

    #sau khi dang nhap hien 1 cửa sổ mới
    newRoot = Tk()
    newRoot.title("Hệ thống quản lý bệnh viện")
    newRoot.geometry("800x520")
    my_menu = Menu(newRoot)
    newRoot.config(menu = my_menu)

    def our_command():
        pass

    role = Menu(my_menu)

    my_menu.add_cascade(label ="Role", menu = role)# tao menu Role
    role.add_command(label ="Create", command = partial(crl_ptm, username, password))
    role.add_command(label ="Drop", command = partial(drl_ptm, username, password))
    role.add_command(label ="Grant role to user", command = newRoot.quit)
   

    privileges = Menu(my_menu)

    my_menu.add_cascade(label ="Privilege", menu = privileges)# tao menu Privilege
    privileges.add_command(label ="Grant User Object Privilege", command = our_command)
    privileges.add_command(label ="Grant Role Privilege", command = newRoot.quit)
    privileges.add_command(label ="Grant Role Privilege for user", command = newRoot.quit)
    privileges.add_command(label ="Grant Role Privilege for user", command = newRoot.quit)

    Check_privilege = Menu(my_menu)

    my_menu.add_cascade(label ="Check Privilege", menu = Check_privilege)# tao menu Check Privilege
    Check_privilege.add_command(label ="Check privilege of User", command = our_command)
    Check_privilege.add_command(label ="Check privilege of Role", command = newRoot.quit)

    def createUser():
        cur = tv.active_login(username, password)
        print(username, password)

        createUser = tk.Tk()
        createUser.title("Create User")
        createUser.geometry("400x300")

        username_label = tk.Label(createUser, text="Username:")
        username_label.pack()
        password_label = tk.Label(createUser, text="Password:")
        password_label.pack()
        
        def create_User():
            new_username = username_entry.get()
            new_password = password_entry.get()
            create_txt = "CREATE USER " + new_username + " IDENTIFIED BY " + new_password
            grant_txt = "GRANT CREATE SESSION TO " + new_username
            print(create_txt)
            cur.execute(create_txt)
            cur.execute(grant_txt)

        
        username_entry = tk.Entry(createUser)
        username_entry.pack()
        password_entry = tk.Entry(createUser)
        password_entry.pack()
        submit_button = tk.Button(createUser, text="Create", command=create_User)
        submit_button.pack()

    def dropUser():
        cur = tv.active_login(username, password)
        user_drop = tv.TreeView(newRoot, username, password)

        print("User drop:" + user_drop)
        sqltxt = "DROP USER " + user_drop
        print(sqltxt)
        cur.execute(sqltxt)
        
        
        
        
    def userList():
        tv.TreeView(newRoot, username, password)

    def tableList():
        tv.tableList(newRoot,username, password)

    
    
    label = tk.Label(newRoot, text="List of user")
    label.config(font=("Arial", 18))
    label.place( x= 10, y = 40)

    btn1 = tk.Button(newRoot, text="Create User", command=createUser)
    btn1.place(x= 200, y = 40)

    btn2 = tk.Button(newRoot, text="Drop User", command=dropUser)
    btn2.place(x= 300, y = 40)

    btn3 = tk.Button(newRoot, text="User List", command=userList)
    btn3.place(x= 400, y = 40)

    btn4 = tk.Button(newRoot, text="Table List", command=tableList)
    btn4.place(x= 500, y = 40)

    
    tv.TreeView(newRoot, username, password) # module của TreeView


def crl_ptm(username, password):
    crl.UI(username, password)

def drl_ptm(username, password):
    drl.UI(username, password)



root = tk.Tk()
root.title("Oracle Login")
root.geometry("300x200")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()


root.mainloop()

    
