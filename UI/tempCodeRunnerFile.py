my_menu = Menu(newRoot)
#     newRoot.config(menu = my_menu)

#     def our_command():
#         pass

#     role = Menu(my_menu)

#     my_menu.add_cascade(label ="Role", menu = role)# tao menu Role
#     role.add_command(label ="Create", command = partial(crl_ptm, username, password))
#     role.add_command(label ="Drop", command = partial(drl_ptm, username, password))
   

#     privileges = Menu(my_menu)

#     my_menu.add_cascade(label ="Privilege", menu = privileges)# tao menu Privilege
#     privileges.add_command(label ="Grant User Object Privilege",command = partial(gup_ldt,username, password))
#     privileges.add_command(label ="Grant Role for user",command = partial(gru_ldt,username, password))
#     privileges.add_command(label ="Grant Role Privilege",command = partial(grp_ldt,username, password))
#     privileges.add_command(label ="Grant privilege on columns",command = partial(col_ldt,username, password))
#     privileges.add_command(label ="Revoke User Object Privilege",command = partial(RV.Revoke_privilege_form_user,username, password))
#     privileges.add_command(label ="Revoke Role Privilege",command = partial(RV.Revoke_privilege_form_role,username, password))

#     Check_privilege = Menu(my_menu)

#     my_menu.add_cascade(label ="Check Privilege", menu = Check_privilege)# tao menu Check Privilege
#     Check_privilege.add_command(label ="Check privilege of User", command = partial(cpu.checkPriUser_window, username, password)) 
#     Check_privilege.add_command(label ="Check privilege of Role",command = partial(cpr.checkPriRole_window, username, password))
    
#     def createUser():
#         cur = tv.active_login(username, password)
#         print(username, password)

#         createUser = tk.Tk()
#         createUser.title("Create User")
#         createUser.geometry("400x300")

#         username_label = tk.Label(createUser, text="Username:")
#         username_label.grid(row=0, column=0)
#         password_label = tk.Label(createUser, text="Password:")
#         password_label.grid(row=1, column=0)
        
#         def create_User():
#             new_username = username_entry.get()
#             new_password = password_entry.get()
#             create_txt = "CREATE USER " + new_username + " IDENTIFIED BY " + new_password
#             grant_txt = "GRANT CREATE SESSION TO " + new_username
#             print(create_txt)
#             cur.execute('alter session set "_ORACLE_SCRIPT" = true')
#             cur.execute(create_txt)
#             cur.execute(grant_txt)
#             messagebox.showinfo("Notification", ("Create user success") )

        
#         username_entry = tk.Entry(createUser)
#         username_entry.grid(row=0, column=1)
#         password_entry = tk.Entry(createUser)
#         password_entry.grid(row=1, column=1)
#         submit_button = tk.Button(createUser, text="Create", command=create_User)
#         submit_button.grid(row=2, column=1)

#     def dropUser():
#         cur = tv.active_login(username, password)

#         dropUser = tk.Tk()
#         dropUser.title("Drop User")
#         dropUser.geometry("400x150")

#         username_label = tk.Label(dropUser, text="Username:")
#         username_label.pack()

#         def drop_User():
#             sqltxt = "DROP USER " + username_entry.get()
#             print(sqltxt)
#             cur.execute('alter session set "_ORACLE_SCRIPT" = true')
#             cur.execute(sqltxt)
#             messagebox.showinfo("Notification", ("Drop user success") )
#         username_entry = tk.Entry(dropUser)
#         username_entry.pack()
#         submit_button = tk.Button(dropUser, text="Drop", command=drop_User)
#         submit_button.pack()
        
        
#     def userList():
#         tv.TreeView(newRoot, username, password)

#     def tableList():
#         tv.tableList(newRoot,username, password)

    
    
    
#     label = tk.Label(newRoot, text="List of user")
#     label.config(font=("Arial", 18))
#     label.place( x= 10, y = 40)

#     btn1 = tk.Button(newRoot, text="Create User", command=createUser)
#     btn1.place(x= 200, y = 40)

#     btn2 = tk.Button(newRoot, text="Drop User", command=dropUser)
#     btn2.place(x= 300, y = 40)

#     btn3 = tk.Button(newRoot, text="User List", command=userList)
#     btn3.place(x= 400, y = 40)

#     btn4 = tk.Button(newRoot, text="Table List", command=tableList)
#     btn4.place(x= 500, y = 40)

    
#     tv.TreeView(newRoot,username, password) # module của TreeView
# def gup_ldt(username, password): #LDT lệnh sau khi click vào Grant User Object Privilege
#      gup.UI(username, password)  
# def grp_ldt(username, password):
#      grp.UI(username, password) 
# def gru_ldt(username, password):
#      gru.UI(username, password) 
# def col_ldt(username, password):
#      col.UI(username, password) 
    
   


# def crl_ptm(username, password):
#     crl.UI(username, password)

# def drl_ptm(username, password):
#     drl.UI(username, password)

# def gup_ldt(username, password): #LDT lệnh sau khi click vào Grant User Object Privilege
#     gup.UI(username, password)  

# def grp_ldt(username, password):
#     grp.UI(username, password) 
    
# def gru_ldt(username, password):
#     gru.UI(username, password) 


# def crl_ptm(username, password):
#     crl.UI(username, password)

# def drl_ptm(username, password):
#     drl.UI(username, password)

# def gup_ldt(username, password): #LDT lệnh sau khi click vào Grant User Object Privilege
#     gup.UI(username, password)  

# def grp_ldt(username, password):
#     grp.UI(username, password) 
    
# def gru_ldt(username, password):
#     gru.UI(username, password) 