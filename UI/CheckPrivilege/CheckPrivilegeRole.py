from tkinter import *
from tkinter import ttk
import oracledb
from tkinter import messagebox
from functools import partial

global cursor

# Hàm hiển thị cửa sổ xem quyền của Role
def checkPriRole_window(username, password):
    try:
        dsn = {
            "host": "localhost",
            "port": "1521",
            "sid": "xe",
            "user": username,
            "password": password}
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()

        checkPriRoleWindow = Tk()
        checkPriRoleWindow.title("Check privilege of Role")
        checkPriRoleWindow.geometry("300x150")

        # Nút bấm xem quyền trên bảng
        pressCheck_Pri_Role_Ob = Button(checkPriRoleWindow,
            text = "Check object privilege",
            width = 20,
            command = partial(checkPriRole_Ob, cursor))
        pressCheck_Pri_Role_Ob.pack()

        # Nút bấm xem quyền hệ thống
        pressCheck_Pri_Role_Sys = Button(checkPriRoleWindow,
            text = "Check system privilege",
            width = 20,
            command = partial(checkPriRole_Sys, cursor))
        pressCheck_Pri_Role_Sys.pack()
    except:
        pass

# Hàm kiểm tra quyền trên bảng của Role
def checkPriRole_Ob(cursor):
    ob_pri_role_Window = Tk()
    ob_pri_role_Window.title("Object Privilege Role")
    ob_pri_role_Window.geometry("530x400")

    # Hàm khi nhấn nút tìm kiếm quyền trên bảng của Role
    def searchRole_Ob():
        flag = True
        val_name = inputRole.get().upper()
        cursor.execute("SELECT ROLE FROM DBA_ROLES WHERE ROLE = '{}'".format(val_name))
        result = cursor.fetchall()
        count = cursor.rowcount
        if count < 1:
            flag = False
            messagebox.showinfo("ERROR!!!!", "Invalid Role")
        if flag == True:
            for i in tree_Role_Ob.get_children():
                tree_Role_Ob.delete(i)
            cursor.execute("SELECT ROLE,OWNER,TABLE_NAME,COLUMN_NAME,PRIVILEGE FROM ROLE_TAB_PRIVS WHERE ROLE = '{}'".format(val_name))
            rows_ob_role_pri = cursor.fetchall()
            for row in rows_ob_role_pri:
                tree_Role_Ob.insert(parent='', index='end', values=row)

    # khung nhập tên role
    inputRole = Entry(
        ob_pri_role_Window,
        width = 60)
    inputRole.insert(END, "Input role")
    inputRole.grid(row=1, column=0)

    # nút bấm tìm kiếm
    press_Search = Button(ob_pri_role_Window,
        text = "Search",
        width = 10,
        command = searchRole_Ob).grid(row=1, column=2)
    
    # bảng hiển thị quyền
    table_Search = Frame(ob_pri_role_Window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=2, columnspan=3, padx=10)

    tree_scroll_Role_Ob = Scrollbar(table_Search)
    tree_scroll_Role_Ob.pack(side=RIGHT, fill=Y)

    tree_Role_Ob = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Role_Ob.set)
    tree_Role_Ob.pack()

    tree_scroll_Role_Ob.config(command=tree_Role_Ob.yview)
    tree_Role_Ob['columns'] = ("1","2","3","4","5")
    tree_Role_Ob['show'] = 'headings'
    tree_Role_Ob.column("1", anchor=CENTER, width=90,minwidth=25)
    tree_Role_Ob.column("2", anchor=CENTER, width=90)
    tree_Role_Ob.column("3", anchor=CENTER, width=90)
    tree_Role_Ob.column("4", anchor=CENTER, width=90)
    tree_Role_Ob.column("5", anchor=CENTER, width=90)

    tree_Role_Ob.heading("1", text="ROLE", anchor=CENTER)
    tree_Role_Ob.heading("2",text = "OWNER", anchor=CENTER)
    tree_Role_Ob.heading("3", text = "TABLE_NAME", anchor=CENTER)
    tree_Role_Ob.heading("4", text = "COLUMN_NAME", anchor=CENTER)
    tree_Role_Ob.heading("5", text = "PRIVILEGE", anchor=CENTER)

# Hàm kiểm tra quyền hệ thống của Role
def checkPriRole_Sys(cursor):
    sys_pri_role_Window = Tk()
    sys_pri_role_Window.title("System Privilege Role")
    sys_pri_role_Window.geometry("530x400")

        # Hàm khi nhấn nút tìm kiếm quyền hệ thống của User
    def searchRole_Sys():
        flag = True
        val_name = inputRole.get().upper()
        cursor.execute("SELECT ROLE FROM DBA_ROLES WHERE ROLE = '{}'".format(val_name))
        result = cursor.fetchall()
        count = cursor.rowcount
        if count < 1:
            flag = False
            messagebox.showinfo("ERROR!!!!", "Invalid Role")
        if flag == True:
            for i in tree_Role_sys.get_children():
                tree_Role_sys.delete(i)
            cursor.execute("SELECT * FROM ROLE_SYS_PRIVS WHERE ROLE = '{}'".format(val_name))
            rows_sys_role_pri = cursor.fetchall()
            for row in rows_sys_role_pri:
                tree_Role_sys.insert(parent='', index='end', values=row)
    
    # khung nhập tên role
    inputRole = Entry(
        sys_pri_role_Window,
        width = 60)
    inputRole.insert(END, "Input role")
    inputRole.grid(row=1, column=0)

    # nút bấm tìm kiếm
    press_Search = Button(sys_pri_role_Window,
        text = "Search",
        width = 10,
        command = searchRole_Sys).grid(row=1, column=2)
    
    # bảng hiển thị quyền
    table_Search = Frame(sys_pri_role_Window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=2, columnspan=3, padx=10)

    tree_scroll_Role_sys = Scrollbar(table_Search)
    tree_scroll_Role_sys.pack(side=RIGHT, fill=Y)

    tree_Role_sys = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Role_sys.set)
    tree_Role_sys.pack()

    tree_scroll_Role_sys.config(command=tree_Role_sys.yview)
    tree_Role_sys['columns'] = ("1","2","3","4","5")
    tree_Role_sys['show'] = 'headings'
    tree_Role_sys.column("1", anchor=CENTER, width=90,minwidth=25)
    tree_Role_sys.column("2", anchor=CENTER, width=90)
    tree_Role_sys.column("3", anchor=CENTER, width=90)
    tree_Role_sys.column("4", anchor=CENTER, width=90)
    tree_Role_sys.column("5", anchor=CENTER, width=90)

    tree_Role_sys.heading("1", text="GRANTEE", anchor=CENTER)
    tree_Role_sys.heading("2",text = "PRIVILEGE", anchor=CENTER)
    tree_Role_sys.heading("3", text = "ADMIN_OPTION", anchor=CENTER)
    tree_Role_sys.heading("4", text = "COMMON", anchor=CENTER)
    tree_Role_sys.heading("5", text = "INHERITED", anchor=CENTER)