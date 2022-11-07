from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import ctypes
import sms
import datetime
import json
import time

ctypes.windll.shcore.SetProcessDpiAwareness(1)
login_window, email_otp_entry = None, None
ForgetPasswordWindow, change_password_window = None, None
password_entry, EmailId_lable = None, None
new_password_entry, confirm_password_entry = None, None
login_password, new_email_entry = None, None
MainWindow = None
with open("data.json", "r") as file:
    content = json.load(file)
    login_password = content["password"]
    EmailID = content["Email"]
    Mob_number = content["Mob_number"]
    path = content["path"]


def login_page():
    global password_entry, login_window
    login_window = Tk()
    login_window.title("App Login")
    login_window.config(width=400, height=200)
    password_label = Label(login_window, text="Password: ")
    password_entry = Entry(login_window, show="*")
    password_button = Button(login_window, text="Submit", command=validate_password)
    forget_password_button = Button(login_window, text="Forget Password", command=forget_password_window)
    password_label.place(x=50, y=60)
    password_entry.place(x=140, y=60)
    password_button.place(x=75, y=120)
    forget_password_button.place(x=180, y=120)
    login_window.mainloop()


def forget_password_window():
    login_window.destroy()
    global ForgetPasswordWindow
    ForgetPasswordWindow = Tk()
    ForgetPasswordWindow.title("Forget Password")
    ForgetPasswordWindow.config(width=400, height=200)
    txt_label = Label(text="Get OTP through:")
    sms_button = Button(text="Message", command=sms_win)
    email_button = Button(text="Email", command=email_win)
    all_commands = lambda: [ForgetPasswordWindow.destroy(), login_page()]
    back_button = Button(text="<--", command=all_commands)
    txt_label.place(x=90, y=20)
    back_button.place(x=10, y=10)
    sms_button.place(x=120, y=60)
    email_button.place(x=240, y=60)

    ForgetPasswordWindow.mainloop()


def change_password():
    global ChangePasswordWindow, new_password_entry, confirm_password_entry
    ChangePasswordWindow = Tk()
    ChangePasswordWindow.title("Change Password")
    ChangePasswordWindow.config(width=600, height=200)
    new_password_label = Label(text="Enter new password: ")
    confirm_password_label = Label(text="Confirm new Password: ")
    new_password_entry = Entry(ChangePasswordWindow)
    confirm_password_entry = Entry(ChangePasswordWindow)
    confirm_password_button = Button(text="Change Password", command=change_new_password)
    new_password_label.place(x=50, y=50)
    confirm_password_label.place(x=35, y=90)
    new_password_entry.place(x=240, y=50)
    confirm_password_entry.place(x=240, y=90)
    confirm_password_button.place(x=250, y=140)


def validate_password():
    if password_entry.get() == login_password:
        login_window.destroy()
        messagebox.showinfo("Access granted", "             Access Granted                   ")
        main_window()

    else:
        messagebox.showwarning("Access denied", "Access denied due to Invalid password!")


def main_window():
    global MainWindow
    MainWindow = Tk()
    MainWindow.title("Main Window")
    MainWindow.config(width=700, height=600)
    # EmailId
    global EmailId_lable
    EmailId_lable = Label(MainWindow, text=f"Current Email ID: {EmailID}")
    EmailId_button = Button(MainWindow, text="Change", command=change_email)
    mob_number_label = Label(MainWindow, text=f"Current Mobile number: {Mob_number}")
    mob_number_button = Button(MainWindow, text="Change", command=change_mob_number)
    add_dir_label = Label(MainWindow, text="Add Directory")
    add_dir_button = Button(MainWindow, text="  +  ", command=add_dir)
    EmailId_lable.place(x=100, y=90)
    EmailId_button.place(x=500, y=85)
    mob_number_label.place(x=100, y=140)
    mob_number_button.place(x=500, y=135)
    add_dir_label.place(x=250, y=190)
    add_dir_button.place(x=400, y=185)


def add_dir():
    file_path = fd.askdirectory()
    print(content["path"])
    path.append(file_path)
    with open("data.json", "w") as file2:
        json.dump(content, file2, indent=4)


def change_email():
    def changeemail():
        content["Email"] = new_email_entry.get()
        with open("data.json", "w") as file1:
            json.dump(content, file1, indent=4)
        change_email_window.destroy()
        messagebox.showinfo(title="Information", message="Please restart the app to see your updated email.")
        MainWindow.destroy()

    change_email_window = Tk()
    change_email_window.config(width=600, height=200)
    new_email_label = Label(change_email_window, text="New Email: ")
    global EmailId_lable, MainWindow, new_email_entry
    new_email_entry = Entry(change_email_window, width=30)
    new_email_submit_button = Button(change_email_window, text="Change", command=changeemail)
    new_email_label.place(x=90, y=20)
    new_email_entry.place(x=230, y=20)
    new_email_submit_button.place(x=300, y=100)
    print(new_email_entry.get())


def change_mob_number():
    def changemobnumber():
        content["Mob_number"] = new_email_entry.get()
        with open("data.json", "w") as file1:
            json.dump(content, file1, indent=4)
        change_email_window.destroy()
        messagebox.showinfo(title="Information", message="Please restart the app to see your updated mobile number.")
        MainWindow.destroy()
    change_email_window = Tk()
    change_email_window.config(width=600, height=200)
    new_email_label = Label(change_email_window, text="New number: ")
    global new_email_entry
    new_email_entry = Entry(change_email_window, width=30)
    new_email_submit_button = Button(change_email_window, text="Change", command=changemobnumber)
    new_email_label.place(x=90, y=20)
    new_email_entry.place(x=230, y=20)
    new_email_submit_button.place(x=300, y=100)


def sms_win():
    global email_otp_entry
    submit_button = Button(text="Submit", command=validate_otp)
    submit_button.place(x=175, y=150)
    email_otp_entry = Entry(ForgetPasswordWindow, width=10, show="*")
    email_otp_entry.place(x=160, y=112)
    # sms.sms_message()


def email_win():
    global email_otp_entry
    email_otp_entry = Entry(ForgetPasswordWindow, width=10, show="*")
    email_otp_entry.place(x=160, y=112)
    submit_button = Button(text="Submit", command=validate_otp)
    submit_button.place(x=175, y=150)
    sms.email_message()


def validate_otp():
    global email_otp_entry
    if (datetime.datetime.now().minute - sms.now1 <= 5) and (sms.Otp == int(email_otp_entry.get())):
        ForgetPasswordWindow.destroy()
        change_password()
    else:
        messagebox.showwarning(title="Warning", message="Invalid  OTP")


def change_new_password():
    global login_password
    if new_password_entry.get() == confirm_password_entry.get():
        if login_password != new_password_entry.get():
            login_password = new_password_entry.get()
            content["password"] = new_password_entry.get()
            with open("data.json", "w") as file1:
                json.dump(content, file1, indent=4)
            ChangePasswordWindow.destroy()
            login_page()
        else:
            messagebox.showwarning("warning", "New password cannot be same as old password.")
    else:
        messagebox.showwarning("warning", "password mismatch")
