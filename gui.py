# % GUI.py
# % UI界面

import tkinter as tk
from tkinter import *
from tsp import *

window = tk.Tk()
window.title('旅游规划路径')
window.geometry('1000x800')

l1 = tk.Label(window, text='请先点击起点，再点击其他要经过的景点', height=2).pack()

# 框架
frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')
frm_l_l = tk.Frame(frm_l)
frm_l_r = tk.Frame(frm_l)
frm_l_l.pack(side='left')
frm_l_r.pack(side='right')
frm_r_l = tk.Frame(frm_r)
frm_r_r = tk.Frame(frm_r)
frm_r_l.pack(side='left')
frm_r_r.pack(side='right')
frm_0 = tk.Frame(frm_l_l)
frm_1 = tk.Frame(frm_l_l)
frm_0.pack(side='left')
frm_1.pack(side='right')
frm_2 = tk.Frame(frm_l_r)
frm_3 = tk.Frame(frm_l_r)
frm_2.pack(side='left')
frm_3.pack(side='right')
frm_4 = tk.Frame(frm_r_l)
frm_5 = tk.Frame(frm_r_l)
frm_4.pack(side='left')
frm_5.pack(side='right')
frm_6 = tk.Frame(frm_r_r)
frm_7 = tk.Frame(frm_r_r)
frm_6.pack(side='left')
frm_7.pack(side='right')

sites = site_name  # 51个地点
select_site = []  # 存放被选中的地点

sites_dict = {}  # 地点与按钮对应的字典
i = 0
for site in sites:
    sites_dict["b" + str(i)] = site
    i += 1


def print_site_b0():
    global select_site
    t.insert('end', sites_dict['b0'] + " ")
    b0.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b0'])


def print_site_b1():
    global select_site
    t.insert('end', sites_dict['b1'] + " ")
    b1.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b1'])


def print_site_b2():
    global select_site
    t.insert('end', sites_dict['b2'] + " ")
    b2.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b2'])


def print_site_b3():
    global select_site
    t.insert('end', sites_dict['b3'] + " ")
    b3.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b3'])


def print_site_b4():
    global select_site
    t.insert('end', sites_dict['b4'] + " ")
    b4.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b4'])


def print_site_b5():
    global select_site
    t.insert('end', sites_dict['b5'] + " ")
    b5.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b5'])


def print_site_b6():
    global select_site
    t.insert('end', sites_dict['b6'] + " ")
    b6.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b6'])


def print_site_b7():
    global select_site
    t.insert('end', sites_dict['b7'] + " ")
    b7.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b7'])


def print_site_b8():
    global select_site
    t.insert('end', sites_dict['b8'] + " ")
    b8.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b8'])


def print_site_b9():
    global select_site
    t.insert('end', sites_dict['b9'] + " ")
    b9.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b9'])


def print_site_b10():
    global select_site
    t.insert('end', sites_dict['b10'] + " ")
    b10.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b10'])


def print_site_b11():
    global select_site
    t.insert('end', sites_dict['b11'] + " ")
    b11.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b11'])


def print_site_b12():
    global select_site
    t.insert('end', sites_dict['b12'] + " ")
    b12.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b12'])


def print_site_b13():
    global select_site
    t.insert('end', sites_dict['b13'] + " ")
    b13.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b13'])


def print_site_b14():
    global select_site
    t.insert('end', sites_dict['b14'] + " ")
    b14.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b14'])


def print_site_b15():
    global select_site
    t.insert('end', sites_dict['b15'] + " ")
    b15.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b15'])


def print_site_b16():
    global select_site
    t.insert('end', sites_dict['b16'] + " ")
    b16.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b16'])


def print_site_b17():
    global select_site
    t.insert('end', sites_dict['b17'] + " ")
    b17.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b17'])


def print_site_b18():
    global select_site
    t.insert('end', sites_dict['b18'] + " ")
    b18.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b18'])


def print_site_b19():
    global select_site
    t.insert('end', sites_dict['b19'] + " ")
    b19.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b19'])


def print_site_b20():
    global select_site
    t.insert('end', sites_dict['b20'] + " ")
    b20.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b20'])


def print_site_b21():
    global select_site
    t.insert('end', sites_dict['b21'] + " ")
    b21.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b21'])


def print_site_b22():
    global select_site
    t.insert('end', sites_dict['b22'] + " ")
    b22.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b22'])


def print_site_b23():
    global select_site
    t.insert('end', sites_dict['b23'] + " ")
    b23.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b23'])


def print_site_b24():
    global select_site
    t.insert('end', sites_dict['b24'] + " ")
    b24.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b24'])


def print_site_b25():
    global select_site
    t.insert('end', sites_dict['b25'] + " ")
    b25.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b25'])


def print_site_b26():
    global select_site
    t.insert('end', sites_dict['b26'] + " ")
    b26.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b26'])


def print_site_b27():
    global select_site
    t.insert('end', sites_dict['b27'] + " ")
    b27.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b27'])


def print_site_b28():
    global select_site
    t.insert('end', sites_dict['b28'] + " ")
    b28.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b28'])


def print_site_b29():
    global select_site
    t.insert('end', sites_dict['b29'] + " ")
    b29.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b29'])


def print_site_b30():
    global select_site
    t.insert('end', sites_dict['b30'] + " ")
    b30.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b30'])


def print_site_b31():
    global select_site
    t.insert('end', sites_dict['b31'] + " ")
    b31.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b31'])


def print_site_b32():
    global select_site
    t.insert('end', sites_dict['b32'] + " ")
    b32.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b32'])


def print_site_b33():
    global select_site
    t.insert('end', sites_dict['b33'] + " ")
    b33.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b33'])


def print_site_b34():
    global select_site
    t.insert('end', sites_dict['b34'] + " ")
    b34.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b34'])


def print_site_b35():
    global select_site
    t.insert('end', sites_dict['b35'] + " ")
    b35.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b35'])


def print_site_b36():
    global select_site
    t.insert('end', sites_dict['b36'] + " ")
    b36.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b36'])


def print_site_b37():
    global select_site
    t.insert('end', sites_dict['b37'] + " ")
    b37.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b37'])


def print_site_b38():
    global select_site
    t.insert('end', sites_dict['b38'] + " ")
    b38.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b38'])


def print_site_b39():
    global select_site
    t.insert('end', sites_dict['b39'] + " ")
    b39.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b39'])


def print_site_b40():
    global select_site
    t.insert('end', sites_dict['b40'] + " ")
    b40.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b40'])


def print_site_b41():
    global select_site
    t.insert('end', sites_dict['b41'] + " ")
    b41.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b41'])


def print_site_b42():
    global select_site
    t.insert('end', sites_dict['b42'] + " ")
    b42.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b42'])


def print_site_b43():
    global select_site
    t.insert('end', sites_dict['b43'] + " ")
    b43.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b43'])


def print_site_b44():
    global select_site
    t.insert('end', sites_dict['b44'] + " ")
    b44.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b44'])


def print_site_b45():
    global select_site
    t.insert('end', sites_dict['b45'] + " ")
    b45.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b45'])


def print_site_b46():
    global select_site
    t.insert('end', sites_dict['b46'] + " ")
    b46.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b46'])


def print_site_b47():
    global select_site
    t.insert('end', sites_dict['b47'] + " ")
    b47.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b47'])


def print_site_b48():
    global select_site
    t.insert('end', sites_dict['b48'] + " ")
    b48.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b48'])


def print_site_b49():
    global select_site
    t.insert('end', sites_dict['b49'] + " ")
    b49.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b49'])


def print_site_b50():
    global select_site
    t.insert('end', sites_dict['b50'] + " ")
    b50.config(bg='DeepSkyBlue', fg='OrangeRed')
    select_site.append(sites_dict['b50'])


def print_site_b51():
    global select_site
    global sites
    for site in sites:
        if site not in select_site:
            select_site.append(site)
            t.insert('end', site + " ")

    b0.config(bg='DeepSkyBlue', fg='OrangeRed')
    b1.config(bg='DeepSkyBlue', fg='OrangeRed')
    b2.config(bg='DeepSkyBlue', fg='OrangeRed')
    b3.config(bg='DeepSkyBlue', fg='OrangeRed')
    b4.config(bg='DeepSkyBlue', fg='OrangeRed')
    b5.config(bg='DeepSkyBlue', fg='OrangeRed')
    b6.config(bg='DeepSkyBlue', fg='OrangeRed')
    b7.config(bg='DeepSkyBlue', fg='OrangeRed')
    b8.config(bg='DeepSkyBlue', fg='OrangeRed')
    b9.config(bg='DeepSkyBlue', fg='OrangeRed')
    b10.config(bg='DeepSkyBlue', fg='OrangeRed')
    b11.config(bg='DeepSkyBlue', fg='OrangeRed')
    b12.config(bg='DeepSkyBlue', fg='OrangeRed')
    b13.config(bg='DeepSkyBlue', fg='OrangeRed')
    b14.config(bg='DeepSkyBlue', fg='OrangeRed')
    b15.config(bg='DeepSkyBlue', fg='OrangeRed')
    b16.config(bg='DeepSkyBlue', fg='OrangeRed')
    b17.config(bg='DeepSkyBlue', fg='OrangeRed')
    b18.config(bg='DeepSkyBlue', fg='OrangeRed')
    b19.config(bg='DeepSkyBlue', fg='OrangeRed')
    b20.config(bg='DeepSkyBlue', fg='OrangeRed')
    b21.config(bg='DeepSkyBlue', fg='OrangeRed')
    b22.config(bg='DeepSkyBlue', fg='OrangeRed')
    b23.config(bg='DeepSkyBlue', fg='OrangeRed')
    b24.config(bg='DeepSkyBlue', fg='OrangeRed')
    b25.config(bg='DeepSkyBlue', fg='OrangeRed')
    b26.config(bg='DeepSkyBlue', fg='OrangeRed')
    b27.config(bg='DeepSkyBlue', fg='OrangeRed')
    b28.config(bg='DeepSkyBlue', fg='OrangeRed')
    b29.config(bg='DeepSkyBlue', fg='OrangeRed')
    b30.config(bg='DeepSkyBlue', fg='OrangeRed')
    b31.config(bg='DeepSkyBlue', fg='OrangeRed')
    b32.config(bg='DeepSkyBlue', fg='OrangeRed')
    b33.config(bg='DeepSkyBlue', fg='OrangeRed')
    b34.config(bg='DeepSkyBlue', fg='OrangeRed')
    b35.config(bg='DeepSkyBlue', fg='OrangeRed')
    b36.config(bg='DeepSkyBlue', fg='OrangeRed')
    b37.config(bg='DeepSkyBlue', fg='OrangeRed')
    b38.config(bg='DeepSkyBlue', fg='OrangeRed')
    b39.config(bg='DeepSkyBlue', fg='OrangeRed')
    b40.config(bg='DeepSkyBlue', fg='OrangeRed')
    b41.config(bg='DeepSkyBlue', fg='OrangeRed')
    b42.config(bg='DeepSkyBlue', fg='OrangeRed')
    b43.config(bg='DeepSkyBlue', fg='OrangeRed')
    b44.config(bg='DeepSkyBlue', fg='OrangeRed')
    b45.config(bg='DeepSkyBlue', fg='OrangeRed')
    b46.config(bg='DeepSkyBlue', fg='OrangeRed')
    b47.config(bg='DeepSkyBlue', fg='OrangeRed')
    b48.config(bg='DeepSkyBlue', fg='OrangeRed')
    b49.config(bg='DeepSkyBlue', fg='OrangeRed')
    b50.config(bg='DeepSkyBlue', fg='OrangeRed')


def print_site_b52():
    global select_site
    global sites
    for site in sites:
        if site not in select_site:
            select_site.append(site)
            t.insert('end', site + " ")

    b0.config(bg='DeepSkyBlue', fg='OrangeRed')
    b1.config(bg='DeepSkyBlue', fg='OrangeRed')
    b2.config(bg='DeepSkyBlue', fg='OrangeRed')
    b3.config(bg='DeepSkyBlue', fg='OrangeRed')
    b4.config(bg='DeepSkyBlue', fg='OrangeRed')
    b5.config(bg='DeepSkyBlue', fg='OrangeRed')
    b6.config(bg='DeepSkyBlue', fg='OrangeRed')
    b7.config(bg='DeepSkyBlue', fg='OrangeRed')
    b8.config(bg='DeepSkyBlue', fg='OrangeRed')
    b9.config(bg='DeepSkyBlue', fg='OrangeRed')
    b10.config(bg='DeepSkyBlue', fg='OrangeRed')
    b11.config(bg='DeepSkyBlue', fg='OrangeRed')
    b12.config(bg='DeepSkyBlue', fg='OrangeRed')
    b13.config(bg='DeepSkyBlue', fg='OrangeRed')
    b14.config(bg='DeepSkyBlue', fg='OrangeRed')
    b15.config(bg='DeepSkyBlue', fg='OrangeRed')
    b16.config(bg='DeepSkyBlue', fg='OrangeRed')
    b17.config(bg='DeepSkyBlue', fg='OrangeRed')
    b18.config(bg='DeepSkyBlue', fg='OrangeRed')
    b19.config(bg='DeepSkyBlue', fg='OrangeRed')
    b20.config(bg='DeepSkyBlue', fg='OrangeRed')
    b21.config(bg='DeepSkyBlue', fg='OrangeRed')
    b22.config(bg='DeepSkyBlue', fg='OrangeRed')
    b23.config(bg='DeepSkyBlue', fg='OrangeRed')
    b24.config(bg='DeepSkyBlue', fg='OrangeRed')
    b25.config(bg='DeepSkyBlue', fg='OrangeRed')
    b26.config(bg='DeepSkyBlue', fg='OrangeRed')
    b27.config(bg='DeepSkyBlue', fg='OrangeRed')
    b28.config(bg='DeepSkyBlue', fg='OrangeRed')
    b29.config(bg='DeepSkyBlue', fg='OrangeRed')
    b30.config(bg='DeepSkyBlue', fg='OrangeRed')
    b31.config(bg='DeepSkyBlue', fg='OrangeRed')
    b32.config(bg='DeepSkyBlue', fg='OrangeRed')
    b33.config(bg='DeepSkyBlue', fg='OrangeRed')
    b34.config(bg='DeepSkyBlue', fg='OrangeRed')
    b35.config(bg='DeepSkyBlue', fg='OrangeRed')
    b36.config(bg='DeepSkyBlue', fg='OrangeRed')
    b37.config(bg='DeepSkyBlue', fg='OrangeRed')
    b38.config(bg='DeepSkyBlue', fg='OrangeRed')
    b39.config(bg='DeepSkyBlue', fg='OrangeRed')
    b40.config(bg='DeepSkyBlue', fg='OrangeRed')
    b41.config(bg='DeepSkyBlue', fg='OrangeRed')
    b42.config(bg='DeepSkyBlue', fg='OrangeRed')
    b43.config(bg='DeepSkyBlue', fg='OrangeRed')
    b44.config(bg='DeepSkyBlue', fg='OrangeRed')
    b45.config(bg='DeepSkyBlue', fg='OrangeRed')
    b46.config(bg='DeepSkyBlue', fg='OrangeRed')
    b47.config(bg='DeepSkyBlue', fg='OrangeRed')
    b48.config(bg='DeepSkyBlue', fg='OrangeRed')
    b49.config(bg='DeepSkyBlue', fg='OrangeRed')
    b50.config(bg='DeepSkyBlue', fg='OrangeRed')


b0 = tk.Button(frm_0, text=sites_dict['b0'], width=13, height=1, activebackground='DeepSkyBlue',
               activeforeground='OrangeRed', command=print_site_b0)
b0.pack()
origin_bgcolor = b0.cget("background")
origin_fgcolor = b0.cget("foreground")
b1 = tk.Button(frm_1, text=sites_dict['b1'], width=13, height=1, activebackground='DeepSkyBlue',
               activeforeground='OrangeRed', command=print_site_b1)
b1.pack()
b2 = tk.Button(frm_2, text=sites_dict['b2'], width=13, height=1, activebackground='DeepSkyBlue',
               activeforeground='OrangeRed', command=print_site_b2)
b2.pack()
b3 = tk.Button(frm_3, text=sites_dict['b3'], width=13, height=1, activebackground='DeepSkyBlue',
               activeforeground='OrangeRed', command=print_site_b3)
b3.pack()
b4 = tk.Button(frm_4, text=sites_dict['b4'], width=13, height=1, activebackground='DeepSkyBlue',
               activeforeground='OrangeRed', command=print_site_b4)
b4.pack()
b5 = tk.Button(frm_5, text=sites_dict['b5'], width=13, height=1, activebackground='DeepSkyBlue',
               activeforeground='OrangeRed', command=print_site_b5)
b5.pack()
b6 = tk.Button(frm_6, text=sites_dict['b6'], width=13, height=1, activebackground='DeepSkyBlue',
               activeforeground='OrangeRed', command=print_site_b6)
b6.pack()
b7 = tk.Button(frm_7, text=sites_dict['b7'], width=13, height=1, activebackground='DeepSkyBlue',
               activeforeground='OrangeRed', command=print_site_b7)
b7.pack()
b8 = tk.Button(frm_0, text=sites_dict['b8'], width=13, height=1, activebackground='DeepSkyBlue',
               activeforeground='OrangeRed', command=print_site_b8)
b8.pack()
b9 = tk.Button(frm_1, text=sites_dict['b9'], width=13, height=1, activebackground='DeepSkyBlue',
               activeforeground='OrangeRed', command=print_site_b9)
b9.pack()
b10 = tk.Button(frm_2, text=sites_dict['b10'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b10)
b10.pack()
b11 = tk.Button(frm_3, text=sites_dict['b11'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b11)
b11.pack()
b12 = tk.Button(frm_4, text=sites_dict['b12'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b12)
b12.pack()
b13 = tk.Button(frm_5, text=sites_dict['b13'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b13)
b13.pack()
b14 = tk.Button(frm_6, text=sites_dict['b14'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b14)
b14.pack()
b51 = tk.Button(frm_7, text="全选", width=13, height=1, bg="Beige", command=print_site_b51)
b51.pack()

frm1 = tk.Frame(window)
frm1.pack()
frm1_l = tk.Frame(frm1)
frm1_r = tk.Frame(frm1)
frm1_l.pack(side='left')
frm1_r.pack(side='right')
frm1_l_l = tk.Frame(frm1_l)
frm1_l_r = tk.Frame(frm1_l)
frm1_l_l.pack(side='left')
frm1_l_r.pack(side='right')
frm1_r_l = tk.Frame(frm1_r)
frm1_r_r = tk.Frame(frm1_r)
frm1_r_l.pack(side='left')
frm1_r_r.pack(side='right')
b15 = tk.Button(frm_0, text=sites_dict['b15'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b15)
b15.pack()
b16 = tk.Button(frm_1, text=sites_dict['b16'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b16)
b16.pack()
b17 = tk.Button(frm_2, text=sites_dict['b17'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b17)
b17.pack()
b18 = tk.Button(frm_3, text=sites_dict['b18'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b18)
b18.pack()
b19 = tk.Button(frm_4, text=sites_dict['b19'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b19)
b19.pack()
b20 = tk.Button(frm_5, text=sites_dict['b20'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b20)
b20.pack()
b21 = tk.Button(frm_6, text=sites_dict['b21'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b21)
b21.pack()
b22 = tk.Button(frm_7, text=sites_dict['b22'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b22)
b22.pack()
b23 = tk.Button(frm_0, text=sites_dict['b23'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b23)
b23.pack()
b24 = tk.Button(frm_1, text=sites_dict['b24'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b24)
b24.pack()
b25 = tk.Button(frm_2, text=sites_dict['b25'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b25)
b25.pack()
b26 = tk.Button(frm_3, text=sites_dict['b26'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b26)
b26.pack()
b27 = tk.Button(frm_4, text=sites_dict['b27'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b27)
b27.pack()
b28 = tk.Button(frm_5, text=sites_dict['b28'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b28)
b28.pack()
b29 = tk.Button(frm_6, text=sites_dict['b29'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b29)
b29.pack()
b30 = tk.Button(frm_7, text=sites_dict['b30'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b30)
b30.pack()
b31 = tk.Button(frm_0, text=sites_dict['b31'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b31)
b31.pack()
b32 = tk.Button(frm_1, text=sites_dict['b32'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b32)
b32.pack()
b33 = tk.Button(frm_2, text=sites_dict['b33'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b33)
b33.pack()
b34 = tk.Button(frm_3, text=sites_dict['b34'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b34)
b34.pack()
b35 = tk.Button(frm_4, text=sites_dict['b35'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b35)
b35.pack()
b36 = tk.Button(frm_5, text=sites_dict['b36'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b36)
b36.pack()
b37 = tk.Button(frm_6, text=sites_dict['b37'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b37)
b37.pack()
b38 = tk.Button(frm_7, text=sites_dict['b38'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b38)
b38.pack()
b39 = tk.Button(frm_0, text=sites_dict['b39'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b39)
b39.pack()
b40 = tk.Button(frm_1, text=sites_dict['b40'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b40)
b40.pack()
b41 = tk.Button(frm_2, text=sites_dict['b41'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b41)
b41.pack()
b42 = tk.Button(frm_3, text=sites_dict['b42'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b42)
b42.pack()
b43 = tk.Button(frm_4, text=sites_dict['b43'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b43)
b43.pack()
b44 = tk.Button(frm_5, text=sites_dict['b44'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b44)
b44.pack()
b45 = tk.Button(frm_6, text=sites_dict['b45'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b45)
b45.pack()
b46 = tk.Button(frm_7, text=sites_dict['b46'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b46)
b46.pack()
b47 = tk.Button(frm_0, text=sites_dict['b47'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b47)
b47.pack()
b48 = tk.Button(frm_1, text=sites_dict['b48'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b48)
b48.pack()
b49 = tk.Button(frm_2, text=sites_dict['b49'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b49)
b49.pack()
b50 = tk.Button(frm_3, text=sites_dict['b50'], width=13, height=1, activebackground='DeepSkyBlue',
                activeforeground='OrangeRed', command=print_site_b50)
b50.pack()
b57 = tk.Button(frm_4, width=13, height=1, activebackground='DeepSkyBlue', activeforeground='OrangeRed', relief=GROOVE)
b57.pack()
b54 = tk.Button(frm_5, width=13, height=1, activebackground='DeepSkyBlue', activeforeground='OrangeRed', relief=GROOVE)
b54.pack()
b55 = tk.Button(frm_6, width=13, height=1, activebackground='DeepSkyBlue', activeforeground='OrangeRed', relief=GROOVE)
b55.pack()
b52 = tk.Button(frm_7, text="选择所有剩余", width=13, height=1, bg="Beige", command=print_site_b52)
b52.pack()

l2 = tk.Label(window, text='第一个为起点，再经过剩余景点: ').pack()
t = tk.Text(window, height=4)
t.pack()

frmx = tk.Frame(window)
frmx.pack()
frmx_l = tk.Frame(frmx)
frmx_r = tk.Frame(frmx)
frmx_l.pack(side='left')
frmx_r.pack(side='right')


# def print_b41():
#   t.delete('insert')

def print_b53():
    t.delete('0.0', 'end')
    select_site.clear(),  # 将已选地点清空
    l3.config(text="", bg=origin_bgcolor)
    t1.delete('0.0', 'end')
    t1.config(bg=origin_bgcolor, bd=0)
    plt.close('all')

    b0.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b1.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b2.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b3.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b4.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b5.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b6.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b7.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b8.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b9.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b10.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b11.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b12.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b13.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b14.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b15.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b16.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b17.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b18.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b19.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b20.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b21.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b22.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b23.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b24.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b25.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b26.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b27.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b28.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b29.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b30.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b31.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b32.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b33.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b34.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b35.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b36.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b37.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b38.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b39.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b40.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b41.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b42.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b43.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b44.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b45.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b46.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b47.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b48.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b49.config(bg=origin_bgcolor, fg=origin_fgcolor)
    b50.config(bg=origin_bgcolor, fg=origin_fgcolor)


# b41 = tk.Button(frmx_l,text="光标后单删",width=30, height=2,activebackground='DeepSkyBlue',activeforeground='OrangeRed',command=print_b41)
# b41.pack()
b53 = tk.Button(text="全部删除", width=30, height=1, activebackground='DeepSkyBlue', activeforeground='OrangeRed',
                command=print_b53)
b53.pack()

l4 = tk.Label(window, text="请选择输出方案的个数", height=2)
l4.pack()
e = tk.Entry(window, show=None)
e.pack()


def run():
    global select_site
    # 获得输出方案个数
    output = int(e.get())

    # 起点及地点对应整数编码
    origin, select_site_index = get_origin(select_site)
    # 初始化种群
    population = generate_population(select_site_index)
    DistanceAndPath = get_result(population, origin)

    # 开始迭代
    register = []
    i = 0
    while i < itter_time:
        # 选择繁殖个体群
        parents = selection(population, origin)
        # 交叉繁殖
        children = crossover(parents)
        # 变异操作
        mutation(children)
        # 更新种群
        population = parents + children
        # 更新最优解

        DistanceAndPath = get_result(population, origin)
        register.append(DistanceAndPath[0][0])
        i += 1

    result_path_name = []
    result_path_name.append(index_site_dict[origin])
    for item in DistanceAndPath[0][1]:
        result_path_name.append(index_site_dict[item])
    # l3.config(text="演变结束! 最优总路径距离为:"+str(DistanceAndPath[0][0])+"\n最优路径为:",bg="OrangeRed")
    l3.config(text="演变结束! " + "  最优路径为:", bg="Beige")
    t1.config(bg="SkyBlue", bd=2)
    t1.insert('end', result_path_name)

    for j in range(output):
        result_path = DistanceAndPath[j][1]
        distance = DistanceAndPath[j][0]

        plt.figure(j + 1)
        draw(origin, result_path, distance)

        plt.figure(j + 2)
        plt.plot(list(range(len(register))), register)
        plt.title("最优结果变化趋势")
        plt.show()


b60 = tk.Button(window, text="RUN", width=15, height=2, activebackground='DeepSkyBlue', activeforeground='OrangeRed',
                command=run)
b60.pack()

l3 = tk.Label(window, height=3)
l3.pack()

t1 = tk.Text(window, height=3, bg=origin_bgcolor, bd=0)
t1.pack()

window.mainloop()

