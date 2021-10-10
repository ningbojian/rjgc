import tkinter as tk
import os


window=tk.Tk()
window.title("数独计算结果是")
window.geometry('500x300')
f = open('out.txt', "r", encoding='utf-8')
lab_1=tk.Label(window, text=f.read())
lab_1.pack()
window.mainloop()



