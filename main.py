import tkinter as tk
from tkinter import messagebox

# Dictionary to store user credentials
users = {"admin": "Admin@123"}

# Function to switch to a new frame after successful login
def open_greeting_frame(username):
    for widget in window.winfo_children():
        widget.destroy()

    greeting_label = tk.Label(window, text=f"Welcome, {username}!", font=("Arial", 24))
    greeting_label.pack(pady=20)

# Function to validate login credentials
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        open_greeting_frame(username)
    else:
        error_label.config(text="Error: Invalid username or password!")

# Function to open the registration window
def open_registration():
    registration_window = tk.Toplevel(window)
    registration_window.title("Register")

    tk.Label(registration_window, text="New Username:").grid(row=0, column=0)
    new_username_entry = tk.Entry(registration_window)
    new_username_entry.grid(row=0, column=1)

    tk.Label(registration_window, text="New Password:").grid(row=1, column=0)
    new_password_entry1 = tk.Entry(registration_window, show="*")
    new_password_entry1.grid(row=1, column=1)

    tk.Label(registration_window, text="Confirm Password:").grid(row=2, column=0)
    new_password_entry2 = tk.Entry(registration_window, show="*")
    new_password_entry2.grid(row=2, column=1)

    error_label = tk.Label(registration_window, text="")
    error_label.grid(row=3, column=1)

    # Function to handle registration
    def register():
        new_username = new_username_entry.get()
        new_password1 = new_password_entry1.get()
        new_password2 = new_password_entry2.get()

        # Check if username already exists
        if new_username in users:
            error_label.config(text="Error: Username already exists!")
        # Check if passwords match
        elif new_password1 != new_password2:
            error_label.config(text="Error: Passwords do not match!")
        # Check if password meets criteria
        elif (len(new_password1) < 10 or
              not any(char.isdigit() for char in new_password1) or
              not any(char in "!@#$%^&*()_+" for char in new_password1)):
            error_label.config(text="Error: Password must be 10 chars, 1 number, 1 special char!")
        else:
            # Add the new user to the dictionary
            users[new_username] = new_password1
            messagebox.showinfo("Success", "Registration successful!")
            registration_window.destroy()

    # Register button
    tk.Button(registration_window, text="Register", command=register).grid(row=4, column=1)

# Main window setup
window = tk.Tk()
window.title("Login Page")

# Username and Password fields
tk.Label(window, text="Username:").grid(row=0, column=0)
entry_username = tk.Entry(window)
entry_username.grid(row=0, column=1)

tk.Label(window, text="Password:").grid(row=1, column=0)
entry_password = tk.Entry(window, show="*")
entry_password.grid(row=1, column=1)

# Error label for invalid login
error_label = tk.Label(window, text="")
error_label.grid(row=2, column=1)

# Login button
login_button = tk.Button(window, text="Login", command=login)
login_button.grid(row=3, column=0)

# Register button
register_button = tk.Button(window, text="Register", command=open_registration)
register_button.grid(row=3, column=1)

window.mainloop()
