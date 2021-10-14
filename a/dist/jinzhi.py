import tkinter as tk  # 导入Tk库

window = tk.Tk()
window.title('进制转换器')
window.geometry('350x600')

# 页面布局
l2 = tk.Label(window, text='二进制数',font=('隶书',18))
l2.pack()
e2 = tk.Entry(window, show=None)
e2.pack()

l8 = tk.Label(window, text='八进制数',font=('隶书',18))
l8.pack()
e8 = tk.Entry(window, show=None)
e8.pack()

l10 = tk.Label(window, text='十进制数',font=('隶书',18))
l10.pack()
e10 = tk.Entry(window, show=None)
e10.pack()

l16 = tk.Label(window, text='十六进制数',font=('隶书',18))
l16.pack()
e16 = tk.Entry(window, show=None)
e16.pack()

lfib = tk.Label(window, text='斐波那契数',font=('隶书',18))
lfib.pack()
efib = tk.Entry(window, show=None)
efib.pack()

def computefib():
    a = efib.get()
    i = int(a)
    s = str(fibonacci(i))
    t.insert('insert', '第' + a +'个斐波那契数：'+s+'\n')


def fibonacci(i):
    if i <= 2:
        return 1
    elif i > 2:
        return fibonacci(i-1)+fibonacci(i-2)




# 按钮逻辑
def compute2():
    a2 = e2.get()
    a8 = e8.get()
    a10 = e10.get()
    a16 = e16.get()

    if a2 != '' and a8 == '' and a10 == '' and a16 == '':
        t.insert('insert', '二进制数：' + a2 + '   二进制:' + a2 + '\n')
    if a8 != '' and a10 == '' and a16 == '':
        t.insert('insert', '八进制数:' + a8 + '   二进制:' + bin(int(a8, 8)) + '\n')
    if a10 != '' and a16 == '':
        t.insert('insert', '十进制数:' + a10 + '   二进制:' + bin(int(a10)) + '\n')
    if a16 != '':
        t.insert('insert', '十六进制数:' + a16 + '   二进制:' + bin(int(a16, 16)) + '\n')


def compute8():
    a2 = e2.get()
    a8 = e8.get()
    a10 = e10.get()
    a16 = e16.get()

    if a2 != '' and a8 == '' and a10 == '' and a16 == '':
        t.insert('insert', '二进制数：' + a2 + '   八进制：' + oct(int(a2, 2)) + '\n')
    if a8 != '' and a10 == '' and a16 == '':
        t.insert('insert', '八进制数：' + a8 + '   八进制：' + a8 + '\n')
    if a10 != '' and a16 == '':
        t.insert('insert', '十进制数：' + a10 + '   八进制：' + oct(int(a10)) + '\n')
    if a16 != '':
        t.insert('insert', '十六进制数：' + a16 + '   八进制：' + oct(int(a16, 16)) + '\n')


def compute10():
    a2 = e2.get()
    a8 = e8.get()
    a10 = e10.get()
    a16 = e16.get()

    if a2 != '' and a8 == '' and a10 == '' and a16 == '':
        t.insert('insert', '二进制数：' + a2 + '   十进制：' + str(int(a2, 2)) + '\n')
    if a8 != '' and a10 == '' and a16 == '':
        t.insert('insert', '八进制数：' + a8 + '   十进制：' + str(int(a8, 8)) + '\n')
    if a10 != '' and a16 == '':
        t.insert('insert', '十进制数：' + a10 + '   十进制：' + a10 + '\n')
    if a16 != '':
        t.insert('insert', '十六进制数：' + a16 + '   十进制：' + str(int(a16, 16)) + '\n')


def compute16():
    a2 = e2.get()
    a8 = e8.get()
    a10 = e10.get()
    a16 = e16.get()

    if a2 != '' and a8 == '' and a10 == '' and a16 == '':
        t.insert('insert', '二进制数：' + a2 + '   十六进制：' + str(hex(int(a2, 2))) + '\n')
    if a8 != '' and a10 == '' and a16 == '':
        t.insert('insert', '八进制数：' + a8 + '   十六进制：' + str(hex(int(a8, 8))) + '\n')
    if a10 != '' and a16 == '':
        t.insert('insert', '十进制数：' + a10 + '   十六进制：' + hex(int(a10)) + '\n')
    if a16 != '':
        t.insert('insert', '十六进制数：' + a16 + '   十六进制：' + a16 + '\n')


# 按钮
b2 = tk.Button(window,
               text='转二进制',
               width=15, height=1,font=('隶书',15),
               command=compute2)
b2.pack()

b8 = tk.Button(window,
               text='转八进制',
               width=15, height=1,font=('隶书',15),
               command=compute8)
b8.pack()

b10 = tk.Button(window,
                text='转十进制',
                width=15, height=1,font=('隶书',15),
                command=compute10)
b10.pack()

b16 = tk.Button(window,
                text='转十六进制',
                width=15, height=1,font=('隶书',15),
                command=compute16)
b16.pack()

bfib = tk.Button(window,
                text='斐波那契数',
                width=15, height=1,font=('隶书',15),
                command=computefib)
bfib.pack()

# 结果文本框
t = tk.Text(window)
t.pack()
window.mainloop()  # 这句话必须要有，否则无法生成窗体exe文件
