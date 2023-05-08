import oracledb
from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def Revoke(privilage_entry,object_entry,user_entry,cursor):
    p = privilage_entry.get()
    o = object_entry.get()
    u = user_entry.get()
    u = u.upper()

    try:

        if o == '':
            print(f"Revoke {p} from {u}")
            cursor.execute(f"Revoke {p} from {u}")
        else:
            print(f"Revoke {p} on {o} from {u}")
            cursor.execute(f"Revoke {p} on {o} from {u}")
                  
        messagebox.showinfo("SUCCESS", "Revoke privilage success")
    except :
        messagebox.showerror("FAILED", "Revoke privilage failed")
    


def Revoke_privilege_form_user(username,password):
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

        Ru = Tk()
        Ru.title("Revoke Privilege from User")
        Ru.geometry("300x220")

        privilege_label = Label(Ru, text="Privilege:").grid(row = 0, column = 0)
        privilage_entry = Entry(Ru)
        privilage_entry.grid(row = 0, column = 2)

        object_label = Label(Ru, text="Object:").grid(row = 1, column = 0)
        object_entry = Entry(Ru)
        object_entry.grid(row = 1, column = 2)

        user_label = Label(Ru, text="User:").grid(row = 2, column = 0)
        user_entry = Entry(Ru)
        user_entry.grid(row = 2, column = 2)

        btn = Button(
            Ru, 
            text = "Revoke", 
            width = 20, 
            height= 1,
            command=lambda: Revoke(privilage_entry,object_entry,user_entry,cursor)
        ).grid(
            row = 4, 
            column = 1,
            columnspan = 3
        )

        Ru.mainloop()

        
    except:
        pass

def Revoke_privilege_form_role(username,password):
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

        Rr = Tk()
        Rr.title("Revoke Privilege from User")
        Rr.geometry("300x220")

        privilege_label = Label(Rr, text="Privilege:").grid(row = 0, column = 0)
        privilage_entry = Entry(Rr)
        privilage_entry.grid(row = 0, column = 2)

        object_label = Label(Rr, text="Object:").grid(row = 1, column = 0)
        object_entry = Entry(Rr)
        object_entry.grid(row = 1, column = 2)

        user_label = Label(Rr, text="Role:").grid(row = 2, column = 0)
        user_entry = Entry(Rr)
        user_entry.grid(row = 2, column = 2)

        btn = Button(
            Rr, 
            text = "Revoke", 
            width = 20, 
            height= 1,
            command=lambda: Revoke(privilage_entry,object_entry,user_entry,cursor)
        ).grid(
            row = 4, 
            column = 1,
            columnspan = 3
        )

        Rr.mainloop()

        
    except:
        pass