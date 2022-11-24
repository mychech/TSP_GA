import tkinter as tk
from tkinter.ttk import *
import time
import threading, queue


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Demo')

    def show(self):
        self.progress = tk.IntVar()
        self.progress_max = 100
        self.progressbar = Progressbar(self.root, mode='determinate', orient=tk.HORIZONTAL, variable=self.progress,
                                       maximum=self.progress_max)
        self.progressbar.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.progress.set(0)

        btn = tk.Button(self.root, text='start', command=self.start)
        btn.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)
        self.btn = btn

        self.root.mainloop()

    def start(self):
        self.progress.set(0)
        self.btn.config(state=tk.DISABLED)

        self.thread_queue = queue.Queue()  # used to communicate between main thread (UI) and worker thread
        new_thread = threading.Thread(target=self.run_loop, kwargs={'param1': 100, 'param2': 20})
        new_thread.start()

        # schedule a time-task to check UI
        # it's in main thread, because it's called by self.root
        self.root.after(100, self.listen_for_result)

    def run_loop(self, param1, param2):
        progress = 0
        for entry in range(self.progress_max):
            time.sleep(0.1)
            progress = progress + 1
            self.thread_queue.put(progress)

    def listen_for_result(self):
        '''
        Check if there is something in the queue.
        Must be invoked by self.root to be sure it's running in main thread
        '''
        try:
            progress = self.thread_queue.get(False)
            self.progress.set(progress)
        except queue.Empty:  # must exist to avoid trace-back
            pass
        finally:
            if self.progress.get() < self.progressbar['maximum']:
                self.root.after(100, self.listen_for_result)
            else:
                self.btn.config(state=tk.NORMAL)


if __name__ == '__main__':
    win = MainWindow()
    win.show()