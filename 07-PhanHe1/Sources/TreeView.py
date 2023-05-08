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
        cursor.execute("select username, user_id, account_status, created from DBA_users")
        global rows
        rows = cursor.fetchall()
        total = cursor.rowcount
        
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
            ( "USERNAME", 
            "USER ID",
            "ACCOUNT STATUS", 
            "CREATED DATE" )
        )

        my_tree.heading("#0", text = "USERNAME",anchor=W)
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
        print("Error")

    

def tableList(root, userName, passWord):   
    try:
        cur = active_login(userName, passWord)
        cur.execute("SELECT USER, table_name FROM user_tables")
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
        root.mainloop()

        
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
            "mode": oracledb.SYSDBA }
        connection = oracledb.connect(**dsn)
        cursor = connection.cursor()
        return cursor
        
    except Exception as e:
        return None

