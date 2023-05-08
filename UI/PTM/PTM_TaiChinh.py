from tkinter import *
from tkinter import ttk
import oracledb
from tkinter import messagebox
from functools import partial
import datetime

global cursor
table_Search = None
tree_scroll_Taichinh = None
tree = None
global connection

def taichinh_window(username, password):
    try:
        dsn = {
            "host": "localhost",
            "port": "1521",
            "sid": "xe",
            "user": username,
            "password": password}
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()

        taichinh_window = Tk()
        taichinh_window.title("Trưởng phòng")
        taichinh_window.geometry("1050x520")
        
        table_Search = Frame(taichinh_window, padx = 10, pady = 10, borderwidth=10)
        table_Search.grid(row=1, column=2, rowspan=14, padx=10)

        tree_scroll_Taichinh = Scrollbar(table_Search)
        tree_scroll_Taichinh.pack(side=RIGHT, fill=Y)

        tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Taichinh.set)
        tree.pack()

        tree_scroll_Taichinh.config(command=tree.yview)
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
        
        personal_infor_button = Button(taichinh_window,
            text = "Xem thông tin cá nhân",
            width = 35,
            command =  partial(personal_infor, cursor, taichinh_window))
        personal_infor_button.grid(row=1, column=1)

        update_personal_infor_button = Button(taichinh_window,
            text = "Chỉnh sửa thông tin cá nhân",
            width = 35,
            command =  partial(update_personal_infor, cursor, connection))
        update_personal_infor_button.grid(row=3, column=1)

        phancong_infor_button = Button(taichinh_window,
            text = "Xem thông tin phân công",
            width = 35,
            command =  partial(phancong_infor, cursor, taichinh_window))
        phancong_infor_button.grid(row=5, column=1)

        phongban_infor_button = Button(taichinh_window,
            text = "Xem phòng ban",
            width = 35,
            command =  partial(phongban_infor, cursor, taichinh_window))
        phongban_infor_button.grid(row=7, column=1)

        dean_infor_button = Button(taichinh_window,
            text = "Xem đề án",
            width = 35,
            command =  partial(dean_infor, cursor, taichinh_window))
        dean_infor_button.grid(row=9, column=1)

        view_all_nv_button = Button(taichinh_window,
            text = "Xem toàn bộ Nhân viên",
            width = 35,
            command =  partial(view_all_nv, cursor, taichinh_window))
        view_all_nv_button.grid(row=11, column=1)

        view_all_pc_button = Button(taichinh_window,
            text = "Xem toàn bộ Phân công",
            width = 35,
            command =  partial(view_all_pc, cursor, taichinh_window))
        view_all_pc_button.grid(row=13, column=1)

        update_luong_pc_button = Button(taichinh_window,
            text = "Cập nhật Lương, Phụ Cấp",
            width = 35,
            command =  partial(update_luong_phucap, cursor, taichinh_window, connection))
        update_luong_pc_button.grid(row=15, column=1)

        

    except:
        pass

def personal_infor(cursor, taichinh_window):
    global table_Search, tree_scroll_Taichinh, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Taichinh is not None:
        tree_scroll_Taichinh.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(taichinh_window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Taichinh = Scrollbar(table_Search)
    tree_scroll_Taichinh.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Taichinh.set)
    tree.pack()

    tree_scroll_Taichinh.config(command=tree.yview)
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
                if data == None:
                    list_data.append(data)
                else:
                    date = data.strftime('%d/%m/%Y')
                    list_data.append(date)
            else:
                list_data.append(data)
            count = count + 1
        new_tup = tuple(list_data)
        tree.insert(parent='', index='end', values=new_tup)

def phancong_infor(cursor, taichinh_window):
    global table_Search, tree_scroll_Taichinh, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Taichinh is not None:
        tree_scroll_Taichinh.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(taichinh_window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Taichinh = Scrollbar(table_Search)
    tree_scroll_Taichinh.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Taichinh.set)
    tree.pack()

    tree_scroll_Taichinh.config(command=tree.yview)
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

def update_personal_infor(cursor, connection):
    update_infor_Window = Tk()
    update_infor_Window.title("Cập nhật thông tin cá nhân")
    update_infor_Window.geometry("520x150")

    def update_ngaysinh():
        text = ngaysinh_input.get("1.0", "end-1c")
        if len(text) == 0:
            notify = messagebox.showinfo("Thông báo", "Ngày sinh đang để trống")
            return
        cursor.execute("select MANV from system.view_decrypt_NHANVIEN_LUONG")
        rows = cursor.fetchall()
        manv = rows[0][0]
        try:
            if text.upper() == 'NULL' or text == "Ngày sinh (DD-MM-YYYY)":
                text_ngaysinh = 'NULL'
                cursor.execute("update system.view_decrypt_NHANVIEN_LUONG set NGAYSINH = " + text_ngaysinh + " where MANV = '" + manv + "'")
            else:
                print(text)
                text_ngaysinh = "TO_DATE('" + text + "', 'DD-MM-YYYY')"
                cursor.execute("update system.view_decrypt_NHANVIEN_LUONG set NGAYSINH = " + text_ngaysinh + " where MANV = '" + manv + "'")
            connection.commit()
            notify = messagebox.showinfo("Cập nhật", "Kiểm tra lại thông tin cá nhân để xem kết quả cập nhật")
        except:
            notify = messagebox.showinfo("Cập nhật", "Cập nhật không thành công")
    def update_diachi():
        text = diachi_input.get("1.0", "end-1c")
        if len(text) == 0:
            notify = messagebox.showinfo("Thông báo", "Địa chỉ đang để trống")
            return
        cursor.execute("select MANV from system.view_decrypt_NHANVIEN_LUONG")
        rows = cursor.fetchall()
        manv = rows[0][0]
        try:
            if text.upper() == 'NULL' or text == "Địa chỉ":
                text = 'NULL'
                cursor.execute("update system.view_decrypt_NHANVIEN_LUONG set DIACHI = " + text + " where MANV = '" + manv + "'")
            else:
                cursor.execute("update system.view_decrypt_NHANVIEN_LUONG set DIACHI = '" + text + "' where MANV = '" + manv + "'")
            connection.commit()
            notify = messagebox.showinfo("Cập nhật", "Kiểm tra lại thông tin cá nhân để xem kết quả cập nhật")
        except:
            notify = messagebox.showinfo("Cập nhật", "Cập nhật không thành công")
    def update_sdt():
        text = sdt_input.get("1.0", "end-1c")
        if len(text) == 0:
            notify = messagebox.showinfo("Thông báo", "Số điện thoại đang để trống")
            return
        cursor.execute("select MANV from system.view_decrypt_NHANVIEN_LUONG")
        rows = cursor.fetchall()
        manv = rows[0][0]
        try:
            if text == "Số điện thoại":
                text = 'NULL'
            cursor.execute("update system.view_decrypt_NHANVIEN_LUONG set SODT = " + text + " where MANV = '" + manv + "'")
            connection.commit()
            notify = messagebox.showinfo("Cập nhật", "Kiểm tra lại thông tin cá nhân để xem kết quả cập nhật")
        except:
            notify = messagebox.showinfo("Cập nhật", "Cập nhật không thành công")

    label_ngaysinh = Label(update_infor_Window, text = "Ngày sinh:")
    label_ngaysinh.place(x=30, y=10)

    ngaysinh_input = Text(update_infor_Window, height=1, width=25)
    ngaysinh_input.place(x=110, y=10)
    ngaysinh_input.tag_configure("fade", foreground="#555555")
    ngaysinh_input.insert("end", "Ngày sinh (DD-MM-YYYY)", "fade")

    ngaysinh_button = Button(update_infor_Window,
            text = "Cập nhật ngày sinh",
            width = 20,
            command=update_ngaysinh)
    ngaysinh_button.place(x=330, y=7)

    label_diachi = Label(update_infor_Window, text = "Địa chỉ:")
    label_diachi.place(x=30, y=40)

    diachi_input = Text(update_infor_Window, height=1, width=25)
    diachi_input.place(x=110, y=40)
    diachi_input.tag_configure("fade", foreground="#555555")
    diachi_input.insert("end", "Địa chỉ", "fade")

    diachi_button = Button(update_infor_Window,
            text = "Cập nhật địa chỉ",
            width = 20,
            command=update_diachi)
    diachi_button.place(x=330, y=37)

    label_sdt = Label(update_infor_Window, text = "Số điện thoại:")
    label_sdt.place(x=30, y=70)

    sdt_input = Text(update_infor_Window, height=1, width=25)
    sdt_input.place(x=110, y=70)
    sdt_input.tag_configure("fade", foreground="#555555")
    sdt_input.insert("end", "Số điện thoại", "fade")

    sdt_button = Button(update_infor_Window,
            text = "Cập nhật số điện thoại",
            width = 20,
            command=update_sdt)
    sdt_button.place(x=330, y=67)

def nhanvien_infor(cursor, taichinh_window):
    global table_Search, tree_scroll_Taichinh, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Taichinh is not None:
        tree_scroll_Taichinh.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(taichinh_window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Taichinh = Scrollbar(table_Search)
    tree_scroll_Taichinh.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Taichinh.set)
    tree.pack()

    tree_scroll_Taichinh.config(command=tree.yview)
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

def phongban_infor(cursor, taichinh_window):
    global table_Search, tree_scroll_Taichinh, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Taichinh is not None:
        tree_scroll_Taichinh.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(taichinh_window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Taichinh = Scrollbar(table_Search)
    tree_scroll_Taichinh.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Taichinh.set)
    tree.pack()

    tree_scroll_Taichinh.config(command=tree.yview)
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

def dean_infor(cursor, taichinh_window):
    global table_Search, tree_scroll_Taichinh, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Taichinh is not None:
        tree_scroll_Taichinh.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(taichinh_window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Taichinh = Scrollbar(table_Search)
    tree_scroll_Taichinh.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Taichinh.set)
    tree.pack()

    tree_scroll_Taichinh.config(command=tree.yview)
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

def view_all_nv(cursor, taichinh_window):
    global table_Search, tree_scroll_Taichinh, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Taichinh is not None:
        tree_scroll_Taichinh.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(taichinh_window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Taichinh = Scrollbar(table_Search)
    tree_scroll_Taichinh.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Taichinh.set)
    tree.pack()

    tree_scroll_Taichinh.config(command=tree.yview)
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
    cursor.execute("select * from system.NHANVIEN")
    rows = cursor.fetchall()
    for i in rows:
        tree.insert('','end', values = i)


def update_luong_phucap(cursor, taichinh_window, connection):
    update_infor_Window = Tk()
    update_infor_Window.title("Cập nhật Lương và Phụ cấp")
    update_infor_Window.geometry("520x150")

    label_luong = Label(update_infor_Window, text = "Mã NV:")
    label_luong.place(x=30, y=10)

    nhanvien_input = Text(update_infor_Window, height=1, width=25)
    nhanvien_input.place(x=110, y=10)

    def update_luong():
        text = luong_input.get("1.0", "end-1c")
        manv = nhanvien_input.get("1.0", "end-1c")
        try:
            cursor.execute("update system.NHANVIEN set LUONG = " + text + " where MANV = '" + manv + "'")
            notify = messagebox.showinfo("Cập nhật", "Kiểm tra lại thông tin cá nhân để xem kết quả cập nhật")
            connection.commit()
        except:
            notify = messagebox.showinfo("Cập nhật", "Cập nhật không thành công")

    def update_phucap():
        text = phucap_input.get("1.0", "end-1c")
        manv = nhanvien_input.get("1.0", "end-1c")
        try:
            cursor.execute("update system.NHANVIEN set PHUCAP = " + text + " where MANV = '" + manv + "'")
            connection.commit()
            notify = messagebox.showinfo("Cập nhật", "Kiểm tra lại thông tin cá nhân để xem kết quả cập nhật")
        except:
            notify = messagebox.showinfo("Cập nhật", "Cập nhật không thành công")

    label_luong = Label(update_infor_Window, text = "Lương:")
    label_luong.place(x=30, y=40)

    luong_input = Text(update_infor_Window, height=1, width=25)
    luong_input.place(x=110, y=40)

    label_phuccap = Label(update_infor_Window, text = "Phụ cấp:")
    label_phuccap.place(x=30, y=70)

    phucap_input = Text(update_infor_Window, height=1, width=25)
    phucap_input.place(x=110, y=70)

    luong_button = Button(update_infor_Window,
            text = "Cập nhật Lương",
            width = 20,
            command=update_luong)
    luong_button.place(x=330, y=7)

    pc_button = Button(update_infor_Window,
            text = "Cập nhật Phụ cấp",
            width = 20,
            command=update_phucap)
    pc_button.place(x=330, y=60)



def view_all_pc(cursor, taichinh_window):
    global table_Search, tree_scroll_Taichinh, tree
    if table_Search is not None:
        table_Search.destroy()
    if tree_scroll_Taichinh is not None:
        tree_scroll_Taichinh.destroy()
    if tree is not None:
        tree.destroy()
    table_Search = Frame(taichinh_window, padx = 10, pady = 10, borderwidth=10)
    table_Search.grid(row=1, column=2, rowspan=14, padx=10)

    tree_scroll_Taichinh = Scrollbar(table_Search)
    tree_scroll_Taichinh.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(table_Search, yscrollcommand=tree_scroll_Taichinh.set)
    tree.pack()

    tree_scroll_Taichinh.config(command=tree.yview)
    tree['columns'] = ("1","2","3")
    tree['show'] = 'headings'
    tree.column("1", anchor=CENTER, width=120, stretch=NO)
    tree.column("2", anchor=CENTER, width=120, stretch=NO)
    tree.column("3", anchor=CENTER, width=120, stretch=NO)

    tree.heading("1", text="MANV", anchor=CENTER)
    tree.heading("2",text = "MADA", anchor=CENTER)
    tree.heading("3", text = "THOIGIAN", anchor=CENTER)
    cursor.execute("select * from system.PHANCONG")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert(parent='', index='end', values=row)