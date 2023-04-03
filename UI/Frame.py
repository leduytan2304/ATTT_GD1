import tkinter as tk
import oracledb
from tkinter import *
root = tk.Tk()
root.title("Hệ thống quản lý bệnh viện")
root.geometry("400x320")

privilege = tk.Label(root, text="Privilege")
privilege.place(x=60, y = 40)
privilege.config(font=("Arial", 12))
privilege_entry = tk.Entry(root)
privilege_entry.place(x=160, y = 45)


object = tk.Label(root, text="Object")
object.place(x=60, y = 80)
object.config(font=("Arial", 12))
object_entry = tk.Entry(root)
object_entry.place(x=160, y = 85)



username = tk.Label(root, text="Username")
username.place(x=60, y = 120)
username.config(font=("Arial", 12))
username_entry = tk.Entry(root)
username_entry.place(x=160, y = 125)

check = StringVar()
c = Checkbutton(root, text="With grant option", variable=check)
c.place(x=160, y = 145)


privilege_data =privilege_entry.get()
object_data= object_entry.get()
user_data = username_entry.get()

Execute_btn = tk.Button(root, text="Grant user privilege")# button Drop User
Execute_btn.place(x= 180, y = 200)






root.mainloop()