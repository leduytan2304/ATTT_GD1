import tkinter as tk
import oracledb
from functools import partial
from tkinter import *
from tkinter import messagebox

from functools import partial
import tkinter as tk
from tkinter import *
from tkinter import ttk
import oracledb

def TreeView_LDT(root, userName, passWord):   
    try:
        dsn = {
            "host": "localhost",
            "port": "1521",
            "sid": "xe",
            "user": userName,
            "password": passWord,
            #"mode": oracledb.DEFAULT_AUTH 
            }
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()
        cursor.execute("select * from system.NHANVIEN")
        global rows
        rows = cursor.fetchall()
        total = cursor.rowcount
        print(total)
        
        scrollBarX = Scrollbar(root, orient=HORIZONTAL)
        scrollBarY = Scrollbar(root, orient=VERTICAL)

        my_tree = ttk.Treeview(root)
        my_tree.place(relx = 0.01,rely = 0.128, width = 646, height = 410)
        my_tree.configure(yscrollcommand= scrollBarY.set, xscrollcommand= scrollBarX.set)
        my_tree.configure(selectmode="extended")

        scrollBarY.configure(command=my_tree.yview)
        scrollBarX.configure(command=my_tree.xview)

        scrollBarY.place(relx = 0.934 , rely = 0.128, width = 22, height = 432)
        scrollBarX.place(relx = 0.002 , rely = 0.922, width = 651, height = 22)

        my_tree.configure(
            columns=
            ( "USER ID", 
            "USER Name",
            "Phai", 
            "NgaySinh",
             "DiaChi",
              "SoDT",
               "Luong",
                "PhuCap",
                 "VaiTro",
                  "MaNQL",
                   "NQL" )
        )

        my_tree.heading("USER ID", text = "USER ID",anchor=W)
        my_tree.heading("USER Name", text = "USER Name",anchor=W)
        my_tree.heading("Phai", text = "Phai",anchor=W)
        my_tree.heading("NgaySinh", text = "NgaySinh",anchor=W)
        my_tree.heading("DiaChi", text = "DiaChi",anchor=W)
        my_tree.heading("SoDT", text = "SoDT",anchor=W)
        my_tree.heading("Luong", text = "Luong",anchor=W)
        my_tree.heading("PhuCap", text = "PhuCap",anchor=W)
        my_tree.heading("VaiTro", text = "VaiTro",anchor=W)
        my_tree.heading("MaNQL", text = "MaNQL",anchor=W)
        my_tree.heading("NQL", text = "NQL",anchor=W)

        for i in rows:
            my_tree.insert('','end', values = i)

        #edit column 
        my_tree.column("#0",stretch=NO, minwidth=0,width=0)
        my_tree.column("#1",stretch=NO, minwidth=0,width=55)
        my_tree.column("#2",stretch=NO, minwidth=25,width=100)
        my_tree.column("#3",stretch=NO, minwidth=25,width=75)
        my_tree.column("#4",stretch=NO, minwidth=25,width=75)
        my_tree.column("#5",stretch=NO, minwidth=25,width=75)
        my_tree.column("#6",stretch=NO, minwidth=25,width=75)
        my_tree.column("#7",stretch=NO, minwidth=25,width=75)
        my_tree.column("#8",stretch=NO, minwidth=25,width=75)
        my_tree.column("#9",stretch=NO, minwidth=25,width=75)
        my_tree.column("#10",stretch=NO, minwidth=25,width=75)
        
        my_tree.mainloop()

    except:
        print("Error")

def tableList_LDT(root, userName, passWord):   
    try:
        cur = active_login(userName, passWord)
        cur.execute("select * from system.NHANVIEN")
        global rows
        rows = cur.fetchall()
        total = cur.rowcount
        print("total data entries: "+ str(total))
        for row in rows:
            print(row)
        
        scrollBarX = Scrollbar(root, orient=HORIZONTAL)
        scrollBarY = Scrollbar(root, orient=VERTICAL)

        my_tree = ttk.Treeview(root)
        my_tree.place(relx = 0.01,rely = 0.128, width = 646, height = 410)
        my_tree.configure(yscrollcommand= scrollBarY.set, xscrollcommand= scrollBarX.set)
        my_tree.configure(selectmode="extended")


        scrollBarY.configure(command=my_tree.yview)
        scrollBarX.configure(command=my_tree.xview)
        my_tree.configure(selectmode="extended")

        scrollBarY.place(relx = 0.934 , rely = 0.128, width = 22, height = 432)
        scrollBarX.place(relx = 0.002 , rely = 0.922, width = 651, height = 22)

        my_tree.configure(
            columns=("OWNER", 
            "TABLE NAME")
        )

        my_tree.heading("#0", text = "OWNER", anchor=W)
        my_tree.heading("#1", text = "TABLE NAME", anchor=W)

        for i in rows:
            my_tree.insert('','end', values = i)

        def on_select2(event):
            item = my_tree.focus()
            text = my_tree.item(item, "values")
            first_paramater = text[0]
            print(first_paramater)
            return first_paramater

        my_tree.bind("<<TreeviewSelect>>", on_select2)
        res = on_select2(None)
        print(res)
        
        #edit column 
        my_tree.column("#0",stretch=NO, minwidth=0,width=0)
        my_tree.column("#1",stretch=NO, minwidth=0,width=125)
        my_tree.mainloop()

        
    except Exception as e:
        print("An error occurred:", e)
        res = None
    return res


        
        


def active_login(username, password):
    try:
        dsn = {
            "host": "localhost",
            "port": "1521",
            "sid": "xe",
            "user": username,
            "password": password,
            #"mode": oracledb.DEFAULT_AUTH 
            }
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()
        
        return cursor
        
    except Exception as e:
        return None


def UI_Update(username, password):  

    root = tk.Tk()
    root.title("Update on DEAN")
    root.geometry("400x320")       
    MaDA = tk.Label(root, text="MaDA")
    MaDA.place(x=60, y = 40)
    MaDA.config(font=("Arial", 12))
    MaDA_entry = tk.Entry(root)
    MaDA_entry.place(x=160, y = 45)


    TenDA = tk.Label(root, text="TenDA")
    TenDA.place(x=60, y = 80)
    TenDA.config(font=("Arial", 12))
    TenDA_entry = tk.Entry(root)
    TenDA_entry.place(x=160, y = 85)

    NgayBD = tk.Label(root, text="NgayBD")
    NgayBD.place(x=60, y = 120)
    NgayBD.config(font=("Arial", 12))
    NgayBD_entry = tk.Entry(root)
    NgayBD_entry.place(x=160, y = 125)
   
    Phong = tk.Label(root, text="Phong")
    Phong.place(x=60, y = 160)
    Phong.config(font=("Arial", 12))
    Phong_entry = tk.Entry(root)
    Phong_entry.place(x=160, y = 165)   

    

    MaDA_data =MaDA_entry.get()
    TenDA_data = TenDA_entry.get()
    NgayBD_data = NgayBD_entry.get()
    Phong_data = Phong_entry.get()
    def print_data():
        if(MaDA_entry.get() ==""  or TenDA_entry.get() =="" or NgayBD_entry.get() =="" or Phong_entry.get() ==""):
            print("please input in all the textbox")
        else:
            MaDA_data =MaDA_entry.get()
            TenDA_data  = TenDA_entry.get()
            NgayBD_data = NgayBD_entry.get()
            Phong_data = Phong_entry.get()
            print(MaDA_entry.get())
            print(TenDA_entry.get())
            print(NgayBD_entry.get())
            print(Phong_entry.get())
            try:
                cur = active_login(username, password)
                sqlTxt = "UPDATE system.DEAN SET  TENDA ='" + TenDA_data +"', NGAYBD = TO_DATE('" + NgayBD_data +"', 'YYYY-MM-DD'), PHONG ='" + Phong_data +  "' WHERE MADA = '"+ MaDA_data + "'" 
                print("sql text:" + sqlTxt)
                cur.execute(sqlTxt)
                print("sql text:" + sqlTxt)
                cur.execute("COMMIT")
            except:
                print("da xay ra loi") 
        
           


    Execute_btn = tk.Button(root, text="Update", command=print_data)# button Drop User
    Execute_btn.place(x= 180, y = 200)
    #SELECT GRANTEE,GRANTED_ROLE FROM DBA_ROLE_PRIVS WHERE GRANTED_ROLE = 'DATAENTRY'
    root.mainloop()

def UI_Insert(username, password):  

    root = tk.Tk()
    root.title("Insert on DEAN")
    root.geometry("400x320")       
    MaDA = tk.Label(root, text="MaDA")
    MaDA.place(x=60, y = 40)
    MaDA.config(font=("Arial", 12))
    MaDA_entry = tk.Entry(root)
    MaDA_entry.place(x=160, y = 45)


    TenDA = tk.Label(root, text="TenDA")
    TenDA.place(x=60, y = 80)
    TenDA.config(font=("Arial", 12))
    TenDA_entry = tk.Entry(root)
    TenDA_entry.place(x=160, y = 85)

    NgayBD = tk.Label(root, text="NgayBD")
    NgayBD.place(x=60, y = 120)
    NgayBD.config(font=("Arial", 12))
    NgayBD_entry = tk.Entry(root)
    NgayBD_entry.place(x=160, y = 125)
   
    Phong = tk.Label(root, text="Phong")
    Phong.place(x=60, y = 160)
    Phong.config(font=("Arial", 12))
    Phong_entry = tk.Entry(root)
    Phong_entry.place(x=160, y = 165)   

    

    MaDA_data =MaDA_entry.get()
    TenDA_data = TenDA_entry.get()
    NgayBD_data = NgayBD_entry.get()
    Phong_data = Phong_entry.get()
    def print_data():
        if(MaDA_entry.get() ==""  or TenDA_entry.get() =="" or NgayBD_entry.get() =="" or Phong_entry.get() ==""):
            print("please input in all the textbox")
        else:
            MaDA_data =MaDA_entry.get()
            TenDA_data  = TenDA_entry.get()
            NgayBD_data = NgayBD_entry.get()
            Phong_data = Phong_entry.get()
            print(MaDA_entry.get())
            print(TenDA_entry.get())
            print(NgayBD_entry.get())
            print(Phong_entry.get())
            try:
                cur = active_login(username, password)
                sqlTxt = "insert into system.DEAN  (MADA, TENDA, NGAYBD, PHONG) values ('" + MaDA_data +"', '" + TenDA_data + "',  TO_DATE('" + NgayBD_data +"', 'YYYY-MM-DD'), '" + Phong_data + "') "
                print("sql text:" + sqlTxt)
                cur.execute(sqlTxt)
                print("sql text:" + sqlTxt)
                cur.execute("COMMIT")
            except:
                print("da xay ra loi") 
        
           


    Execute_btn = tk.Button(root, text="Insert", command=print_data)# button Drop User
    Execute_btn.place(x= 180, y = 200)
    #SELECT GRANTEE,GRANTED_ROLE FROM DBA_ROLE_PRIVS WHERE GRANTED_ROLE = 'DATAENTRY'
    root.mainloop()

def UI_Delete(username, password):  

    root = tk.Tk()
    root.title("Insert on DEAN")
    root.geometry("400x320")       
    MaDA = tk.Label(root, text="MaDA")
    MaDA.place(x=60, y = 40)
    MaDA.config(font=("Arial", 12))
    MaDA_entry = tk.Entry(root)
    MaDA_entry.place(x=160, y = 45)


    
    MaDA_data =MaDA_entry.get()
    def print_data_3():
        if(MaDA_entry.get() ==""):
            print("please input in all the textbox")
        else:
            MaDA_data =MaDA_entry.get()
            
            print(MaDA_entry.get())
            
            try:
                cur = active_login(username, password)
                #delete from system.DEAN where MADA = 'DA0007'; 
                sqlTxt = "delete from system.DEAN where MADA = '" + MaDA_data +"'" 
                print("sql text:" + sqlTxt)
                cur.execute(sqlTxt)
                print("sql text:" + sqlTxt)
                cur.execute("COMMIT")
            except:
                print("da xay ra loi") 
    Execute_btn = tk.Button(root, text="Delete", command=print_data_3)# button Drop User
    Execute_btn.place(x= 200, y = 200)
        #SELECT GRANTEE,GRANTED_ROLE FROM DBA_ROLE_PRIVS WHERE GRANTED_ROLE = 'DATAENTRY'
    root.mainloop()
 

        
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
        #"mode": oracledb 
        }
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()
        print("Login success")
        cursor.execute("select * from system.NHANVIEN")
        rows = cursor.fetchall()
        root.destroy()
        cursor.close()
        connection.close()
    
        afterLogin(username, password)
    except oracledb.DatabaseError as e:
        print("Login fail")
        return False
    

     

def afterLogin(username, password):

    #sau khi dang nhap hien 1 cửa sổ mới
    # if('NhanSu' in username):
    #     pass
    # else:
        newRoot = Tk()
        newRoot.title("Truong De An")
        newRoot.geometry("800x520")
        my_menu = Menu(newRoot)
        newRoot.config(menu = my_menu)

        role = Menu(my_menu)

      



       
   
        
            
            
        def userList():
            TreeView_LDT(newRoot, username, password)

        def tableList():
            tableList_LDT(newRoot,username, password)
        def Update_DEAN():
            UI_Update(username, password)
        def Delete_DEAN():
            UI_Delete(username, password)
        def Update_DEAN():
            UI_Insert(username, password)

        btn3 = tk.Button(newRoot, text="User List", command=userList)
        btn3.place(x= 50, y = 40)

        btn4 = tk.Button(newRoot, text="Table List", command=tableList)
        btn4.place(x= 120, y = 40)
        btn5 = tk.Button(newRoot, text="Update DEAN Info ", command=Update_DEAN)
        btn5.place(x= 200, y = 40)
        btn6 = tk.Button(newRoot, text="ADD NEW DEAN ", command=Update_DEAN)
        btn6.place(x= 350, y = 40)
        btn6 = tk.Button(newRoot, text=" DELETE DEAN ", command=Delete_DEAN)
        btn6.place(x= 500, y = 40)
       
        TreeView_LDT(newRoot,username, password) # module của TreeView


    

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

    