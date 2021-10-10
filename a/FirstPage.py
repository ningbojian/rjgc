import tkinter as tk
import os

#登入界面
def click_1():
   os.system('python ./game/game_huarongdao.py')

def click_2():
   os.system('python ./game/game_shudu/main.py')

def click_3():
   os.system('python ./calculator/cal.py')

def click_4():
   os.system('python jinzhi.py')

def click_5():
   os.system('python ./game/game_guess.py')

def click_6():
   os.system('python ./solution/hr/hr.py')

def click_7():
   os.system('python ./solution/soduku/soduku.py')


window=tk.Tk()
window.title("欢迎使用多功能计算器")
window.geometry('500x300')
lab_1=tk.Label(window,text="请选择：")
lab_1.pack()
but_dr1=tk.Button(window, text="1..........华容道游戏",command=click_1)
but_dr2=tk.Button(window, text="2............数独游戏", command=click_2)
but_dr3=tk.Button(window, text="3..........科学计算器", command=click_3)
but_dr4=tk.Button(window, text="4..进制转换/斐波那契数", command=click_4)
but_dr5=tk.Button(window, text="5..猜数字/测试反应速度", command=click_5)
but_dr6=tk.Button(window, text="6..........求解华容道", command=click_6)
but_dr7=tk.Button(window, text="7............求解数独", command=click_7)
lab_1.grid(row=0,column=0)
but_dr1.grid(row=1,column=10)
but_dr2.grid(row=3, column=10)
but_dr3.grid(row=5, column=10)
but_dr4.grid(row=7, column=10)
but_dr5.grid(row=9, column=10)
but_dr6.grid(row=1, column=50)
but_dr7.grid(row=3, column=50)
window.mainloop()



