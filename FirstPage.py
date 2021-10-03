import tkinter as tk
import os

#登入界面
def click_1():

   window1=tk.Tk()
   window1.title("欢迎进入三阶华容道")
   window1.geometry('500x300')
   lab_1=tk.Label(window1,text="游戏规则如下：将打乱的1-8复原到数字九宫格对应的位置，点击计算",height=3)
   lab_1.grid(row=0,column=0,sticky="w"+"e")
   window1.mainloop()

def click_2():
   os.system('python soduku.py')

def click_3():
   os.system('python cal.py')


window=tk.Tk()
window.title("欢迎使用多功能计算器")
window.geometry('500x300')
lab_1=tk.Label(window,text="请选择：")
lab_1.pack()
but_dr1=tk.Button(window,text="华容道",command=click_1)
but_dr2=tk.Button(window, text="数独", command=click_2)
but_dr3=tk.Button(window, text="科学计算器", command=click_3)
lab_1.grid(row=0,column=0)
but_dr1.grid(row=1,column=10)
but_dr2.grid(row=5, column=10)
but_dr3.grid(row=7, column=10)
window.mainloop()



