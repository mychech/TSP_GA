import os.path
import shutil
import tkinter as tk
import tkinter.ttk
from tsp import readDate, getDistanceMatrix, generate_population, get_origin, get_result, \
    selection, crossover, mutation, draw
import matplotlib.pyplot as plt
import cv2
import tkinter.messagebox
import queue, threading
import time
from PIL import Image, ImageSequence, ImageTk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('850x820')
        self.name2btn = {}
        self.isshow = False
        self.set_gui()
        self.show_text.insert("insert", "Init Model...\n")
        self.root.mainloop()


    def set_gui(self):
        pt_name, pt_coord = readDate('city.csv')
        self.all_pt_names = pt_name
        for i, name in enumerate(pt_name):
            pos_x, pos_y = i % 10 , i // 10 + 1
            self.name2btn[name] = tk.Checkbutton(self.root, text=name, bd=6, bg='green', width=5)
            self.name2btn[name].place(x=pos_x*80 + 20, y=pos_y*50 - 20)
            # print(pos_x*80 + 20, pos_y*50 - 20)
            self.name2btn[name].select()

        self.label1 = tk.Label(self.root, text='选择起始点:', width=10, height=1)
        self.comb_var = tkinter.StringVar()
        self.combox = tk.ttk.Combobox(self.root, textvariable=self.comb_var, width=20, height=5,
                            value=tuple(pt_name))
        self.combox.current(0)
        self.combox.bind("<<ComboboxSelected>>", self.ChangeStart)


        self.label2 = tk.Label(self.root, text='迭代次数:', width=10, height=1)
        self.label3 = tk.Label(self.root, text='种群数量:', width=10, height=1)
        self.label4 = tk.Label(self.root, text='变异概率:', width=10, height=1)

        self.envar1 = tk.StringVar(value='100')
        self.envar2 = tk.StringVar(value='500')
        self.envar3 = tk.StringVar(value='0.9')
        self.entr1 = tk.Entry(self.root, textvariable=self.envar1)
        self.entr2 = tk.Entry(self.root, textvariable=self.envar2)
        self.entr3 = tk.Entry(self.root, textvariable=self.envar3)

        self.show_text = tk.Text(self.root, width=50, height=20)

        self.start_btn = tk.Button(self.root, text='Start', width=10, height=2, font=('',15,'bold'),
                                   command=self.RunAlgo)

        self.show_btn = tk.Button(self.root, text='Best', width=10, height=2, font=('',15,'bold'),
                                   command=self.ShowImg)

        self.label1.place(x=20, y=240)
        self.label2.place(x=20, y=290)
        self.label3.place(x=20, y=340)
        self.label4.place(x=20, y=390)
        self.entr1.place(x=120, y=290)
        self.entr2.place(x=120, y=340)
        self.entr3.place(x=120, y=390)
        self.combox.place(x=100, y = 240)
        self.show_text.place(x=30, y=450)
        self.start_btn.place(x=40, y=750)
        self.show_btn.place(x=150, y=750)
        self.show_btn.config(state=tk.DISABLED)

        self.show_temp = tk.Label(self.root, bg='white')
        self.show_temp.place(x=400, y=200)

        self.ChangeStart(None)


    def ShowImg(self):
        img = cv2.resize(cv2.imread('temp.png'), (420, 550), cv2.INTER_CUBIC)
        cv2.imwrite('temp.png', img)
        photo = tk.PhotoImage(file='temp.png')
        self.show_temp.config(image=photo)
        self.root.mainloop()


    def ChangeStart(self, event):
        change_name = self.comb_var.get()
        # print(change_name)
        for name in self.all_pt_names:
            self.name2btn[name].configure(bg='green')
        self.name2btn[change_name].configure(bg='yellow')
        self.root.mainloop()



    def RunAlgo(self):
        self.show_text.insert("insert", '------     Start This Run!   ------\n')
        try:
            num_popu = int(self.envar2.get())
            num_iter = int(self.envar1.get())
            mul_rate = float(self.envar3.get())
            st_point = self.comb_var.get()
            print(num_popu, num_iter, mul_rate, st_point)
            self.start_btn.config(state=tk.DISABLED)

            self.progress = tk.IntVar()
            self.progress_max = num_iter
            self.progressbar = tkinter.ttk.Progressbar(self.root, mode='determinate', orient=tk.HORIZONTAL,
                                                       variable=self.progress,
                                                       maximum=self.progress_max,
                                                       length=250)
            self.progressbar.place(x=450, y=780)
            self.progress.set(0)

            self.thread_queue = queue.Queue()  # used to communicate between main thread (UI) and worker thread
            new_thread = threading.Thread(target=self.StartAlgo, kwargs={'num_pou':num_popu,
                                                                         'num_iter':num_iter,
                                                                         'mul_rate':mul_rate,
                                                                         'st_point':st_point})
            new_thread.start()

            # schedule a time-task to check UI
            # it's in main thread, because it's called by self.root
            self.root.after(50, self.listen_for_result)
        except:
            tkinter.messagebox.showinfo('Error', '参数出错/未找到相关数据文件！')




    def listen_for_result(self):
        try:
            progress = self.thread_queue.get(False)
            self.progress.set(progress)

        except queue.Empty:  # must exist to avoid trace-back
            pass
        finally:
            if self.progress.get() < self.progressbar['maximum']:
                self.root.after(50, self.listen_for_result)


    def StartAlgo(self, num_pou, num_iter, mul_rate, st_point):
        point_name, point_coordinate = readDate('city.csv')
        # distance matrix
        point_count = len(point_name)
        Distance = getDistanceMatrix(point_count, point_coordinate)

        # NUmber of population
        totalNum_population = num_pou
        # Number of evolutions
        itter_time = num_iter
        # mutation rate
        mutation_rate = mul_rate

        # point2idx idx2point
        point_idx_dict = {name: i for i, name in enumerate(point_name)}
        idx_point_dict = {i: name for i, name in enumerate(point_name)}

        # num of output
        output = 1
        select_point = [i for i in point_name]

        # start point and select point index
        origin, select_point_idx = get_origin(st_point, point_idx_dict, select_point)

        # init population
        population = generate_population(totalNum_population, select_point_idx)
        DistanceAndPath = get_result(population, origin, Distance)

        # 开始迭代
        register = []
        frames = []
        i = 0
        while i <= itter_time:
            print(i)
            # select population to reproduction
            parents = selection(population, origin, Distance)
            # Cross reproduction
            children = crossover(totalNum_population, parents)
            # mutation
            mutation(children, mutation_rate)
            # refresh population
            population = parents + children

            # refresh best solutions
            DistanceAndPath = get_result(population, origin, Distance)
            register.append(DistanceAndPath[0][0])


            if i == 0 or (i + 1) % 20 == 0:
                self.Plot(DistanceAndPath, point_name, point_coordinate, origin, register, i)
                img = cv2.resize(cv2.imread('temp.png'), (420, 550), cv2.INTER_CUBIC)
                cv2.imwrite('temp.png', img)
                photo = tk.PhotoImage(file='temp.png')
                self.show_temp.config(image=photo)
                self.show_temp.update()

                self.show_text.insert("insert", "[{}/{}]({}) Min Distance is :{:.2f}\n".format(i+1, itter_time,
                                                                                               st_point,
                                                                                                DistanceAndPath[0][0]))
            self.thread_queue.put(i)
            i += 1
        self.show_text.insert("insert", 'Best Travel Route is:\n')


        self.show_text.insert("insert", '------     Finish This Run!   ------\n')
        self.start_btn.config(state=tk.NORMAL)
        self.show_btn.config(state=tk.NORMAL)


    def Plot(self, DistanceAndPath, point_name, point_coordinate, origin, register, i):
        result_path = DistanceAndPath[0][1]
        distance = DistanceAndPath[0][0]
        plt.figure(figsize=(6, 12), dpi=200)

        plt.subplot(2, 1, 1)
        draw(origin, result_path, distance, point_coordinate, point_name)

        plt.subplot(2, 1, 2)
        plt.plot(list(range(len(register))), register)
        plt.title("距离随迭代次数变化的曲线")
        plt.savefig(f'temp.png', bbox_inches='tight')
        plt.savefig(f'best.png', bbox_inches='tight')



if __name__ == '__main__':
    gui = GUI()
