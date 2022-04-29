import tkinter as tk
from tkinter import messagebox
from db import db
from mainpage import MainPage
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class LoginPage:

    def __init__(self, master):

        self.root = master
        self.root.geometry('300x200+750+300')
        self.root.title('智趣空间生产管理系统v0.01')

        self.page = ttk.Frame(self.root)
        self.page.pack()
        self.username = ttk.StringVar()
        self.password = ttk.StringVar()

        ttk.Label(self.page).grid(row=0, column=0)

        ttk.Label(self.page, text='帐户： ').grid(row=1, column=1)
        ttk.Entry(self.page, textvariable=self.username).grid(row=1, column=2)

        ttk.Label(self.page, text='密码： ').grid(row=2, column=1, pady=20)
        ttk.Entry(self.page, textvariable=self.password).grid(row=2, column=2)
        ttk.Button(self.page, text='登陆',bootstyle=INFO, command=self.login).grid(row=3, column=1, pady=12)
        ttk.Button(self.page, text='注册',bootstyle=INFO, command=self.register).grid(row=3, column=2)

    def register(self):
        name = self.username.get()
        pwd = self.password.get()
        print('注册用户信息：', name, pwd)

    def login(self):
        name = self.username.get()
        pwd = self.password.get()
        flag, message = db.check_login(name, pwd)


        if flag:
            self.page.destroy()
            MainPage(self.root)

        else:
            messagebox.showwarning(title='错误', message=message)




if __name__ == '__main__':
    root = ttk.Window(themename='solar')

    LoginPage(master=root)
    root.mainloop()
