from tkinter import *
import datetime

def jiemi():
  d1=datetime.datetime.now()
  p=varin.get()
  for a in range(33,127):
    for b in range(33,127):
      for c in range(33,127):
        for d in range(33,127):
          s=chr(a)+chr(b)+chr(c)+chr(d)
          if s==p:
            d2=datetime.datetime.now()
            d=d2-d1
            varout.set(str(d.seconds)+"秒"+str(d.microseconds/1000)+"毫秒")
            return 0      #起结束函数运行的作用

root=Tk()
root.title("破解超级密码")
root.geometry('300x100')
frm = Frame(root)
frm_L = Frame(frm)
Label(frm_L, text='输入密码：', font=('Arial', 10)).pack()
Label(frm_L, text='破解用时：', font=('Arial', 10)).pack()
frm_L.pack(side=LEFT)
frm_R = Frame(frm)
varin=StringVar()
varout=StringVar()
Entry(frm_R, textvariable = varin).pack()
Entry(frm_R, textvariable = varout).pack()
frm_R.pack(side=RIGHT)
frm.pack()
Button(root, text="破解", command=jiemi,relief="solid",width=10).pack()
root.mainloop()
