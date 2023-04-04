
import tkinter as tk
from tkinter import *
from tkinter import ttk
import oracledb
def TreeView(root, userName, passWord):   
    try:
        dsn = {
                "host": "localhost",
                "port": "1521",
                "sid": "xe",
                "user": userName,
                "password": passWord,
                "mode": oracledb.SYSDBA }
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()
        print("Login success")
        cursor.execute("select username, user_id, account_status, created from DBA_users")
        global rows
        rows = cursor.fetchall()
        total = cursor.rowcount
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
        # my_tree.configure(selectmode="extended")


        scrollBarY.place(relx = 0.934 , rely = 0.128, width = 22, height = 432)
        scrollBarX.place(relx = 0.002 , rely = 0.922, width = 651, height = 22)


        my_tree.configure(
            columns=
            (
            "USERNAME", 
            "USER ID",
            "ACCOUNT STATUS", 
            "CREATED DATE"
            )
        )


        my_tree.heading("#0", text = "ID",anchor=W)
        my_tree.heading("USERNAME", text = "USERNAME",anchor=W)
        my_tree.heading("USER ID", text = "USER ID",anchor=W)
        my_tree.heading("ACCOUNT STATUS", text = "ACCOUNT STATUS",anchor=W)
        my_tree.heading("CREATED DATE", text = "CREATED DATE",anchor=W)
        for i in rows:
            my_tree.insert('','end', values = i)



        #edit column 
        my_tree.column("#0",stretch=NO, minwidth=0,width=0)
        my_tree.column("#1",stretch=NO, minwidth=0,width=125)
        my_tree.column("#2",stretch=NO, minwidth=25,width=125)
        my_tree.column("#3",stretch=NO, minwidth=25,width=125)


        root.mainloop()






    except:
        pass

