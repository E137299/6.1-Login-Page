from tkinter import *
import re

root = Tk()
root.title("Login Page")
root.geometry("800x600+20+20")

#### Model ####
# Define a function to add placeholder functionality to an Entry widget
def create_entry_with_placeholder(parent, default_text, x, y, width, height, is_password=False):
    entry = Entry(parent, fg='grey')
    entry.default_text = default_text  # Store the default text
    entry.is_password = is_password  # Track if this entry is for passwords
    entry.insert(0, default_text)

    # Bind events to the entry widget for placeholder functionality
    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focusout)
    
    entry.place(x=x, y=y, width=width, height=height)
    return entry

# Function to remove placeholder text when the entry gets clicked
def on_entry_click(event):
    entry_widget = event.widget
    if entry_widget.get() == entry_widget.default_text:
        entry_widget.delete(0, END)  # Remove the placeholder text
        entry_widget.config(fg='black')  # Change text color to normal
        # If it's a password field, enable the masking
        if entry_widget.is_password:
            entry_widget.config(show="*")

# Function to restore placeholder text if entry is left empty
def on_focusout(event):
    entry_widget = event.widget
    if entry_widget.get() == "":
        entry_widget.insert(0, entry_widget.default_text)  # Restore placeholder text
        entry_widget.config(fg='grey')
        # If it's a password field, disable the masking when showing the placeholder
        if entry_widget.is_password:
            entry_widget.config(show="")

def verify_login():
    # global name
    name.set(username_entry.get())
    password = password_entry.get()


    if name.get() in logins and logins[name.get()]==password:
        frame2.tkraise()
        username_entry.delete(0, END)
        username_entry.insert(0, "Enter your username")  # Insert placeholder text
        username_entry.config(fg='grey')
        password_entry.delete(0, END)
        

    else:
        error.config(text = "Either the username or password is incorrect.\nPlease reenter your credentials.")
        username_entry.delete(0, END)
        username_entry.insert(0, "Enter your username")  # Insert placeholder text
        username_entry.config(fg='grey')
        password_entry.delete(0, END)

def return_login():
    frame1.tkraise()

def register_account():
    frame3.tkraise()

def is_cred_good():
    print(reg_username_entry.get(), reg_password_entry1.get(), reg_password_entry2.get())
    if reg_username_entry.get() in logins:
        reg_error.config(text = "The username is already registered\n to an existing account.")
        return False
    if reg_password_entry1.get() != reg_password_entry2.get():
        reg_error.config(text = "The passwords do not match.")
        return False
    if len(reg_password_entry1.get()) < 10:
        reg_error.config(text = "The password must have ten or more characters.")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", reg_password_entry1.get()):
        reg_error.config(text = "The password must contain at\n least one special character")
        return False
    if not re.search(r"\d", reg_password_entry1.get()):
        reg_error.config(text = "The password must contain\n at lease one number.")
        return False
    if not re.search(r"[a-z]", reg_password_entry1.get()):
        reg_error.config(text = "The password must contain\n at lease one lowercase letter.")
        return False
    if not re.search(r"[A-Z]", reg_password_entry1.get()):
        reg_error.config(text = "The password must contain\n at lease one uppercase letter.")
        return False
    
    return True

def check_registration():
    if is_cred_good():
        print("Good")
        logins[reg_username_entry.get()] = reg_password_entry1.get()
        reg_error.config(text = "")
        return_login()
    

name = StringVar()
name.set("")

logins ={"DavidYin":"123Password!"}

frame3 = Frame(root,width = 800,height=6000, bg = "teal")
frame3.place(x=0, y=0, width = 800,height=6000)

frame2 = Frame(root,width = 800,height=6000, bg = "teal")
frame2.place(x=0, y=0, width = 800,height=6000)

frame1 = Frame(root,width = 800,height=6000, bg = "teal")
frame1.place(x=0, y=0, width = 800,height=6000)

#### Controller ####
'''FRAME 1 - Login Page'''
username_label = Label(frame1, bg = "teal", fg = "white", text = "Username: ",font = ("Times New Roman",24) )
username_label.place(x=200, y = 200, width = 200, height = 35)

username_entry = create_entry_with_placeholder(frame1, "Enter your username", 400, 200, 200, 35)

password_label = Label(frame1, bg = "teal", fg = "white", text = "Password: ",font = ("Times New Roman",24) )
password_label.place(x=200, y = 250, width = 200, height = 35)

password_entry = create_entry_with_placeholder(frame1, "Enter your password", 400, 250, 200, 35, is_password = True)

login = Button(frame1, bg="white", fg="teal", text = "Login", font = ("Times New Roman",24), command = verify_login )
login.place(x=300,y=300,width = 200, height = 40)

register = Button(frame1, bg="white", fg="teal", text = "Register Account", font = ("Times New Roman",18), command = register_account )
register.place(x=300,y=350,width = 200, height = 40)

'''FRAME 2 - Welcome Page'''
logout = Button(frame2, bg="white", fg="teal", text = "Log Out", font = ("Times New Roman",18), command = return_login)
logout.place(x=300,y=450,width = 200, height = 40)

'''FRAME 3 - Registration Page'''
reg_username_label = Label(frame3, bg = "teal", fg = "white", text = "Username: ",font = ("Times New Roman",24) )
reg_username_label.place(x=200, y = 150, width = 200, height = 35)

reg_username_entry = create_entry_with_placeholder(frame3, "Enter your username", 400, 150, 200, 35)

reg_password_label1 = Label(frame3, bg = "teal", fg = "white", text = "Password: ",font = ("Times New Roman",24) )
reg_password_label1.place(x=200, y = 200, width = 200, height = 35)

reg_password_entry1 = create_entry_with_placeholder(frame3, "Enter your password", 400, 200, 200, 35, is_password = True)

reg_password_label2 = Label(frame3, bg = "teal", fg = "white", text = "Password: ",font = ("Times New Roman",24) )
reg_password_label2.place(x=200, y = 250, width = 200, height = 35)

reg_password_entry2 = create_entry_with_placeholder(frame3, "Reenter your password", 400, 250, 200, 35, is_password = True)

reg_account = Button(frame3, bg="white", fg="teal", text = "Register Account", font = ("Times New Roman",18), command = check_registration )
reg_account.place(x=300,y=300,width = 200, height = 40)

#### View ####
'''FRAME 1 - Login Page'''
title = Label(frame1, bg = "teal", fg = "white",text = "Login Page", font = ("Times New Roman",24))
title.place(x = 300,y=20,width = 200, height = 50)

error = Label(frame1, bg="teal", fg = "red", text = "", font = ("Times New Roman",20))
error.place(x=150,y=450,width = 500, height = 150)

'''FRAME 2 - Welcome Page'''
welcome = Label(frame2, bg="teal",fg = "white", textvariable = name, text=f"Welcome {name.get()}!", font = ("Times New Roman",20))
welcome.place(x=200,y=250,width =400, height = 50)

'''FRAME 3 - Registration Page'''
reg_title = Label(frame3, bg = "teal", fg = "white",text = "Register Account", font = ("Times New Roman",24))
reg_title.place(x = 200,y=20,width = 400, height = 50)

reg_error = Label(frame3, bg="teal", fg = "red", text = "", font = ("Times New Roman",20))
reg_error.place(x=100,y=450,width = 600, height = 150)

root.mainloop()