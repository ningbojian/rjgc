import tkinter as tk
import random
import time
number = random.randint(0,100)
running = True
num = 0
nmaxn = 100
nminn = 0
start_time = time.perf_counter()



def eBtnClose(event):
    root.destroy()
def eBtnGuess(eent):
    global nmaxn
    global nminn
    global num
    global running
    if running:
        var_a = int(entry_a.get())
        if var_a == number:
            labelqval("恭喜你答对了！")
            num += 1
            running = False
            numGuess()
        elif var_a < number:
            if var_a > nminn:
                nminn = var_a
                num += 1
                labelqval("小了哦，请输入"+str(nminn)+"到"+str(nmaxn)+"之间任意整数：")
        else:
            if var_a < nmaxn:
                nmaxn = var_a
                num +=1
                labelqval("大了哦，请输入"+str(nminn)+"到"+str(nmaxn)+"之间任意整数：")
    else:labelqval('你已经答对啦。。。')

def numGuess():
    end_time = time.perf_counter()
    total_time = end_time - start_time
    if num == 1:
        if total_time <= 15:
            labelqval('一次答对！' + '\n花费的时间是' + str(total_time) + 's'+'\n你真是个小机灵鬼!')
        elif total_time <= 25:
            labelqval('一次答对！' + '\n花费的时间是' + str(total_time) + 's'+'\n普普通通.......')
        else:
            labelqval('一次答对！' + '\n花费的时间是' + str(total_time) + 's'+'\n太慢了，你是在发呆吗？')
    elif num<10:
        if total_time <= 15:
            labelqval('厉害啦！！！10次以内就猜中了\n尝试次数 : ' + str(num) + '\n花费的时间是' + str(total_time) + 's'+'\n你真是个小机灵鬼!')
        elif total_time <= 25:
            labelqval('厉害啦！！！10次以内就猜中了\n尝试次数 : ' + str(num) + '\n花费的时间是' + str(total_time) + 's'+'\n普普通通.......')
        else:
            labelqval('厉害啦！！！10次以内就猜中了\n尝试次数 : '+str(num)+'\nbut...花费的时间是'+str(total_time)+'s'+'\n太慢了，你是在发呆吗？')
    else:
        if total_time <= 15:
            labelqval('猜对了！！尝试次数:' + str(num) + '\n花费的时间是' + str(total_time) + 's'+'\n你真是个小机灵鬼!')
        elif total_time <= 25:
            labelqval('猜对了！！尝试次数:' + str(num) + '\n花费的时间是' + str(total_time) + 's'+'\n普普通通.......')
        else:
            labelqval('猜对了！！尝试次数:'+str(num)+'\n花费的时间是'+str(total_time)+'s'+'\n太慢了，你是在发呆吗？')

def labelqval(vText):
    label_val_q.config(label_val_q,text = vText)

root = tk.Tk(className="猜数字游戏")
root.geometry("400x160+200+200")

line_a_tip=tk.Frame(root)
label_tip_max=tk.Label(line_a_tip,text=nmaxn)
label_tip_min=tk.Label(line_a_tip,text=nminn)
label_tip_max.pack(side="top",fill="x")
label_tip_min.pack(side="bottom",fill="y")


label_val_q = tk.Label(root,width = "80")
label_val_q.pack(side = "top")

entry_a = tk.Entry(root,width = "40")
btnGuess = tk.Button(root,text = "猜",font=('隶书',15))
entry_a.pack()
entry_a.bind('<Return>',eBtnGuess)
btnGuess.bind('<Button-1>',eBtnGuess)
btnGuess.pack()
btnClose = tk.Button(root,text = "关闭",font=('隶书',15))
btnClose.bind('<Button-1>',eBtnClose)
btnClose.pack()
labelqval("请输入0到100之间任意整数：")
entry_a.focus_get()
print(number)
root.mainloop()
