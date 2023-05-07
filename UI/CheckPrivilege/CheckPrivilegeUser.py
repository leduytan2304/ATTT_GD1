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
            "password": password}
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()

        check_Pri_User(cursor)

    except:
        pass

# Hàm kiểm tra quyền trên bảng của User
def check_Pri_User(cursor):
    pri_user_Window = Tk()
    pri_user_Window.title("Object Privilege Users")
    pri_user_Window.geometry("720x400")

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
            for i in tree_User_Pri.get_children():
                tree_User_Pri.delete(i)
            cursor.execute("select * from sys.check_privilege_user where username = '{}'".format(val_name))
            rows_user_pri = cursor.fetchall()
            for row in rows_user_pri:
                tree_User_Pri.insert(parent='', index='end', values=row)

    # khung nhập tên user
    inputUser = Entry(
        pri_user_Window,
        width = 60)
    inputUser.insert(END, "Input username")
    inputUser.grid(row=1, column=0)

    # nút bấm tìm kiếm
    press_Search = Button(pri_user_Window,
        text = "Search",
        width = 10,
        command = searchUser_Ob).grid(row=1, column=2)
    
    # bảng hiển thị quyền
    table_Search = Frame(pri_user_Window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=2, columnspan=3, padx=10)

    tree_scroll_User = Scrollbar(table_Search)
    tree_scroll_User.pack(side=RIGHT, fill=Y)

    tree_User_Pri = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_User.set)
    tree_User_Pri.pack()

    tree_scroll_User.config(command=tree_User_Pri.yview)
    tree_User_Pri['columns'] = ("1","2","3","4","5","6","7")
    tree_User_Pri['show'] = 'headings'
    tree_User_Pri.column("1", anchor=CENTER, width=90,minwidth=25)
    tree_User_Pri.column("2", anchor=CENTER, width=90)
    tree_User_Pri.column("3", anchor=CENTER, width=90)
    tree_User_Pri.column("4", anchor=CENTER, width=90)
    tree_User_Pri.column("5", anchor=CENTER, width=90)
    tree_User_Pri.column("6", anchor=CENTER, width=90)
    tree_User_Pri.column("7", anchor=CENTER, width=90)

    tree_User_Pri.heading("1", text="USERNAME", anchor=CENTER)
    tree_User_Pri.heading("2",text = "PRIVILEGE", anchor=CENTER)
    tree_User_Pri.heading("3", text = "OWNER", anchor=CENTER)
    tree_User_Pri.heading("4", text = "TABLE_NAME", anchor=CENTER)
    tree_User_Pri.heading("5", text = "COLUMN_NAME", anchor=CENTER)
    tree_User_Pri.heading("6", text = "ADMIN_OPTION", anchor=CENTER)
    tree_User_Pri.heading("7", text = "ACCESS_TYPE", anchor=CENTER)

