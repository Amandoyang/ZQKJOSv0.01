import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from view import PrMenu, OrderMenu, SailMenu, StrMenu, QuMenu, ImigMenu


class MainPage:

    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.geometry('700x400+750+300')
        self.root.title('智趣空间生产管理系统V 0.01')

        self.odermenu = OrderMenu(self.root)
        self.sailmenu = SailMenu(self.root)
        self.prmenu = PrMenu(self.root)
        self.strmn = StrMenu(self.root)
        self.qumn = QuMenu(self.root)
        self.imgmn = ImigMenu(self.root)
        menu_bar = ttk.Menu(self.root)

        menu_bar.add_cascade(label='订单管理', menu=self.odermenu, activebackground='blue', font='微软雅黑''20')
        menu_bar.add_cascade(label='生产管理', menu=self.prmenu, activebackground='blue', font='微软雅黑''20')
        menu_bar.add_cascade(label='售后管理', menu=self.sailmenu, activebackground='blue', font='微软雅黑''20')
        menu_bar.add_cascade(label='库存管理', menu=self.strmn, activebackground='blue', font='微软雅黑''20')
        menu_bar.add_cascade(label='查询', menu=self.qumn, activebackground='blue', font='微软雅黑''20')
        menu_bar.add_cascade(label='图表', menu=self.imgmn, activebackground='blue', font='微软雅黑''20')

        self.root.config(menu=menu_bar)


if __name__ == '__main__':
    root = ttk.Window(themename='superhero')
    MainPage(master=root)
    root.mainloop()
