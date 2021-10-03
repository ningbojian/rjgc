from tkinter import *
root=Tk()


def getnum():
    print(En0.get())

En0=Entry(root).grid(row=0,column=1)
En1=Entry(root).grid(row=0,column=2)
En2=Entry(root).grid(row=0,column=3)
En3=Entry(root).grid(row=2,column=1)
En4=Entry(root).grid(row=2,column=2)
En5=Entry(root).grid(row=2,column=3)
En6=Entry(root).grid(row=3,column=1)
En7=Entry(root).grid(row=3,column=2)
En8=Entry(root).grid(row=3,column=3)
Button(root,text='确定',anchor='c',width=6,height=1,command=getnum()).grid(row=4,column=1)

root.mainloop()

