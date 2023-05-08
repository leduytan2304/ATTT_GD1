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
global connection

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
            command =  partial(update_personal_infor, cursor, connection))
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
            command =  partial(update_phancong, cursor, connection))
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
    cursor.execute("select * from system.view_NV_NhanVien")
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
    cursor.execute("select * from system.view_NV_PhanCong")
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
        cursor.execute("select MANV from system.view_NV_NhanVien")
        rows = cursor.fetchall()
        manv = rows[0][0]
        try:
            if text.upper() == 'NULL' or text == "Ngày sinh (DD-MM-YYYY)":
                text_ngaysinh = 'NULL'
                cursor.execute("update system.view_NV_NhanVien set NGAYSINH = " + text_ngaysinh + " where MANV = '" + manv + "'")
            else:
                print(text)
                text_ngaysinh = "TO_DATE('" + text + "', 'DD-MM-YYYY')"
                cursor.execute("update system.view_NV_NhanVien set NGAYSINH = " + text_ngaysinh + " where MANV = '" + manv + "'")
            connection.commit()
            notify = messagebox.showinfo("Cập nhật", "Kiểm tra lại thông tin cá nhân để xem kết quả cập nhật")
        except:
            notify = messagebox.showinfo("Cập nhật", "Cập nhật không thành công")

    def update_diachi():
        text = diachi_input.get("1.0", "end-1c")
        if len(text) == 0:
            notify = messagebox.showinfo("Thông báo", "Địa chỉ đang để trống")
            return
        cursor.execute("select MANV from system.view_NV_NhanVien")
        rows = cursor.fetchall()
        manv = rows[0][0]
        try:
            if text.upper() == 'NULL' or text == "Địa chỉ":
                text = 'NULL'
                cursor.execute("update system.view_NV_NhanVien set DIACHI = " + text + " where MANV = '" + manv + "'")
            else:
                cursor.execute("update system.view_NV_NhanVien set DIACHI = '" + text + "' where MANV = '" + manv + "'")
            connection.commit()
            notify = messagebox.showinfo("Cập nhật", "Kiểm tra lại thông tin cá nhân để xem kết quả cập nhật")
        except:
            notify = messagebox.showinfo("Cập nhật", "Cập nhật không thành công")
    def update_sdt():
        text = sdt_input.get("1.0", "end-1c")
        if len(text) == 0:
            notify = messagebox.showinfo("Thông báo", "Số điện thoại đang để trống")
            return
        cursor.execute("select MANV from system.view_NV_NhanVien")
        rows = cursor.fetchall()
        manv = rows[0][0]
        try:
            if text == "Số điện thoại":
                text = 'NULL'
            cursor.execute("update system.view_NV_NhanVien set SODT = " + text + " where MANV = '" + manv + "'")
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

def update_phancong(cursor, connection):
    update_phancong_Window = Tk()
    update_phancong_Window.title("Cập nhật thông tin cá nhân")
    update_phancong_Window.geometry("650x300")

    def check(MaNv, MaDa):
        cursor.execute("select MANV from system.view_NV_NhanVien")
        rows_manv = cursor.fetchall()
        manv = rows_manv[0][0]
        if MaNv == manv:
            return False
        cursor.execute("select MANV from system.View_TruongPhong_Select_NhanVien_Info")
        rows_nv_list = cursor.fetchall()
        list_msnv = []
        for row in rows_nv_list:
            list_msnv.append(row[0])
        if MaNv not in list_msnv:
            return False
        else:
            cursor.execute("select MADA from system.DEAN")
            rows_da_list = cursor.fetchall()
            list_da = []
            for row in rows_da_list:
                list_da.append(row[0])
            if MaDa in list_da:
                return True
            else:
                return False

    def insert_PhanCong():
        text_manv = insert_manv_input.get("1.0", "end-1c")
        if len(text_manv) == 0:
            notify = messagebox.showinfo("Thông báo", "Mã nhân viên đang trống")
            return
        text_mada = insert_mada_input.get("1.0", "end-1c")
        if len(text_mada) == 0:
            notify = messagebox.showinfo("Thông báo", "Mã đề án đang trống")
            return
        text_thoigian = insert_thoigian_input.get("1.0", "end-1c")
        if len(text_thoigian) == 0 or text_thoigian.upper() == 'NULL' or text_thoigian == "Thời gian (DD-MM-YYYY)":
            text_thoigian = "NULL"
        text_manv = text_manv.upper()
        text_mada = text_mada.upper()
        check_condition = check(text_manv, text_mada)
        if check_condition == False:
            notify = messagebox.showinfo("Thông báo", "Mã nhân viên hoặc mã đề án không hợp lệ")
            return
        try:
            if text_thoigian.upper() == 'NULL':
                cursor.execute("CALL system.INSERT_PHANCONG('" + text_manv + "','" + text_mada + "',NULL)")
            else:
                text_convert = "TO_DATE('" + text_thoigian + "', 'DD-MM-YYYY')"
                cursor.execute("CALL system.INSERT_PHANCONG('" + text_manv + "','" + text_mada + "'," + text_convert + ")")
            notify = messagebox.showinfo("Thông báo", "Thêm phân công thành công")
        except:
            notify = messagebox.showinfo("Thông báo", "Thêm phân công không thành công")
    def delete_PhanCong():
        text_manv = delete_manv_input.get("1.0", "end-1c")
        if len(text_manv) == 0:
            notify = messagebox.showinfo("Thông báo", "Mã nhân viên đang trống")
            return
        text_mada = delete_mada_input.get("1.0", "end-1c")
        if len(text_mada) == 0:
            notify = messagebox.showinfo("Thông báo", "Mã đề án đang trống")
            return
        text_manv = text_manv.upper()
        text_mada = text_mada.upper()
        check_condition = check(text_manv, text_mada)
        if check_condition == False:
            notify = messagebox.showinfo("Thông báo", "Mã nhân viên hoặc mã đề án không hợp lệ")
            return
        try:
            cursor.execute("CALL system.DELETE_PHANCONG('" + text_manv + "','" + text_mada + "')")
            notify = messagebox.showinfo("Thông báo", "Xóa phân công thành công")
        except:
            notify = messagebox.showinfo("Thông báo", "Xóa phân công không thành công")
    def update_PhanCong():
        text_manv = update_manv_input.get("1.0", "end-1c")
        if len(text_manv) == 0:
            notify = messagebox.showinfo("Thông báo", "Mã nhân viên đang trống")
            return
        text_mada = update_mada_input.get("1.0", "end-1c")
        if len(text_mada) == 0:
            notify = messagebox.showinfo("Thông báo", "Mã đề án đang trống")
            return
        text_thoigian = update_thoigian_input.get("1.0", "end-1c")
        if len(text_thoigian) == 0 or text_thoigian.upper() == 'NULL' or text_thoigian == "Thời gian (DD-MM-YYYY)":
            text_thoigian = "NULL"
        text_manv = text_manv.upper()
        text_mada = text_mada.upper()
        check_condition = check(text_manv, text_mada)
        if check_condition == False:
            notify = messagebox.showinfo("Thông báo", "Mã nhân viên hoặc mã đề án không hợp lệ")
            return
        try:
            if text_thoigian.upper() == 'NULL':
                cursor.execute("CALL system.UPDATE_PHANCONG('" + text_manv + "','" + text_mada + "',NULL)")
            else:
                text_convert = "TO_DATE('" + text_thoigian + "', 'DD-MM-YYYY')"
                print("CALL system.UPDATE_PHANCONG('" + text_manv + "','" + text_mada + "'," + text_convert + ")")
                cursor.execute("CALL system.UPDATE_PHANCONG('" + text_manv + "','" + text_mada + "'," + text_convert + ")")
            notify = messagebox.showinfo("Thông báo", "Cập nhật phân công thành công")
        except:
            notify = messagebox.showinfo("Thông báo", "Cập nhật phân công không thành công")
    
    
    # thêm label và ô input cho insert
    label_insert = Label(update_phancong_Window, text = "Thêm phân công")
    label_insert.place(x=30, y=10)

    label_insert_manv = Label(update_phancong_Window, text = "Mã nhân viên:")
    label_insert_manv.place(x=30, y=30)

    insert_manv_input = Text(update_phancong_Window, height=1, width=12)
    insert_manv_input.place(x=33, y=50)
    insert_manv_input.tag_configure("fade", foreground="#555555")
    insert_manv_input.insert("end", "Mã nhân viên", "fade")

    label_insert_mada = Label(update_phancong_Window, text = "Mã đề án:")
    label_insert_mada.place(x=140, y=30)

    insert_mada_input = Text(update_phancong_Window, height=1, width=12)
    insert_mada_input.place(x = 143, y=50)
    insert_mada_input.tag_configure("fade", foreground="#555555")
    insert_mada_input.insert("end", "Mã đề án", "fade")

    label_insert_thoigian = Label(update_phancong_Window, text = "Thời gian:")
    label_insert_thoigian.place(x=250, y=30)

    insert_thoigian_input = Text(update_phancong_Window, height=1, width=22)
    insert_thoigian_input.place(x=253, y=50)
    insert_thoigian_input.tag_configure("fade", foreground="#555555")
    insert_thoigian_input.insert("end", "Thời gian (DD-MM-YYYY)", "fade")
    

    insert_button = Button(update_phancong_Window,
            text = "Thêm phân công",
            width = 20,
            command=insert_PhanCong)
    insert_button.place(x=460, y=47)

    # thêm label và ô input cho delete
    label_delete = Label(update_phancong_Window, text = "Xóa phân công")
    label_delete.place(x=30, y=100)

    label_delete_manv = Label(update_phancong_Window, text = "Mã nhân viên:")
    label_delete_manv.place(x=30, y=120)

    delete_manv_input = Text(update_phancong_Window, height=1, width=12)
    delete_manv_input.place(x=33, y=140)
    delete_manv_input.tag_configure("fade", foreground="#555555")
    delete_manv_input.insert("end", "Mã nhân viên", "fade")

    label_delete_mada = Label(update_phancong_Window, text = "Mã đề án:")
    label_delete_mada.place(x=140, y=120)

    delete_mada_input = Text(update_phancong_Window, height=1, width=12)
    delete_mada_input.place(x = 143, y=140)
    delete_mada_input.tag_configure("fade", foreground="#555555")
    delete_mada_input.insert("end", "Mã đề án", "fade")

    delete_button = Button(update_phancong_Window,
            text = "Xóa phân công",
            width = 20,
            command=delete_PhanCong)
    delete_button.place(x=460, y=137)

    # thêm label và ô input cho update
    label_update = Label(update_phancong_Window, text = "Cập nhật phân công (cập nhật thời gian)")
    label_update.place(x=30, y=190)

    label_update_manv = Label(update_phancong_Window, text = "Mã nhân viên:")
    label_update_manv.place(x=30, y=210)

    update_manv_input = Text(update_phancong_Window, height=1, width=12)
    update_manv_input.place(x=33, y=230)
    update_manv_input.tag_configure("fade", foreground="#555555")
    update_manv_input.insert("end", "Mã nhân viên", "fade")

    label_update_mada = Label(update_phancong_Window, text = "Mã đề án:")
    label_update_mada.place(x=140, y=210)

    update_mada_input = Text(update_phancong_Window, height=1, width=12)
    update_mada_input.place(x = 143, y=230)
    update_mada_input.tag_configure("fade", foreground="#555555")
    update_mada_input.insert("end", "Mã đề án", "fade")

    label_update_thoigian = Label(update_phancong_Window, text = "Thời gian:")
    label_update_thoigian.place(x=250, y=210)

    update_thoigian_input = Text(update_phancong_Window, height=1, width=22)
    update_thoigian_input.place(x=253, y=230)
    update_thoigian_input.tag_configure("fade", foreground="#555555")
    update_thoigian_input.insert("end", "Thời gian (DD-MM-YYYY)", "fade")
    

    update_button = Button(update_phancong_Window,
            text = "Cập nhật phân công",
            width = 20,
            command=update_PhanCong)
    update_button.place(x=460, y=227)