"""
Created on Fri Nov 20 01:10:56 2020
@author: MU-PING
"""

import matplotlib.pyplot as plt
import tkinter as tk
import os
import numpy as np
import time
from math import floor, ceil
from random import randint
from matplotlib import animation
from tkinter import messagebox
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from collections import defaultdict

def gen_data():
    plt.clf()
    plt.title("Data")
    
    cluster = np.random.randint(2, 5)
    data = []
    for i in range(cluster): #群數
        single_data=[]
        center_x = np.random.randint(-31, 31)
        center_y = np.random.randint(-31, 31)
        single_data.append([center_x, center_y])
        for j in range(np.random.randint(48/cluster, 96/cluster)): #一群的點數
            new_x = center_x + np.random.uniform(-3.5, 3.5)
            new_y = center_y + np.random.uniform(-3.5, 3.5)
            single_data.append([new_x, new_y])
            plt.plot(new_x, new_y, 'o', ms=3 , color = 'gray', alpha=.8) #畫圖 ms：折點大小
    canvas1.draw()
def Euclid():
    pass
def Cosθ():
    pass
def Dot():
    pass
def start():
    pass
window = tk.Tk()
window.geometry("520x390")
window.resizable(False, False)
window.title("競爭式學習法 - 單層神經網路")

classification = ["歐基里德距離", "cosθ值", "內積"]
setting1 = tk.Frame(window)
setting1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N)

lr = tk.IntVar()#學習率
lr.set(1)
Neurons = tk.IntVar()#神經元個數
Neurons.set(3)

tk.Label(setting1, font=("微軟正黑體", 12, "bold"), text="學習率：").grid(row=0, sticky=tk.W, pady=5)
tk.Entry(setting1, width=10, textvariable=lr).grid(row=1, sticky=tk.W)
tk.Label(setting1, font=("微軟正黑體", 12, "bold"), text="神經元個數：").grid(row=2, sticky=tk.W, pady=5)
tk.Entry(setting1, width=10, textvariable=Neurons).grid(row=3, sticky=tk.W)
tk.Label(setting1, font=("微軟正黑體", 12, "bold"), text="分類標準").grid(row=4, sticky=tk.W, pady=4)
data_combobox = ttk.Combobox(setting1, value = classification, state="readonly", width=12) #readonly為只可讀狀態
data_combobox.grid(row=5, sticky=tk.W)
btn = tk.Button(setting1, text='隨機產生資料', command = gen_data)
btn.grid(row=6, sticky=tk.W, pady=20)
btn = tk.Button(setting1, text='開始訓練', command = start)
btn.grid(row=7, sticky=tk.W)

setting2 = tk.Frame(window)
setting2.grid(row=0, column=1, pady=10)
fig = plt.figure(figsize=(5,5))
plt.title("Data")
canvas1 = FigureCanvasTkAgg(fig, setting2)  # A tk.DrawingArea.
canvas1.get_tk_widget().grid()

window.mainloop()