from tkinter import *
from tkcalendar import DateEntry

update_root = Tk()
update_root.title("Ngày Sinh")
update_root.geometry("250x100")

privilege_label = Label(update_root, text="Privilege:").grid(row = 0, column = 0, padx = 10)
privilage_entry = Entry(update_root)
privilage_entry.grid(row = 0, column = 1,pady = 10)

btn = Button(
            update_root, 
            text = "Revoke", 
            width = 10, 
            height= 1)
btn.grid(
        row = 1, 
        column = 1,
        columnspan = 3
        )
update_root.mainloop()






