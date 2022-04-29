import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# class AboutPage(ttk.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#         ttk.Label(self, text='关于软件：本软件由ttkbootstrap制作').pack()
#         ttk.Label(self, text='关于作者：杨超').pack()
#         ttk.Label(self, text='版权所有：杨超').pack()

class QuMenu(ttk.Menu):
    def __init__(self, root):
        super().__init__(root)
        m1 = ttk.Menu.add_cascade(self, label="单号查询")
        m1 = ttk.Menu.add_cascade(self, label="时间查询")
        self.config(menu=m1)


class ImigMenu(ttk.Menu):
    def __init__(self, root):
        super().__init__(root)
        m1 = ttk.Menu.add_cascade(self, label="热力图")
        m1 = ttk.Menu.add_cascade(self, label="销售曲线")
        self.config(menu=m1)


class PrMenu(ttk.Menu):
    def __init__(self, root):
        super(PrMenu, self).__init__(root)

        m1 = ttk.Menu.add_cascade(self, label="订单状态")
        self.config(menu=m1)

class OrderMenu(ttk.Menu):
    def __init__(self, root):
        super().__init__(root)
        m1 = ttk.Menu.add_cascade(self, label="新接订单")
        m1 = ttk.Menu.add_cascade(self, label="已下订单")
        m1 = ttk.Menu.add_cascade(self, label="全部订单")
        m1 = ttk.Menu.add_cascade(self, label="订单查询")
        self.config(menu=m1)

class SailMenu(ttk.Menu):
    def __init__(self, root):
        super().__init__(root)
        m1 = ttk.Menu.add_cascade(self, label="已完成订单")
        m1 = ttk.Menu.add_cascade(self, label="未完成订单")
        m1 = ttk.Menu.add_cascade(self, label="售后跟踪")
        self.config(menu=m1)

class StrMenu(ttk.Menu):
    def __init__(self, root):
        super().__init__(root)
        m1 = ttk.Menu.add_cascade(self, label="入库单")
        m1 = ttk.Menu.add_cascade(self, label="出库单")
        m1 = ttk.Menu.add_cascade(self, label="入库明细")
        m1 = ttk.Menu.add_cascade(self, label="出库明细")
        m1 = ttk.Menu.add_cascade(self, label="库存汇总")
        m1 = ttk.Menu.add_cascade(self, label="商品明细")
        self.config(menu=m1)

