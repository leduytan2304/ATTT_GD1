from tkinter import *
from tkinter import ttk
import oracledb
from tkinter import messagebox
from functools import partial

global cursor

def checkPriUser_window(username, password):
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
        checkPriUserWindow = Tk()
        checkPriUserWindow.title("Check privilege of User")
        checkPriUserWindow.geometry("300x150")

        # Nút bấm xem quyền trên bảng
        pressCheck_Pri_User_Ob = Button(checkPriUserWindow,
            text = "Check object privilege",
            width = 20,
            command = partial(checkPriUser_Ob, cursor))
        pressCheck_Pri_User_Ob.pack()

        # Nút bấm xem quyền hệ thống
        pressCheck_Pri_User_Sys = Button(checkPriUserWindow,
            text = "Check system privilege",
            width = 20,
            command = partial(checkPriUser_Sys, cursor))
        pressCheck_Pri_User_Sys.pack()
    except:
        pass

# Hàm kiểm tra quyền trên bảng của User
def checkPriUser_Ob(cursor):
    ob_pri_user_Window = Tk()
    ob_pri_user_Window.title("Object Privilege Users")
    ob_pri_user_Window.geometry("530x400")

    # Hàm khi nhấn nút tìm kiếm quyền tren bảng của User
    def searchUser_Ob():
        flag = True
        val_name = inputUser.get().upper()
        cursor.execute("SELECT USERNAME FROM DBA_USERS WHERE USERNAME = '{}'".format(val_name))
        result = cursor.fetchall()
        count = cursor.rowcount
        if count < 1:
            flag = False
            messagebox.showinfo("ERROR!!!!", "Invalid Username")
        if flag == True:
            for i in tree_User_Ob.get_children():
                tree_User_Ob.delete(i)
            cursor.execute("SELECT GRANTEE,OWNER,TABLE_NAME,PRIVILEGE,TYPE FROM USER_TAB_PRIVS WHERE GRANTEE = '{}'".format(val_name))
            rows_ob_user_pri = cursor.fetchall()
            for row in rows_ob_user_pri:
                tree_User_Ob.insert(parent='', index='end', values=row)

    # khung nhập tên user
    inputUser = Entry(
        ob_pri_user_Window,
        width = 60)
    inputUser.insert(END, "Input username")
    inputUser.grid(row=1, column=0)

    # nút bấm tìm kiếm
    press_Search = Button(ob_pri_user_Window,
        text = "Search",
        width = 10,
        command = searchUser_Ob).grid(row=1, column=2)
    
    # bảng hiển thị quyền
    table_Search = Frame(ob_pri_user_Window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=2, columnspan=3, padx=10)

    tree_scroll_User_Ob = Scrollbar(table_Search)
    tree_scroll_User_Ob.pack(side=RIGHT, fill=Y)

    tree_User_Ob = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_User_Ob.set)
    tree_User_Ob.pack()

    tree_scroll_User_Ob.config(command=tree_User_Ob.yview)
    tree_User_Ob['columns'] = ("1","2","3","4","5")
    tree_User_Ob['show'] = 'headings'
    tree_User_Ob.column("1", anchor=CENTER, width=90,minwidth=25)
    tree_User_Ob.column("2", anchor=CENTER, width=90)
    tree_User_Ob.column("3", anchor=CENTER, width=90)
    tree_User_Ob.column("4", anchor=CENTER, width=90)
    tree_User_Ob.column("5", anchor=CENTER, width=90)

    tree_User_Ob.heading("1", text="GRANTEE", anchor=CENTER)
    tree_User_Ob.heading("2",text = "OWNER", anchor=CENTER)
    tree_User_Ob.heading("3", text = "TABLE_NAME", anchor=CENTER)
    tree_User_Ob.heading("4", text = "PRIVILEGE", anchor=CENTER)
    tree_User_Ob.heading("5", text = "TYPE", anchor=CENTER)

# Hàm kiểm tra quyền hệ thống của User
def checkPriUser_Sys(cursor):
    sys_pri_user_Window = Tk()
    sys_pri_user_Window.title("System Privilege User")
    sys_pri_user_Window.geometry("530x400")

        # Hàm khi nhấn nút tìm kiếm quyền hệ thống của User
    def searchUser_Sys():
        flag = True
        val_name = inputUser.get().upper()
        cursor.execute("SELECT USERNAME FROM DBA_USERS WHERE USERNAME = '{}'".format(val_name))
        result = cursor.fetchall()
        count = cursor.rowcount
        if count < 1:
            flag = False
            messagebox.showinfo("ERROR!!!!", "Invalid Username")
        if flag == True:
            for i in tree_User_sys.get_children():
                tree_User_sys.delete(i)
            cursor.execute("SELECT * FROM DBA_SYS_PRIVS WHERE GRANTEE = '{}'".format(val_name))
            rows_sys_user_pri = cursor.fetchall()
            for row in rows_sys_user_pri:
                tree_User_sys.insert(parent='', index='end', values=row)
    
    # khung nhập tên user
    inputUser = Entry(
        sys_pri_user_Window,
        width = 60)
    inputUser.insert(END, "Input username")
    inputUser.grid(row=1, column=0)

    # nút bấm tìm kiếm
    press_Search = Button(sys_pri_user_Window,
        text = "Search",
        width = 10,
        command = searchUser_Sys).grid(row=1, column=2)
    
    # bảng hiển thị quyền
    table_Search = Frame(sys_pri_user_Window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=2, columnspan=3, padx=10)

    tree_scroll_User_sys = Scrollbar(table_Search)
    tree_scroll_User_sys.pack(side=RIGHT, fill=Y)

    tree_User_sys = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_User_sys.set)
    tree_User_sys.pack()

    tree_scroll_User_sys.config(command=tree_User_sys.yview)
    tree_User_sys['columns'] = ("1","2","3","4","5")
    tree_User_sys['show'] = 'headings'
    tree_User_sys.column("1", anchor=CENTER, width=90,minwidth=25)
    tree_User_sys.column("2", anchor=CENTER, width=90)
    tree_User_sys.column("3", anchor=CENTER, width=90)
    tree_User_sys.column("4", anchor=CENTER, width=90)
    tree_User_sys.column("5", anchor=CENTER, width=90)

    tree_User_sys.heading("1", text="GRANTEE", anchor=CENTER)
    tree_User_sys.heading("2",text = "PRIVILEGE", anchor=CENTER)
    tree_User_sys.heading("3", text = "ADMIN_OPTION", anchor=CENTER)
    tree_User_sys.heading("4", text = "COMMON", anchor=CENTER)
    tree_User_sys.heading("5", text = "INHERITED", anchor=CENTER)