import tkinter as tk
import os


window=tk.Tk()
window.title("复原华容道")
window.geometry('800x800')
lab_1=tk.Label(window, text='具体步骤如下')
lab_1.pack()
f = open('hrout.txt', "r", encoding='utf-8')
text = tk.Text(window, width=60, height=50)
scroll = tk.Scrollbar()
# 放到窗口的右侧, 填充Y竖直方向
scroll.pack(side=tk.RIGHT, fill=tk.Y)
# 两个控件关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
text.pack()
str1 = f.read()
text.insert(tk.INSERT, str1)
window.mainloop()
