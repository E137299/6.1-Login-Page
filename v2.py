from tkinter import *

root = Tk()
root.title("Login Page")
root.geometry("800x600+20+20")


#### Model ####
def on_entry_click(event):
    """Function to remove placeholder text when the entry gets clicked."""
    if username_entry.get() == "Enter your username":
        username_entry.delete(0, END)  # Remove all text in the entry
        username_entry.config(fg='black')  # Change the text color back to normal

def on_focusout(even):
    """Function to restore placeholder text if entry is left empty."""
    if username_entry.get() == "":
        username_entry.insert(0, "Enter your username")  # Insert placeholder text
        username_entry.config(fg='grey') 

def verify_login():
    user = username_entry.get()
    password = password_entry.get()

    if user in logins and logins[user]==password:
        frame2.tkraise()
    else:
        error.config(text = "Either the username or password is incorrect.\nPlease reenter your credentials.")

logins ={"DavidYin":"123Password!"}

frame2 = Frame(root,width = 800,height=6000, bg = "teal")
frame2.place(x=0, y=0, width = 800,height=6000)

frame1 = Frame(root,width = 800,height=6000, bg = "teal")
frame1.place(x=0, y=0, width = 800,height=6000)

#### Controller ####
username_label = Label(frame1, bg = "teal", fg = "white", text = "Username: ",font = ("Times New Roman",24) )
username_label.place(x=200, y = 100, width = 200, height = 35)

username_entry = Entry(frame1, fg ="gray")
username_entry.insert(0, "Enter your username")
username_entry.bind("<FocusIn>", on_entry_click)
username_entry.bind("<FocusOut>", on_focusout)
username_entry.place(x=400, y = 100, width = 200, height = 35)


password_label = Label(frame1, bg = "teal", fg = "white", text = "Password: ",font = ("Times New Roman",24) )
password_label.place(x=200, y = 150, width = 200, height = 35)

password_entry = Entry(frame1, show = "*")
password_entry.place(x=400, y = 150, width = 200, height = 35)

login = Button(frame1, bg="orange", fg="black", text = "Login", font = ("Times New Roman",24), command = verify_login )
login.place(x=300,y=200,width = 200, height = 40)

register = Button(frame1, bg="orange", fg="black", text = "Register Account", font = ("Times New Roman",20) )
register.place(x=300,y=250,width = 200, height = 40)

#### View ####
title = Label(frame1, bg = "teal", fg = "black",text = "Login Page", font = ("Times New Roman",20))
title.place(x = 300,y=20,width = 200, height = 50)

welcome = Label(frame2, bg="teal",fg = "purple", text="Welcome!", font = ("Times New Roman",20))
welcome.place(x=350,y=250,width =100, height = 50)

error = Label(frame1, bg="teal", fg = "red", text = "", font = ("Times New Roman",20))
error.place(x=150,y=300,width = 500, height = 150)




root.mainloop()