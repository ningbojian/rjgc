import tkinter as tk
import random
def moveNum(nTag):              #移动被鼠标点击的数字，参数是在Canvas中字符对象的tag
    global X0,Y0,w,gameOver     #空位所在位置的坐标(X0,Y0)
    x,y=w.coords(nTag)          #得到被点击的数字所在位置的坐标
    if abs(x-X0)+abs(y-Y0)==60 and gameOver==False:  #判断被单击数字是否和空白处相邻
        w.move(nTag,X0-x,Y0-y)  #如果和空白处相邻,移动数字到空白处,第2,3参数是移动增量
        X0,Y0=x,y                           #记录新空白处位置坐标
        numbers=list('087654321')
        for y in range(90,270,60):           #y为Canvas的y坐标,90,150,210
            for x in range(90,270,60):       #x为Canvas的x坐标,90,150,210
                m=numbers.pop()
                if m!= '0':                 #如m!= '0'，8个数字还未检查完
#tag='1'字符对象显示1，在(90,90)位置正确，tag='2'字符对象显示2，在(150,90)处正确，等等
                    if [x,y]!=w.coords("A"+m):  #如相应字符对象位置不正确，玩家未赢
                        return
                else:                       #如m=='0'，8个数字所在位置正确，玩家赢了
                    gameOver=True
                    label['text']="你赢了"
root = tk.Tk()                                #初始化窗口
root.title('数字华容道_用Canvas实现')          #窗口标题
root.geometry("300x260+200+20")#窗口宽300,高=2600,窗口左上点离屏幕左边界200,离屏幕上边界距离20。
root.resizable(width=False,height=False) #设置窗口是否可变，这里宽不可变，高不可变，默认为True
w = tk.Canvas(root, width = 300, height = 260, background = "#D2B48C")        #建立Canvas对象
w.pack()
gameOver=False
numbers=list('123456780')
random.shuffle(numbers)             #使列表数字和空白随机排列
label=tk.Label(w,text='单击数字移动方块',fg='#000000',font=("Arial",15), background = "#D2B48C")
label.place(x=20,y=10,width=250,height=40)
X0=Y0=0                                #空位所在位置的坐标(X0,Y0)
for x in range(60,300,60):          #画棋盘4条竖线,x为Canvas的x坐标
    w.create_line(x,60,x,240,fill = "#FFE4B5",width = 3)
for y in range(60,300,60):          #画棋盘4条横线,y为Canvas的y坐标
    w.create_line(60,y,240,y,fill = "#FFE4B5",width = 3)
for y in range(90,270,60):           #y为Canvas的y坐标,90,150,210
    for x in range(90,270,60):       #x为Canvas的x坐标,90,150,210
        n=numbers.pop()
        if n!='0':#如n!='0',建立8个数字对象,注意tag有2个值,可通过"R"操作所有数字对象,如删除所有数字
            w.create_text(x,y,text=n,fill="#000000",tag=("A"+n,"R"),font=("Arial",40))#tag=A1,显示1
            def leftClick(event,nTag="A"+n): #每个按钮都生成一个事件函数，参数默认值是该数字的tag
                moveNum(nTag)            #所有事件函数都调用同一函数
            w.tag_bind("A"+n,'<Button-1>',leftClick)        #绑定左键单击事件
        else:                           #n=0,代表空白，记住无数字的空位的Canvas坐标(x,y)
            X0,Y0=x,y
root.mainloop()
