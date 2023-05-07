from tkinter import *
from tkinter import ttk
import oracledb
from tkinter import messagebox
from functools import partial
import datetime

global cursor
table_Search = None
tree_scroll_Truongphong = None
tree = None

def truongphong_window(username, password):
    try:
        dsn = {
            "host": "localhost",
            "port": "1521",
            "sid": "xe",
            "user": username,
            "password": password}
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()

        truongphong_Window = Tk()
        truongphong_Window.title("Trưởng phòng")
        truongphong_Window.geometry("1050x520")
        
        table_Search = Frame(truongphong_Window, padx = 10, pady = 10, borderwidth=10)
        table_Search.grid(row=1, column=2, rowspan=14, padx=10)

        tree_scroll_Truongphong = Scrollbar(table_Search)
        tree_scroll_Truongphong.pack(side=RIGHT, fill=Y)

        tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Truongphong.set)
        tree.pack()

        tree_scroll_Truongphong.config(command=tree.yview)
        tree['columns'] = ("1","2","3","4","5")
        tree['show'] = 'headings'
        tree.column("1", anchor=CENTER, width=90, stretch=NO)
        tree.column("2", anchor=CENTER, width=90, stretch=NO)
        tree.column("3", anchor=CENTER, width=90, stretch=NO)
        tree.column("4", anchor=CENTER, width=90, stretch=NO)
        tree.column("5", anchor=CENTER, width=90, stretch=NO)


        tree.heading("1", text="", anchor=CENTER)
        tree.heading("2",text = "", anchor=CENTER)
        tree.heading("3", text = "", anchor=CENTER)
        tree.heading("4", text = "", anchor=CENTER)
        tree.heading("5", text = "", anchor=CENTER)
        
        personal_infor_button = Button(truongphong_Window,
            text = "Xem thông tin cá nhân",
            width = 35,
            command =  partial(personal_infor, cursor, truongphong_Window))
        personal_infor_button.grid(row=1, column=1)

        update_personal_infor_button = Button(truongphong_Window,
            text = "Chỉnh sửa thông tin cá nhân",
            width = 35,
            command =  partial(update_personal_infor, cursor))
        update_personal_infor_button.grid(row=3, column=1)

        phancong_infor_button = Button(truongphong_Window,
            text = "Xem thông tin phân công",
            width = 35,
            command =  partial(phancong_infor, cursor, truongphong_Window))
        phancong_infor_button.grid(row=5, column=1)

        phongban_infor_button = Button(truongphong_Window,
            text = "Xem phòng ban",
            width = 35,
            command =  partial(phongban_infor, cursor, truongphong_Window))
        phongban_infor_button.grid(row=7, column=1)

        dean_infor_button = Button(truongphong_Window,
            text = "Xem đề án",
            width = 35,
            command =  partial(dean_infor, cursor, truongphong_Window))
        dean_infor_button.grid(row=9, column=1)

        nhanvien_infor_button = Button(truongphong_Window,
            text = "Xem danh sách nhân viên thuộc phòng ban",
            width = 35,
            command =  partial(nhanvien_infor, cursor, truongphong_Window))
        nhanvien_infor_button.grid(row=11, column=1)

        update_phancong_button = Button(truongphong_Window,
            text = "Thêm, xóa, sửa phân công",
            width = 35,
            command =  partial(update_phancong, cursor))
        update_phancong_button.grid(row=13, column=1)

        

    except:
        pass

def personal_infor(cursor, truongphong_Window):
    global table_Search, tree_scroll_Truongphong, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Truongphong is not None:
        tree_scroll_Truongphong.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(truongphong_Window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Truongphong = Scrollbar(table_Search)
    tree_scroll_Truongphong.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Truongphong.set)
    tree.pack()

    tree_scroll_Truongphong.config(command=tree.yview)
    tree['columns'] = ("1","2","3","4","5","6","7","8","9","10","11")
    tree['show'] = 'headings'
    tree.column("1", anchor=CENTER, width=50, stretch=NO)
    tree.column("2", anchor=CENTER, width=85, stretch=NO)
    tree.column("3", anchor=CENTER, width=50, stretch=NO)
    tree.column("4", anchor=CENTER, width=85, stretch=NO)
    tree.column("5", anchor=CENTER, width=85, stretch=NO)
    tree.column("6", anchor=CENTER, width=85, stretch=NO)
    tree.column("7", anchor=CENTER, width=50, stretch=NO)
    tree.column("8", anchor=CENTER, width=50, stretch=NO)
    tree.column("9", anchor=CENTER, width=85, stretch=NO)
    tree.column("10", anchor=CENTER, width=50, stretch=NO)
    tree.column("11", anchor=CENTER, width=50, stretch=NO)

    tree.heading("1", text="MANV", anchor=CENTER)
    tree.heading("2", text="TENNV", anchor=CENTER)
    tree.heading("3", text="PHAI", anchor=CENTER)
    tree.heading("4", text="NGAYSINH", anchor=CENTER)
    tree.heading("5", text="DIACHI", anchor=CENTER)
    tree.heading("6", text="SODT", anchor=CENTER)
    tree.heading("7", text="LUONG", anchor=CENTER)
    tree.heading("8", text="PHUCAP", anchor=CENTER)
    tree.heading("9", text="VAITRO", anchor=CENTER)
    tree.heading("10", text="MANQL", anchor=CENTER)
    tree.heading("11", text="PHG", anchor=CENTER)
    cursor.execute("select * from system.view_decrypt_NHANVIEN_LUONG")
    rows = cursor.fetchall()
    count = 1
    list_data = []
    for row in rows:
        for data in row:
            if count == 4:
                date = data.strftime('%d/%m/%Y')
                list_data.append(date)
            else:
                list_data.append(data)
            count = count + 1
        new_tup = tuple(list_data)
        tree.insert(parent='', index='end', values=new_tup)

def phancong_infor(cursor, truongphong_Window):
    global table_Search, tree_scroll_Truongphong, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Truongphong is not None:
        tree_scroll_Truongphong.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(truongphong_Window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Truongphong = Scrollbar(table_Search)
    tree_scroll_Truongphong.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Truongphong.set)
    tree.pack()

    tree_scroll_Truongphong.config(command=tree.yview)
    tree['columns'] = ("1","2","3")
    tree['show'] = 'headings'
    tree.column("1", anchor=CENTER, width=150, stretch=NO)
    tree.column("2", anchor=CENTER, width=150, stretch=NO)
    tree.column("3", anchor=CENTER, width=150, stretch=NO)

    tree.heading("1", text="MANV", anchor=CENTER)
    tree.heading("2",text = "MADA", anchor=CENTER)
    tree.heading("3", text = "THOIGIAN", anchor=CENTER)
    cursor.execute("select * from system.View_Select_PhanCong_Info")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert(parent='', index='end', values=row)


def update_personal_infor(cursor):
    pass

def phongban_infor(cursor, truongphong_Window):
    global table_Search, tree_scroll_Truongphong, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Truongphong is not None:
        tree_scroll_Truongphong.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(truongphong_Window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Truongphong = Scrollbar(table_Search)
    tree_scroll_Truongphong.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Truongphong.set)
    tree.pack()

    tree_scroll_Truongphong.config(command=tree.yview)
    tree['columns'] = ("1","2","3")
    tree['show'] = 'headings'
    tree.column("1", anchor=CENTER, width=150, stretch=NO)
    tree.column("2", anchor=CENTER, width=150, stretch=NO)
    tree.column("3", anchor=CENTER, width=150, stretch=NO)

    tree.heading("1", text="MAPB", anchor=CENTER)
    tree.heading("2",text = "TENPB", anchor=CENTER)
    tree.heading("3", text = "TRPHG", anchor=CENTER)
    cursor.execute("select * from system.phongban")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert(parent='', index='end', values=row)

def dean_infor(cursor, truongphong_Window):
    global table_Search, tree_scroll_Truongphong, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Truongphong is not None:
        tree_scroll_Truongphong.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(truongphong_Window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Truongphong = Scrollbar(table_Search)
    tree_scroll_Truongphong.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Truongphong.set)
    tree.pack()

    tree_scroll_Truongphong.config(command=tree.yview)
    tree['columns'] = ("1","2","3","4")
    tree['show'] = 'headings'
    tree.column("1", anchor=CENTER, width=120, stretch=NO)
    tree.column("2", anchor=CENTER, width=120, stretch=NO)
    tree.column("3", anchor=CENTER, width=120, stretch=NO)
    tree.column("4", anchor=CENTER, width=120, stretch=NO)

    tree.heading("1", text="MADA", anchor=CENTER)
    tree.heading("2",text = "TENDA", anchor=CENTER)
    tree.heading("3", text = "NGAYBD", anchor=CENTER)
    tree.heading("4", text = "PHONG", anchor=CENTER)
    cursor.execute("select * from system.DEAN")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert(parent='', index='end', values=row)

def nhanvien_infor(cursor, truongphong_Window):
    global table_Search, tree_scroll_Truongphong, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Truongphong is not None:
        tree_scroll_Truongphong.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(truongphong_Window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Truongphong = Scrollbar(table_Search)
    tree_scroll_Truongphong.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Truongphong.set)
    tree.pack()

    tree_scroll_Truongphong.config(command=tree.yview)
    tree['columns'] = ("1","2","3","4","5","6","7","8","9")
    tree['show'] = 'headings'
    tree.column("1", anchor=CENTER, width=60, stretch=NO)
    tree.column("2", anchor=CENTER, width=90, stretch=NO)
    tree.column("3", anchor=CENTER, width=60, stretch=NO)
    tree.column("4", anchor=CENTER, width=90, stretch=NO)
    tree.column("5", anchor=CENTER, width=90, stretch=NO)
    tree.column("6", anchor=CENTER, width=90, stretch=NO)
    tree.column("7", anchor=CENTER, width=90, stretch=NO)
    tree.column("8", anchor=CENTER, width=60, stretch=NO)
    tree.column("9", anchor=CENTER, width=60, stretch=NO)

    tree.heading("1", text="MANV", anchor=CENTER)
    tree.heading("2",text = "TENNV", anchor=CENTER)
    tree.heading("3", text = "PHAI", anchor=CENTER)
    tree.heading("4", text = "NGAYSINH", anchor=CENTER)
    tree.heading("5", text="DIACHI", anchor=CENTER)
    tree.heading("6",text = "SODT", anchor=CENTER)
    tree.heading("7", text = "VAITRO", anchor=CENTER)
    tree.heading("8", text = "MANQL", anchor=CENTER)
    tree.heading("9", text = "PHG", anchor=CENTER)
    cursor.execute("select * from system.View_TruongPhong_Select_NhanVien_Info")
    rows = cursor.fetchall()
    list_data = []
    for row in rows:
        count = 1
        for data in row:
            if count == 4:
                date = data.strftime('%d/%m/%Y')
                list_data.append(date)
            else:
                list_data.append(data)
            count = count + 1
        new_tup = tuple(list_data)
        tree.insert(parent='', index='end', values=new_tup)
        list_data = []

def update_phancong(cursor):
    pass