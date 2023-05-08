import tkinter as tk
import oracledb
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

def GiaoDienQL(username,password):
    dsn = {
            "host": "localhost",
            "port": "1521",
            "sid": "xe",
            "user": username,
            "password": str(password) }

    connection = oracledb.connect(**dsn)
    cursor = connection.cursor()
    print("Login success")

    def ThongTinNhanVien():

        cls = ('MANV',
                'TENNV',
                'PHAI', 
                'NGAYSINH', 
                'DIACHI', 
                'SODT', 
                'LUONG', 
                'PHUCAP', 
                'VAITRO', 
                'MANQL')

        ThongTin_root = Tk()
        ThongTin_root.geometry("300x420")
        ThongTin_root.title("Thông tin nhân viên")

        col_label = [0] * len(cls)
        for i, cl in enumerate(cls):
            col_label[i] = tk.Label(ThongTin_root, text=cl, font=("Helvetica", 10, "bold"))

        for i in range(0, len(cls)):
            col_label[i].grid(row=i, column=0, pady = 9, padx = 30)

        cursor.execute("SELECT * FROM system.view_NV_NhanVien")
        data = cursor.fetchone()


        for i, cl in enumerate(data):
            if cl == None:
                cl = 'NULL'
            col_label[i] = tk.Label(ThongTin_root, text=cl, font=("Helvetica", 10))

        for i in range(0, len(data)):
            col_label[i].grid(row=i, column=1, pady = 9,padx = 10)


    def ThongTinPhanCong():

        cls = ('MANV',
                'MADA',
                'THOIGIAN', )

        ThongTin_root = Tk()
        ThongTin_root.geometry("300x200")
        ThongTin_root.title("Thông tin phân công")

        col_label = [0] * len(cls)
        for i, cl in enumerate(cls):
            col_label[i] = tk.Label(ThongTin_root, text=cl, font=("Helvetica", 10, "bold"))

        for i in range(0, len(cls)):
            col_label[i].grid(row=i, column=0, pady = 9, padx = 30)

        cursor.execute("SELECT * FROM system.view_NV_PhanCong")
        data = cursor.fetchone()


        for i, cl in enumerate(data):
            if cl == None:
                cl = 'NULL'
            col_label[i] = tk.Label(ThongTin_root, text=cl, font=("Helvetica", 10))

        for i in range(0, len(data)):
            col_label[i].grid(row=i, column=1, pady = 9,padx = 10)


    def CapNhatNhanVien():

        def NgaySinh():
            update_root = Tk()
            update_root.title("Ngày Sinh")
            update_root.geometry("250x100")

            date_picker = DateEntry(update_root, width=12, background='darkblue', foreground='white', borderwidth=2)
            date_picker.pack(padx=10, pady=10)

            def update():
                try:
                    selected_date = date_picker.get_date()
                    print("update system.view_NV_NhanVien set ngaysinh = TO_DATE('" + str(selected_date) + "', 'YYYY-MM-DD')")
                    cursor.execute("update system.view_NV_NhanVien set ngaysinh = TO_DATE('" + str(selected_date) + "', 'YYYY-MM-DD')")
                    connection.commit()
                    messagebox.showinfo("SUCCESS", "Update success")
                    update_root.destroy()
                except:
                    messagebox.showerror("FAILED", "Update failed")
                        

            button = Button(update_root, text="UPDATE",height = 2,width = 10, command=update)
            button.pack(padx=10, pady=10)

        def DiaChi():
            update_root = Tk()
            update_root.title("Địa Chỉ")
            update_root.geometry("250x100")

            diachi_label = Label(update_root, text="DiaChi:").grid(row = 0, column = 0, padx = 10)
            diachi_entry = Entry(update_root)
            diachi_entry.grid(row = 0, column = 1,pady = 10)

            def update():
                try:
                    temp = diachi_entry.get()
                    print("update system.view_NV_NhanVien set diachi = '" + str(temp) + "'")
                    cursor.execute("update system.view_NV_NhanVien set diachi = '" + str(temp) + "'")
                    connection.commit()
                    messagebox.showinfo("SUCCESS", "Update success")
                    update_root.destroy()
                except:
                    messagebox.showerror("FAILED", "Update failed")


            btn = Button(update_root, 
                        text = "UPDATE", 
                        width = 10, 
                        height= 1,
                        command=update)
            btn.grid(row = 1, 
                    column = 1,
                    columnspan = 3
                    )
            
        def SoDT():
            update_root = Tk()
            update_root.title("Số Điện Thoại")
            update_root.geometry("250x100")

            sodt_label = Label(update_root, text="SoDT:").grid(row = 0, column = 0, padx = 10)
            sodt_entry = Entry(update_root)
            sodt_entry.grid(row = 0, column = 1,pady = 10)

            def update():
                try:
                    temp = sodt_entry.get()
                    print("update system.view_NV_NhanVien set sodt = '" + str(temp) + "'")
                    cursor.execute("update system.view_NV_NhanVien set sodt = '" + str(temp) + "'")
                    connection.commit()
                    messagebox.showinfo("SUCCESS", "Update success")
                    update_root.destroy()
                except:
                    messagebox.showerror("FAILED", "Update failed")


            btn = Button(update_root, 
                        text = "UPDATE", 
                        width = 10, 
                        height= 1,
                        command=update)
            btn.grid(row = 1, 
                    column = 1,
                    columnspan = 3
                    )   

        update_root = Tk()
        update_root.geometry("320x100")
        update_root.title("Cập Nhật Nhân Viên")

        btn1 = tk.Button(update_root, 
                        text="NGAYSINH",
                        font=("Helvetica", 10), 
                        height = 2,
                        width = 10,
                        borderwidth=3,
                        command=NgaySinh)
        btn1.grid(row = 1, column = 0, pady = 15, padx = 5)

        btn2 = tk.Button(update_root, 
                        text="DIACHI",
                        font=("Helvetica", 10), 
                        height = 2,
                        width = 10,
                        borderwidth=3,
                        command=DiaChi)
        btn2.grid(row = 1, column = 1, pady = 15, padx = 5)

        btn3 = tk.Button(update_root, 
                        text="SODT",
                        font=("Helvetica", 10), 
                        height = 2,
                        width = 10,
                        borderwidth=3,
                        command=SoDT)
        btn3.grid(row = 1, column = 2, pady = 15, padx = 5)

    def ThongTinPhongBan():
        newRoot = Tk()
        newRoot.title("Phòng Ban")
        newRoot.geometry("350x250")
        my_menu = Menu(newRoot)
        newRoot.config(menu = my_menu)

        scrollBarX = Scrollbar(newRoot, orient=HORIZONTAL)
        scrollBarY = Scrollbar(newRoot, orient=VERTICAL)

        my_tree = ttk.Treeview(newRoot)
        my_tree.place(relx = 0.03,rely = 0.05, width = 300, height = 210)
        my_tree.configure(yscrollcommand= scrollBarY.set, xscrollcommand= scrollBarX.set)
        my_tree.configure(selectmode="extended")

        scrollBarY.configure(command=my_tree.yview)
        scrollBarX.configure(command=my_tree.xview)
        # my_tree.configure(selectmode="extended")

        scrollBarY.place(relx = 0.934 , rely = 0.128, width = 22, height = 432)
        scrollBarX.place(relx = 0.002 , rely = 0.922, width = 651, height = 22)

        cls = ('MAPB',
            'TENPB',
            'TRPHG')

        my_tree.configure(
            columns = cls
        )

        for i, cl in enumerate(cls):
            my_tree.heading(i, text=cl, anchor="center")

        my_tree.column("#0",stretch=NO, minwidth=0,width=0)

        for i, cl in enumerate(cls):
            my_tree.column(i, stretch=NO, minwidth=25,width=100, anchor="center")

        cursor.execute("SELECT * FROM system.phongban")
        rows = cursor.fetchall()

        for i in rows:
            my_tree.insert('','end', values = i)


    def ThongTinDeAn():
        newRoot = Tk()
        newRoot.title("Đề Án")
        newRoot.geometry("500x250")
        my_menu = Menu(newRoot)
        newRoot.config(menu = my_menu)

        scrollBarX = Scrollbar(newRoot, orient=HORIZONTAL)
        scrollBarY = Scrollbar(newRoot, orient=VERTICAL)

        my_tree = ttk.Treeview(newRoot)
        my_tree.place(relx = 0.03,rely = 0.05, width = 400, height = 210)
        my_tree.configure(yscrollcommand= scrollBarY.set, xscrollcommand= scrollBarX.set)
        my_tree.configure(selectmode="extended")

        scrollBarY.configure(command=my_tree.yview)
        scrollBarX.configure(command=my_tree.xview)
        # my_tree.configure(selectmode="extended")

        scrollBarY.place(relx = 0.934 , rely = 0.128, width = 22, height = 432)
        scrollBarX.place(relx = 0.002 , rely = 0.922, width = 651, height = 22)

        cls = ('MADA',
            'TENDA',
            'NGAYBD',
            'PHONG')

        my_tree.configure(
            columns = cls
        )

        for i, cl in enumerate(cls):
            my_tree.heading(i, text=cl, anchor="center")

        my_tree.column("#0",stretch=NO, minwidth=0,width=0)

        for i, cl in enumerate(cls):
            my_tree.column(i, stretch=NO, minwidth=25,width=100, anchor="center")

        cursor.execute("SELECT * FROM system.dean")
        rows = cursor.fetchall()

        for i in rows:
            my_tree.insert('','end', values = i)

    def ThongTinQLNhanVien():
        newRoot = Tk()
        newRoot.title("Nhân Viên Quản Lý")
        newRoot.geometry("800x250")
        my_menu = Menu(newRoot)
        newRoot.config(menu = my_menu)

        scrollBarX = Scrollbar(newRoot, orient=HORIZONTAL)
        scrollBarY = Scrollbar(newRoot, orient=VERTICAL)

        my_tree = ttk.Treeview(newRoot)
        my_tree.place(relx = 0.03,rely = 0.05, width = 700, height = 210)
        my_tree.configure(yscrollcommand= scrollBarY.set, xscrollcommand= scrollBarX.set)
        my_tree.configure(selectmode="extended")

        scrollBarY.configure(command=my_tree.yview)
        scrollBarX.configure(command=my_tree.xview)
        # my_tree.configure(selectmode="extended")

        scrollBarY.place(relx = 0.934 , rely = 0.128, width = 22, height = 432)
        scrollBarX.place(relx = 0.002 , rely = 0.922, width = 651, height = 22)

        cls = ('MANV',
                'TENNV',
                'PHAI', 
                'NGAYSINH', 
                'DIACHI', 
                'SODT',  
                'VAITRO', 
                'MANQL')

        my_tree.configure(
            columns = cls
        )

        for i, cl in enumerate(cls):
            my_tree.heading(i, text=cl, anchor="center")

        my_tree.column("#0",stretch=NO, minwidth=0,width=0)

        for i, cl in enumerate(cls):
            my_tree.column(i, stretch=NO, minwidth=25,width=100, anchor="center")

        cursor.execute("SELECT * FROM system.view_QL_NhanVien")
        rows = cursor.fetchall()

        for i in rows:
            my_tree.insert('','end', values = i)

    def ThongTinQLPhanCong():
        newRoot = Tk()
        newRoot.title("Phân Công Quản Lý")
        newRoot.geometry("400x250")
        my_menu = Menu(newRoot)
        newRoot.config(menu = my_menu)

        scrollBarX = Scrollbar(newRoot, orient=HORIZONTAL)
        scrollBarY = Scrollbar(newRoot, orient=VERTICAL)

        my_tree = ttk.Treeview(newRoot)
        my_tree.place(relx = 0.03,rely = 0.05, width = 350, height = 210)
        my_tree.configure(yscrollcommand= scrollBarY.set, xscrollcommand= scrollBarX.set)
        my_tree.configure(selectmode="extended")

        scrollBarY.configure(command=my_tree.yview)
        scrollBarX.configure(command=my_tree.xview)
        # my_tree.configure(selectmode="extended")

        scrollBarY.place(relx = 0.934 , rely = 0.128, width = 22, height = 432)
        scrollBarX.place(relx = 0.002 , rely = 0.922, width = 651, height = 22)

        cls = ('MANV',
                'MADA',
                'THOIGIAN')

        my_tree.configure(
            columns = cls
        )

        for i, cl in enumerate(cls):
            my_tree.heading(i, text=cl, anchor="center")

        my_tree.column("#0",stretch=NO, minwidth=0,width=0)

        for i, cl in enumerate(cls):
            my_tree.column(i, stretch=NO, minwidth=25,width=100, anchor="center")

        cursor.execute("SELECT * FROM system.view_QL_PhanCong")
        rows = cursor.fetchall()

        for i in rows:
            my_tree.insert('','end', values = i)

    ChucNang_root = Tk()
    ChucNang_root.geometry("730x300")
    ChucNang_root.title("Quản Lý")

    nhanvien_label = tk.Label(ChucNang_root, text="Nhân Viên: ", font=("Helvetica", 10, "bold"))
    nhanvien_label.grid(row=0, column=0)

    btn1 = tk.Button(ChucNang_root, 
                    text="Select NhanVien",
                    font=("Helvetica", 10), 
                    height = 2,
                    width = 14,
                    borderwidth=3,
                    command=ThongTinNhanVien)
    btn1.grid(row = 1, column = 0, pady = 10, padx = 10)

    btn2 = tk.Button(ChucNang_root, 
                    text="Select PhanCong",
                    font=("Helvetica", 10), 
                    height = 2,
                    width = 14,
                    borderwidth=3,
                    command=ThongTinPhanCong)
    btn2.grid(row = 1, column = 1, pady = 10, padx = 10)

    btn3 = tk.Button(ChucNang_root, 
                    text="Update NhanVien",
                    font=("Helvetica", 10), 
                    height = 2,
                    width = 14,
                    borderwidth=3,
                    command=CapNhatNhanVien)
    btn3.grid(row = 1, column = 2, pady = 10, padx = 10)

    btn4 = tk.Button(ChucNang_root, 
                    text="Select PhongBan",
                    font=("Helvetica", 10), 
                    height = 2,
                    width = 14,
                    borderwidth=3,
                    command=ThongTinPhongBan)
    btn4.grid(row = 1, column = 3, pady = 10, padx = 10)

    btn5 = tk.Button(ChucNang_root, 
                    text="Select DeAn",
                    font=("Helvetica", 10), 
                    height = 2,
                    width = 14,
                    borderwidth=3,
                    command=ThongTinDeAn)
    btn5.grid(row = 1, column = 4, pady = 10, padx = 10)

    quanly_label = tk.Label(ChucNang_root, text="Quản Lý Trực Tiếp: ", font=("Helvetica", 10, "bold"))
    quanly_label.grid(row=2, column=0)

    btn6 = tk.Button(ChucNang_root, 
                    text="Select NhanVien",
                    font=("Helvetica", 10), 
                    height = 2,
                    width = 14,
                    borderwidth=3,
                    command=ThongTinQLNhanVien)
    btn6.grid(row = 3, column = 0, pady = 10, padx = 10)

    btn7 = tk.Button(ChucNang_root, 
                    text="Select PhanCong",
                    font=("Helvetica", 10), 
                    height = 2,
                    width = 14,
                    borderwidth=3,
                    command=ThongTinQLPhanCong)
    btn7.grid(row = 3, column = 1, pady = 10, padx = 10)

    ChucNang_root.mainloop()

GiaoDienQL('nv2',1)