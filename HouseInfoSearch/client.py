# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/1 16:17
@Auth ： XM
@File ：client.py
@IDE ：PyCharm
"""
import os
import time
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import requests
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'


class MyAPP:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.root = tk.Tk()
        self.root.title('房屋交易信息搜索引擎')
        self.root.geometry("750x420")
        self.myentry_text = ''

        self.mainUi()
        self.root.mainloop()

    def mainUi(self):
        ttk.Label(self.root, text='请输入城市名:').grid(padx=10, pady=5, row=0, column=0)
        self.search_lb = ttk.Entry(self.root)
        self.search_lb.grid(padx=5, pady=5, row=0, column=1)
        self.search_lb.configure(font=("仿宋", 13))
        self.search_lb.configure(validate="focusin")

        self.show_btn = ttk.Button(self.root, text='展示', command=self.show_hist).place(x=630, y=5)

        self.search_btn = ttk.Button(self.root, text="查找", command=self.search).grid(padx=10, pady=5, row=0, column=2)

        self._set_page()

    def _set_page(self):
        """搜索并显示在列表框内"""
        self.listBox = ttk.Treeview(self.root, height=15,
                                    columns=['城市', '位置', '户型', '面积', '朝向', '装修', '楼层', '结构', '价格'], show='headings')
        self.VScroll = ttk.Scrollbar(self.root, orient='vertical', command=self.listBox.yview)
        self.listBox.configure(yscrollcommand=self.VScroll.set)
        self.VScroll.grid(row=1, column=3)

        for col in ['城市', '位置', '户型', '面积', '朝向', '装修', '楼层', '结构', '价格']:
            self.listBox.column(col, width=80, anchor='center')
            self.listBox.heading(col, text=col)
        self.listBox.grid(padx=15, pady=10, row=1, column=0, columnspan=4)

    def send_request(self, url, data=None):
        t1 = time.time()
        print('send')
        if data is None:
            r = requests.get(url)
        else:
            r = requests.post(url, json=data)
        if r.status_code == 200:
            return r.json()
        else:
            return None

    def search(self):

        info = self.search_lb.get()
        data = {'city_name':info.encode('utf-8')}
        res = self.send_request('http://' + self.host + ':' + str(self.port) + '/search' , data)
        if res is None:
            tkinter.messagebox.showinfo('提示', '连接失败，导致查询失败')
        else:
            code = res['code']
            message = res['msg']
            if code == -1 or code == 0 or code == 1:
                tkinter.messagebox.showinfo('提示', message)
            else:
                city = code
                self.show(city)
                self.root.mainloop()


    # 显示
    def show(self, city):
        city_info = self.send_request('http://' + self.host + ':' + self.port + '/read', data={'city_name':city})
        print(city_info)
        if city_info is None or city_info['code'] < 0:
            tkinter.messagebox.showinfo('提示', '数据库中没有{}的房屋信息!'.format(city))
        elif city_info['code'] == 1:
            tkinter.messagebox.showinfo('提示', city_info['msg'])
        else:
            self.listBox.delete(*self.listBox.get_children())  # 清空原先表格
            city_info = city_info['msg']
            for i, row in enumerate(city_info):
                # print(row)
                self.listBox.insert("", "end", values=tuple(row))

    def show_hist(self):
        city_info = self.send_request('http://' + self.host + ':' + self.port + '/show')
        if city_info is None or city_info['code'] < 0:
            tkinter.messagebox.showinfo('提示', '数据库中没有相关的房屋信息!')
        elif city_info['code'] == 1:
            tkinter.messagebox.showinfo('提示', city_info['msg'])
        else:
            city_info = city_info['msg']
            plt.bar(range(len(city_info)), city_info.values(), align='center')
            plt.xticks(range(len((city_info))), city_info.keys(), rotation=90)
            plt.xlabel('城市')
            plt.ylabel('数量')
            plt.tight_layout()
            plt.savefig('hist.png')
            # plt.show()
            win1 = tkinter.Toplevel()
            win1.title('不同城市房屋信息数量')
            img = tkinter.PhotoImage(file='./hist.png')
            label = tkinter.Label(win1, image=img).pack()
            win1.mainloop()

            


if __name__ == "__main__":
    MyAPP('127.0.0.1', '8080')
