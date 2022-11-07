import customtkinter
import pygame
from tkinter import messagebox
import backend
import random
import pyperclip
import json
import socket

with open("data.json", "r") as file:
    try:
        hostname = json.load(file)["hostname"]
    except:
        hostname = None


window = customtkinter.CTk()
window.resizable(0, 0)
pygame.mixer.init()
pygame.mixer.music.load(r"1.mp3")
pygame.mixer.music.play(loops=0)
signup_screen_password_entry = customtkinter.CTkEntry(width=130)
username = None


def login_screen():
    window.geometry("350x180")
    window.title("Login Window")
    global username_login_label, password_login_label, username_login_entry, password_login_entry, signup_btn, \
        login_btn, login_screen_forget_password_btn
    username_login_label = customtkinter.CTkLabel(text="Username : ")
    password_login_label = customtkinter.CTkLabel(text="Password  : ")
    username_login_entry = customtkinter.CTkEntry()
    password_login_entry = customtkinter.CTkEntry(show="*")
    login_btn = customtkinter.CTkButton(text="Login", width=100,
                                        command=lambda: [credential_check()])
    signup_btn = customtkinter.CTkButton(text="Signup", width=100, command=lambda: [login_signin()])
    login_screen_forget_password_btn = customtkinter.CTkButton(text="Forget Password",
                                                               command=lambda: [login_forget_password(),
                                                                                login_screen_forget_password_btn.after(
                                                                                    3000,
                                                                                    login_screen_forget_password_btn.destroy)])
    username_login_label.place(x=20, y=30)
    password_login_label.place(x=20, y=65)
    username_login_entry.place(x=150, y=30)
    password_login_entry.place(x=150, y=65)
    login_btn.place(x=70, y=105)
    signup_btn.place(x=172, y=105)
    login_screen_forget_password_btn.place(x=100, y=135)
    window.mainloop()


def signup_screen():
    window.title("Signup")
    window.geometry("400x220")
    window.resizable(0, 0)
    global username_signup_label, password_signup_label, signup_screen_username_entry, signup_screen_password_entry, \
        generate_signup_btn, back_btn, signup1_btn, email_signup_screen_label, email_signup_screen_entry, \
        otp_signup_screen_label, otp_signup_screen_entry, otp_signup_screen_btn
    username_signup_label = customtkinter.CTkLabel(text="Username: ")
    password_signup_label = customtkinter.CTkLabel(text="Password: ")
    signup_screen_username_entry = customtkinter.CTkEntry(width=200)
    signup_screen_password_entry = customtkinter.CTkEntry(width=130)
    generate_signup_btn = customtkinter.CTkButton(text="Generate", width=30,
                                                  command=lambda: [password_generator(signup_screen_password_entry)])
    email_signup_screen_label = customtkinter.CTkLabel(text="Email: ")
    email_signup_screen_entry = customtkinter.CTkEntry(width=200)
    otp_signup_screen_label = customtkinter.CTkLabel(text="Enter OTP: ")
    otp_signup_screen_entry = customtkinter.CTkEntry(width=130)
    otp_signup_screen_btn = customtkinter.CTkButton(text="Get OTP", width=30, command=lambda: [
        backend.email_message(email_signup_screen_entry.get(), signup_screen_username_entry.get())])
    back_btn = customtkinter.CTkButton(text="Back", width=80, command=signin_login)
    signup1_btn = customtkinter.CTkButton(text="Signup", width=80, command=lambda: [
        backend.check_credentials_signup(signup_screen_username_entry, signup_screen_password_entry,
                                         otp_signup_screen_entry, email_signup_screen_entry)])
    username_signup_label.place(x=20, y=30)
    password_signup_label.place(x=20, y=65)
    signup_screen_username_entry.place(x=130, y=30)
    signup_screen_password_entry.place(x=130, y=65)
    generate_signup_btn.place(x=265, y=65)
    email_signup_screen_label.place(x=30, y=100)
    email_signup_screen_entry.place(x=130, y=100)
    otp_signup_screen_label.place(x=20, y=135)
    otp_signup_screen_entry.place(x=130, y=135)
    otp_signup_screen_btn.place(x=265, y=135)
    back_btn.place(x=125, y=170)
    signup1_btn.place(x=215, y=170)
    window.mainloop()


def action_screen():
    global search_action_btn, add_action_btn, edit_action_btn, remove_action_btn, export_action_btn
    window.geometry("300x120")
    window.title("Action")
    search_action_btn = customtkinter.CTkButton(text="Search", width=105, command=action_search)
    add_action_btn = customtkinter.CTkButton(text="Add", width=105, command=action_add)
    edit_action_btn = customtkinter.CTkButton(text="Edit", width=140, command=action_edit)
    remove_action_btn = customtkinter.CTkButton(text="Remove", width=105, command=action_remove)
    export_action_btn = customtkinter.CTkButton(text="Export", width=105,
                                                command=lambda: [backend.export_password(username)])
    search_action_btn.place(x=40, y=10)
    add_action_btn.place(x=145, y=10)
    edit_action_btn.place(x=75, y=42)
    remove_action_btn.place(x=40, y=74)
    export_action_btn.place(x=145, y=74)
    window.mainloop()


def search_screen():
    window.title("Search Screen")
    window.geometry("400x110")
    window.resizable(0, 0)
    global username_search_label, search_screen_username_entry, search_btn, back_search_btn
    username_search_label = customtkinter.CTkLabel(text="Username/Email: ")
    search_screen_username_entry = customtkinter.CTkEntry(width=170)
    search_btn = customtkinter.CTkButton(text="search", width=80,
                                         command=lambda: [search_search_ext(search_screen_username_entry)])
    back_search_btn = customtkinter.CTkButton(text="Back", width=80, command=search_action)
    username_search_label.place(x=30, y=25)
    search_screen_username_entry.place(x=160, y=25)
    search_btn.place(x=120, y=60)
    back_search_btn.place(x=205, y=60)
    window.mainloop()


def add_screen():
    window.title("Add Screen")
    window.geometry("400x200")
    global website_add_label, website_add_entry, username_add_label, password_add_label, username_add_entry, \
        password_add_entry, generate_add_btn, add_btn, back_add_btn
    website_add_label = customtkinter.CTkLabel(text="Website: ")
    username_add_label = customtkinter.CTkLabel(text="Username: ")
    password_add_label = customtkinter.CTkLabel(text="Password: ")
    website_add_entry = customtkinter.CTkEntry(width=200)
    username_add_entry = customtkinter.CTkEntry(width=170)
    password_add_entry = customtkinter.CTkEntry(width=110)
    generate_add_btn = customtkinter.CTkButton(text="Generate", width=50,
                                               command=lambda: [password_generator(password_add_entry)])
    add_btn = customtkinter.CTkButton(text="Add", width=80, command=lambda: [
        backend.add_password(username, website_add_entry, username_add_entry, password_add_entry)])
    back_add_btn = customtkinter.CTkButton(text="Back", width=80, command=add_action)
    website_add_label.place(x=20, y=30)
    website_add_entry.place(x=130, y=30)
    username_add_label.place(x=20, y=65)
    password_add_label.place(x=20, y=100)
    username_add_entry.place(x=130, y=65)
    password_add_entry.place(x=130, y=100)
    generate_add_btn.place(x=245, y=100)
    add_btn.place(x=95, y=140)
    back_add_btn.place(x=185, y=140)
    window.mainloop()


def remove_screen():
    window.title("Remove Screen")
    window.geometry("400x120")
    window.resizable(0, 0)
    global username_remove_label, remove_screen_username_entry, add_remove_btn, back_remove_btn
    username_remove_label = customtkinter.CTkLabel(text="Website: ")
    remove_screen_username_entry = customtkinter.CTkEntry(width=170)
    add_remove_btn = customtkinter.CTkButton(text="Remove", width=80,
                                             command=lambda: [conformation_screen(remove_screen_username_entry.get())])
    back_remove_btn = customtkinter.CTkButton(text="Back", width=80, command=remove_action)
    username_remove_label.place(x=20, y=30)
    remove_screen_username_entry.place(x=130, y=30)
    add_remove_btn.place(x=95, y=70)
    back_remove_btn.place(x=200, y=70)
    window.mainloop()


def edit_screen():
    window.title("Edit Screen")
    window.geometry("400x180")
    window.resizable(0, 0)
    global website_edit_label, website_edit_entry, username_edit_label, password_edit_label, edit_screen_username_entry, edit_screen_password_entry, \
        edit_edit_btn, back_edit_btn
    website_edit_label = customtkinter.CTkLabel(text="Website: ")
    website_edit_entry = customtkinter.CTkEntry(width=170)
    username_edit_label = customtkinter.CTkLabel(text="Username: ")
    password_edit_label = customtkinter.CTkLabel(text="Password: ")
    edit_screen_username_entry = customtkinter.CTkEntry(width=170)
    edit_screen_password_entry = customtkinter.CTkEntry(width=110)
    edit_edit_btn = customtkinter.CTkButton(text="Edit", width=80, command=lambda: [
        backend.edit_password(username, edit_screen_username_entry, website_edit_entry, edit_screen_password_entry)])
    back_edit_btn = customtkinter.CTkButton(text="Back", width=80, command=edit_action)
    website_edit_label.place(x=25, y=15)
    website_edit_entry.place(x=130, y=15)
    username_edit_label.place(x=20, y=50)
    password_edit_label.place(x=20, y=85)
    edit_screen_username_entry.place(x=130, y=50)
    edit_screen_password_entry.place(x=130, y=85)
    edit_edit_btn.place(x=95, y=120)
    back_edit_btn.place(x=200, y=120)
    window.mainloop()


def conformation_screen(username1):
    global sure_label, yes_conformation_btn, no_conformation_btn
    with open("data.json", "r") as file2:
        content1 = json.load(file2)
    if username1 in content1[username]["websites"]:
        username_remove_label.destroy()
        remove_screen_username_entry.destroy()
        add_remove_btn.destroy()
        back_remove_btn.destroy()
        window.geometry("360x120")
        window.title("Conformation")
        sure_label = customtkinter.CTkLabel(text="Are you sure?...")
        yes_conformation_btn = customtkinter.CTkButton(text="Yes", width=80, command=lambda: [print("hello"), backend.remove_website(username, username1)])
        no_conformation_btn = customtkinter.CTkButton(text="No", width=80, command=conformation_remove)
        sure_label.place(x=115, y=20)
        yes_conformation_btn.place(x=75, y=60)
        no_conformation_btn.place(x=205, y=60)
        window.mainloop()
    else:
        messagebox.showwarning("Warning", "         Username Not found         ")


def forget_password_screen():
    window.geometry("350x210")
    window.title("Forget Password")
    global username_forget_password_label, otp_forget_password_label, otp_forget_password_btn, \
        forget_password_username_entry, forget_password_otp_entry, forget_password_password_label, \
        forget_password_re_password_label, forget_password_password_entry, forget_password_re_password_entry, \
        forget_password_back_btn, forget_password_change_btn, generate_forget_password_btn
    username_forget_password_label = customtkinter.CTkLabel(text="Username : ")
    otp_forget_password_label = customtkinter.CTkLabel(text="OTP : ")
    otp_forget_password_btn = customtkinter.CTkButton(text="OTP", width=90, command=lambda: [
        backend.email_msg_forget_password(forget_password_username_entry.get())])
    forget_password_username_entry = customtkinter.CTkEntry(width=200)
    forget_password_otp_entry = customtkinter.CTkEntry(width=105, show="*")
    forget_password_password_label = customtkinter.CTkLabel(text="Password : ")
    forget_password_re_password_label = customtkinter.CTkLabel(text="Re Password : ")
    forget_password_password_entry = customtkinter.CTkEntry(width=105)
    forget_password_re_password_entry = customtkinter.CTkEntry(width=200)
    generate_forget_password_btn = customtkinter.CTkButton(text="Generate", width=90, command=lambda: [
        password_generator(forget_password_password_entry, forget_password_re_password_entry)])
    forget_password_back_btn = customtkinter.CTkButton(text="Back", width=100, command=forget_password_login)
    forget_password_change_btn = customtkinter.CTkButton(text="Change", width=100, command=lambda: [
        backend.change_p
        assword(forget_password_username_entry, forget_password_otp_entry,
                                forget_password_password_entry, forget_password_re_password_entry)])
    forget_password_username_entry.place(x=110, y=30)
    forget_password_otp_entry.place(x=110, y=65)
    username_forget_password_label.place(x=0, y=30)
    otp_forget_password_label.place(x=15, y=65)
    otp_forget_password_btn.place(x=221, y=65)
    forget_password_password_label.place(x=0, y=100)
    forget_password_re_password_label.place(x=-10, y=135)
    generate_forget_password_btn.place(x=221, y=100)
    forget_password_password_entry.place(x=110, y=100)
    forget_password_re_password_entry.place(x=110, y=135)
    forget_password_back_btn.place(x=70, y=170)
    forget_password_change_btn.place(x=190, y=170)
    window.mainloop()


def search_extend(name):
    global search_screen_password_label, search_screen_username_label, username_copy_btn, password_copy_btn
    with open("data.json", "r") as file2:
        content1 = json.load(file2)
        a = content1[username]["websites"][name.get()]
    search_screen_password_label = customtkinter.CTkLabel(text=f"Password:  {backend.rsa_decrypt(a[2], a[3])}")
    search_screen_username_label = customtkinter.CTkLabel(text=f"Username:  {backend.rsa_decrypt(a[0], a[1])}")
    username_copy_btn = customtkinter.CTkButton(text="copy",
                                                command=lambda: [pyperclip.copy(backend.rsa_decrypt(a[0], a[1]))],
                                                width=50)
    password_copy_btn = customtkinter.CTkButton(text="copy",
                                                command=lambda: [pyperclip.copy(backend.rsa_decrypt(a[2], a[3]))],
                                                width=50)
    search_btn.place(x=120, y=135)
    back_search_btn.place(x=205, y=135)
    search_screen_username_label.place(x=80, y=60)
    search_screen_password_label.place(x=80, y=95)
    username_copy_btn.place(x=280, y=60)
    password_copy_btn.place(x=280, y=95)


def login_signin():
    login_screen_forget_password_btn.after(3000, login_screen_forget_password_btn.destroy)
    username_login_label.destroy()
    password_login_label.destroy()
    username_login_entry.destroy()
    password_login_entry.destroy()
    login_btn.destroy()
    signup_btn.destroy()
    signup_screen()


def signin_login():
    username_signup_label.destroy()
    password_signup_label.destroy()
    signup_screen_username_entry.destroy()
    signup_screen_password_entry.destroy()
    generate_signup_btn.destroy()
    email_signup_screen_label.destroy()
    email_signup_screen_entry.destroy()
    otp_signup_screen_label.destroy()
    otp_signup_screen_entry.destroy()
    otp_signup_screen_btn.destroy()
    back_btn.destroy()
    signup1_btn.destroy()
    login_screen()


def login_action():
    global username
    login_screen_forget_password_btn.after(2, login_screen_forget_password_btn.destroy)
    username = username_login_entry.get()
    username_login_label.destroy()
    password_login_label.destroy()
    username_login_entry.destroy()
    password_login_entry.destroy()
    login_btn.destroy()
    signup_btn.destroy()
    action_screen()


def login_forget_password():
    username_login_label.destroy()
    login_screen_forget_password_btn.destroy()
    password_login_label.destroy()
    username_login_entry.destroy()
    password_login_entry.destroy()
    login_btn.destroy()
    signup_btn.destroy()
    forget_password_screen()


def forget_password_login():
    username_forget_password_label.destroy()
    otp_forget_password_label.destroy()
    otp_forget_password_btn.destroy()
    forget_password_username_entry.destroy()
    forget_password_otp_entry.destroy()
    forget_password_password_label.destroy()
    forget_password_re_password_label.destroy()
    forget_password_password_entry.destroy()
    forget_password_re_password_entry.destroy()
    forget_password_back_btn.destroy()
    forget_password_change_btn.destroy()
    generate_forget_password_btn.destroy()
    login_screen()


def action_search():
    search_action_btn.destroy()
    add_action_btn.destroy()
    edit_action_btn.destroy()
    remove_action_btn.destroy()
    export_action_btn.destroy()
    search_screen()


def search_action():
    try:
        username_search_label.destroy()
        search_screen_username_entry.destroy()
        search_btn.destroy()
        back_search_btn.destroy()
        search_screen_password_label.destroy()
        search_screen_username_label.destroy()
        username_copy_btn.destroy()
        password_copy_btn.destroy()
        action_screen()
    except:
        username_search_label.destroy()
        search_screen_username_entry.destroy()
        search_btn.destroy()
        back_search_btn.destroy()
        action_screen()


def action_add():
    search_action_btn.destroy()
    add_action_btn.destroy()
    edit_action_btn.destroy()
    remove_action_btn.destroy()
    export_action_btn.destroy()
    add_screen()


def add_action():
    website_add_label.destroy()
    website_add_entry.destroy()
    username_add_label.destroy()
    password_add_label.destroy()
    username_add_entry.destroy()
    password_add_entry.destroy()
    generate_add_btn.destroy()
    add_btn.destroy()
    back_add_btn.destroy()
    action_screen()


def action_remove():
    search_action_btn.destroy()
    add_action_btn.destroy()
    edit_action_btn.destroy()
    remove_action_btn.destroy()
    export_action_btn.destroy()
    remove_screen()


def remove_action():
    username_remove_label.destroy()
    remove_screen_username_entry.destroy()
    add_remove_btn.destroy()
    back_remove_btn.destroy()
    action_screen()


def action_edit():
    search_action_btn.destroy()
    add_action_btn.destroy()
    edit_action_btn.destroy()
    remove_action_btn.destroy()
    export_action_btn.destroy()
    edit_screen()


def edit_action():
    website_edit_label.destroy()
    website_edit_entry.destroy()
    username_edit_label.destroy()
    password_edit_label.destroy()
    edit_screen_username_entry.destroy()
    edit_screen_password_entry.destroy()
    edit_edit_btn.destroy()
    back_edit_btn.destroy()
    action_screen()


def conformation_remove():
    sure_label.destroy()
    yes_conformation_btn.destroy()
    no_conformation_btn.destroy()
    remove_screen()


def search_search_ext(name):
    with open("data.json", "r") as fp:
        con = json.load(fp)
        a1 = con[username]["websites"]
    if len(name.get()) >= 4 and name.get() in a1:
        window.geometry("400x200")
        search_extend(name)
    else:
        messagebox.showwarning("Warning", "         Username does not exist..       ")


def password_generator(element, *args):
    element.delete(0, len(element.get()))
    for x in args:
        x.delete(0, len(element.get()))
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    password_list1 = [random.choice(letters) for _ in range(nr_letters)]
    password_list2 = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_list1 + password_list2
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    element.insert(0, password)
    for x in args:
        x.insert(0, password)
    pyperclip.copy(password)


def credential_check():
    if backend.check_credentials_login(username_login_entry.get(), password_login_entry.get()):
        login_action()


try:
    if socket.gethostname() == hostname:
        login_screen()
    else:
        with open("data.json", "w") as file1:
            content = {"hostname": socket.gethostname()}
            json.dump(content, file1)
    login_screen()
except:
    pass
