import copy
import tkinter as tk
import tkinter.messagebox
import os
soduku = [[] for i in range(9)]

#确定计算
def confirm():
    #绑定输入值
    str1 = E1.get()
    a1 = list(str1)
    for x in a1:
        if x in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            x = int(x)
            soduku[0].append(x)
        else:
            x = ''
            soduku[0].append(x)

    str2 = E2.get()
    a2 = list(str2)
    for x in a2:
        if x in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            x = int(x)
            soduku[1].append(x)
        else:
            x = ''
            soduku[1].append(x)

    str3 = E3.get()
    a3 = list(str3)
    for x in a3:
        if x in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            x = int(x)
            soduku[2].append(x)
        else:
            x = ''
            soduku[2].append(x)
    ###
    str4 = E4.get()
    a4 = list(str4)
    for x in a4:
        if x in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            x = int(x)
            soduku[3].append(x)
        else:
            x = ''
            soduku[3].append(x)

    str5 = E5.get()
    a5 = list(str5)
    for x in a5:
        if x in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            x = int(x)
            soduku[4].append(x)
        else:
            x = ''
            soduku[4].append(x)

    str6 = E6.get()
    a6 = list(str6)
    for x in a6:
        if x in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            x = int(x)
            soduku[5].append(x)
        else:
            x = ''
            soduku[5].append(x)
    ###
    str7 = E7.get()
    a7 = list(str7)
    for x in a7:
        if x in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            x = int(x)
            soduku[6].append(x)
        else:
            x = ''
            soduku[6].append(x)

    str8 = E8.get()
    a8 = list(str8)
    for x in a8:
        if x in('1','2','3','4','5','6','7','8','9'):
            x = int(x)
            soduku[7].append(x)
        else:
            x = ''
            soduku[7].append(x)

    str9 = E9.get()
    a9 = list(str9)
    for x in a9:
        if x in('1','2','3','4','5','6','7','8','9'):
            x = int(x)
            soduku[8].append(x)
        else:
            x = ''
            soduku[8].append(x)

        # 检测是否每一行都是九个数？
    if (len(str1)!=9)*(len(str2)!=9)*(len(str3)!=9)*(len(str4)!=9)*(len(str5)!=9)*(len(str6)!=9)*(len(str7)!=9)*(len(str8)!=9)*(len(str9)!=9):
        tkinter.messagebox.showinfo('提示','兄弟，检查一下，你输入有错')
    else:
        tkinter.messagebox.showinfo('提示', '我准备好了，可以开始计算')

def clear():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    E3.delete(0, 'end')
    E4.delete(0, 'end')
    E5.delete(0, 'end')
    E6.delete(0, 'end')
    E7.delete(0, 'end')
    E8.delete(0, 'end')
    E9.delete(0, 'end')

# 求每一行单元格行值域
def valueRange(row):
    temp = copy.deepcopy(row)
    row_value_range = list(range(1,10))
    for i in row:
        if i == '':
            continue
        else:
            if row_value_range.count(i) > 0:
                row_value_range.remove(i)
            else:
                continue
    for j in range(9):
        if temp[j] == '':
            temp[j] = row_value_range
        else:
            temp[j] = [temp[j]]
    return temp

# 求数独每个单元格行值域
def rowValueRange(soduku):
    row_value_range = []
    for row in soduku:
        row_value_range.append(valueRange(row))
    return row_value_range

# 求数独每个单元格列值域
def colValueRange(soduku):
    soduku_invert = [list(i) for i in list(zip(*soduku))]
    temp = rowValueRange(soduku_invert)
    s_column_vrange = [list(i) for i in list(zip(*temp))]
    return s_column_vrange

# 将一个数独数组转化为数独九宫格数组
def matrix_invert(lista):
    listb = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            k = i//3
            l = j//3
            m = k*3 + l
            listb[m].append(lista[i][j])
    return listb

# 求数独每个单元格九宫格值域
def matrixValueRange(soduku):
    matrix = matrix_invert(soduku)
    temp = rowValueRange(matrix)
    matrix_vrange = matrix_invert(temp)
    return matrix_vrange

# 三个列表求交集函数
def inersection(lista,listb,listc):
    tempa = []
    tempb = []
    for i in lista:
        for j in listb:
            if i == j:
                tempa.append(i)
    for k in listc:
        for l in tempa:
            if k == l:
                tempb.append(k)
    return tempb

#  求数独每个单元格总值域
def totalValueRange(soduku):
    row_value_range = rowValueRange(soduku)
    col_value_range = colValueRange(soduku)
    matrix_value_range = matrixValueRange(soduku)
    total_value_range = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            total_value_range[i].append(inersection(row_value_range[i][j],col_value_range[i][j],matrix_value_range[i][j]))
    return total_value_range

# 寻找一行中唯一的值，若该值仅在行值域列表中出现了一次，则其所在单元格取值为该值
def checkUnique(list):
    listb = copy.deepcopy(list)
    templist = []
    for i in listb:
        templist.extend(i)
    for i in range(len(list)):
        for j in list[i]:
            if templist.count(j) == 1:
                listb[i] = [j]
    list = listb
    return list

# 寻找每一行的唯一值，更新值域列表
def row_checkUnique(s_row_vrange):
    temp = []
    for list in s_row_vrange:
        temp.append(checkUnique(list))
    s_row_vrange = temp
    return s_row_vrange

# 检查值域列表每一行、每一列、每一个九宫格的值域，并寻找唯一值，更新值域列表
def soduku_checkUnique(s_row_vrange):
    temp = []
    temp_b = []
    s_row_vrange = row_checkUnique(s_row_vrange)
    for i in list(zip(*s_row_vrange)):# 将数独进行行列转换，然后对每一列进行唯一值检测
        temp.append(list(i))
    temp = row_checkUnique(temp)
    for i in list(zip(*temp)):
        temp_b.append(list(i))
    temp_c = matrix_invert(temp_b)# 将数独进行九宫格转换，然后对每一九宫格进行唯一值检测
    temp_c = row_checkUnique(temp_c)
    temp_d = matrix_invert(temp_c)
    return temp_d

# 将获得的值域列表转化为一个新的数独题目
def generator_soduku(total_value_range):
    soduku = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            if len(total_value_range[i][j]) == 1:
                soduku[i].append(total_value_range[i][j][0])
            else:
                soduku[i].append('')
    return soduku

# 值域列表缩减函数：将值域列表转化为数独题目，求新的数独题目的值域列表，如此反复
def reduce_totalValueRange(soduku):
    for n in range(100):
        total_value_range = totalValueRange(soduku)
        total_value_range = soduku_checkUnique(total_value_range)
        soduku = generator_soduku(total_value_range)
        if total_value_range == totalValueRange(generator_soduku(total_value_range)):
            break
    return total_value_range

# 检查行值域列表是否合法
def row_checkRepeat(s_value_range):
    for i in s_value_range:
        temp = []
        for j in i:
            if len(j) == 1:
                temp.append(j[0])
        len_temp = len(temp)
        if len_temp != len(list(set(temp))):
            return False
    return True

# 检查值域列表是否合法：行检测，列检测，九宫格检测
def soduku_checkRepeat(s_value_range):
    temp_col = list(zip(*s_value_range))
    temp_matrix = matrix_invert(s_value_range)
    return row_checkRepeat(s_value_range) and row_checkRepeat(temp_col) and row_checkRepeat(temp_matrix)

# 计算值域列表取值总的组合数（各单元格值域长度相乘）
def sodukuRate(s_row_vrange):
    rate = 1
    for i in s_row_vrange:
        for j in i:
            rate *= len(j)
    return rate

# 主函数，输入值域列表，如遇到多个取值的单元格，依次尝试值域里的每个值，通过递归的方法检测值是否正确
def trial(total_value_range):
    for i in range(9):
        for j in range(9):
            if len(total_value_range[i][j]) > 1:
                    for k in total_value_range[i][j]:
                        test_value = copy.deepcopy(total_value_range)
                        test_value[i][j] = [k]
                        test_value = reduce_totalValueRange(generator_soduku(test_value))
                        if soduku_checkRepeat(test_value):
                            if sodukuRate(test_value) == 1:
                                return test_value
                            else:    
                                if trial(test_value):
                                    return trial(test_value)
                                else:
                                    continue
                        else:
                            continue
                    return False
            else:
                continue



def jisuan():#输入进txt
    f = open('out.txt', 'w')
    a = reduce_totalValueRange(soduku)
    for i in trial(a):
        print (i,file=f)

def print_result():
    os.system('python sdresult.py')

window = tk.Tk()
window.title("欢迎使用数独计算器，空出为0")
window.geometry('500x300')
lab_1 = tk.Label(window, text="请输入9x9数字:\n(空位以0代替)",font=('隶书',18)).grid(row=0, column=0)
E1 = tk.Entry(window,width=30)
E1.insert(0,"")
E2 = tk.Entry(window,width=30)
E2.insert(0,"")
E3 = tk.Entry(window,width=30)
E3.insert(0,"")
E4 = tk.Entry(window,width=30)
E4.insert(0,"")
E5 = tk.Entry(window,width=30)
E5.insert(0,"")
E6 = tk.Entry(window,width=30)
E6.insert(0,"")
E7 = tk.Entry(window,width=30)
E7.insert(0,"")
E8 = tk.Entry(window,width=30)
E8.insert(0,"")
E9 = tk.Entry(window,width=30)
E9.insert(0,"")

B1 = tk.Button(window, text="确定写入数据", background='#FFF8DC',command=confirm)
B2 = tk.Button(window, text="清除",background='#FFF8DC' ,command=clear)
B3 = tk.Button(window, text="计算",background='#FFF8DC' ,command=jisuan)
B4 = tk.Button(window, text="显示结果",background='#FFF8DC', command=print_result)
E1.grid(row=1,column=1)
E2.grid(row=3,column=1)
E3.grid(row=5,column=1)
E4.grid(row=7,column=1)
E5.grid(row=9,column=1)
E6.grid(row=11,column=1)
E7.grid(row=13,column=1)
E8.grid(row=15,column=1)
E9.grid(row=17,column=1)


B1.grid(row=0,column=1)
B3.grid(row=18,column=0)
B4.grid(row=18,column=1)
B2.grid(row=18,column=2)
#if __name__ == '__main__':


#文本框输入
window.mainloop()