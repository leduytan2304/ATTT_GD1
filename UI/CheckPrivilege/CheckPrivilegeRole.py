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

        check_Pri_Role(cursor)
    except:
        pass

# Hàm kiểm tra quyền trên bảng của Role
def check_Pri_Role(cursor):
    pri_role_Window = Tk()
    pri_role_Window.title("Object Privilege Role")
    pri_role_Window.geometry("720x400")

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
            for i in tree_Role_Pri.get_children():
                tree_Role_Pri.delete(i)
            cursor.execute("select * from sys.check_privilege_role where role = '{}'".format(val_name))
            rows_role_pri = cursor.fetchall()
            for row in rows_role_pri:
                tree_Role_Pri.insert(parent='', index='end', values=row)

    # khung nhập tên role
    inputRole = Entry(
        pri_role_Window,
        width = 60)
    inputRole.insert(END, "Input role")
    inputRole.grid(row=1, column=0)

    # nút bấm tìm kiếm
    press_Search = Button(pri_role_Window,
        text = "Search",
        width = 10,
        command = searchRole_Ob).grid(row=1, column=2)
    
    # bảng hiển thị quyền
    table_Search = Frame(pri_role_Window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=2, columnspan=3, padx=10)

    tree_scroll_Role = Scrollbar(table_Search)
    tree_scroll_Role.pack(side=RIGHT, fill=Y)

    tree_Role_Pri = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Role.set)
    tree_Role_Pri.pack()

    tree_scroll_Role.config(command=tree_Role_Pri.yview)
    tree_Role_Pri['columns'] = ("1","2","3","4","5","6","7")
    tree_Role_Pri['show'] = 'headings'
    tree_Role_Pri.column("1", anchor=CENTER, width=90,minwidth=25)
    tree_Role_Pri.column("2", anchor=CENTER, width=90)
    tree_Role_Pri.column("3", anchor=CENTER, width=90)
    tree_Role_Pri.column("4", anchor=CENTER, width=90)
    tree_Role_Pri.column("5", anchor=CENTER, width=90)
    tree_Role_Pri.column("6", anchor=CENTER, width=90)
    tree_Role_Pri.column("7", anchor=CENTER, width=90)

    tree_Role_Pri.heading("1", text="ROLE", anchor=CENTER)
    tree_Role_Pri.heading("2",text = "PRIVILEGE", anchor=CENTER)
    tree_Role_Pri.heading("3", text = "OWNER", anchor=CENTER)
    tree_Role_Pri.heading("4", text = "TABLE_NAME", anchor=CENTER)
    tree_Role_Pri.heading("5", text = "COLUMN_NAME", anchor=CENTER)
    tree_Role_Pri.heading("6", text = "ADMIN_OPTION", anchor=CENTER)
    tree_Role_Pri.heading("7", text = "ACCESS_TYPE", anchor=CENTER)