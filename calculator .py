from tkinter import*
root=Tk()
root.title("my calcoo")
root.geometry("290x210")

e=Entry(root,width=40,borderwidth=15)
e.grid(row=0,column=0,columnspan=3)
def butto_click(number):
    num=e.get()
    e.delete(0,END)
    #e.delete(0,END)
    e.insert(0,str(num)+ str(number))

def frac():
    num=e.get()
    e.delete(0,END)
    e.insert(-1,str(num)+".")

def clr_scr():
    e.delete(0,END)

def func_cal(sign):
    def minus ():
        f_num=e.get()
        global fir
        global s
        s="min"
        fir=float(f_num)
        e.delete(0,END)
        print(fir)
    def add():
        f_num=e.get()
        global fir
        global s
        s="add"
        fir=float(f_num)
        e.delete(0,END)
        print(fir)
    def multi():
        f_num=e.get()
        global fir
        global s
        s="multi"
        fir=float(f_num)
        e.delete(0,END)
        print(fir)
    def div():
        f_num=e.get()
        global fir
        global s
        s="div"
        fir=float(f_num)
        e.delete(0,END)
        print(fir)
    def equal():
        s_num=e.get()
        e.delete(0,END)
        if s=="add":
            e.insert(0,float(s_num)+float(fir))
            print(float(s_num)+float(fir))
        elif s=="min":
            e.insert(0,float(fir)-float(s_num))
            print(float(fir)-float(s_num))
        elif s=="div":
            e.insert(0,float(fir)/float(s_num))
            print(float(fir)/float(s_num))
        elif s=="multi":
            e.insert(0,float(s_num)*float(fir))
            print(float(s_num)*float(fir))


    if sign=="-":
        minus()
    elif sign=="+":
        add()
    elif sign=="x":
        multi()
    elif sign=="/":
        div()
    elif sign=="eq":
        equal()
    

butto_1=Button(root,text="1",width=10,height=1,bg="GRAY",command=lambda: butto_click(1)).grid(row=1,column=0)
butto_2=Button(root,text="2",width=10,height=1,bg="GRAY",command=lambda: butto_click(2)).grid(row=1,column=1)
butto_3=Button(root,text="3",width=10,height=1,bg="GRAY",command=lambda: butto_click(3)).grid(row=1,column=2)

butto_4=Button(root,text="4",width=10,height=1,bg="GRAY",command=lambda: butto_click(4)).grid(row=2,column=0)
butto_5=Button(root,text="5",width=10,height=1,bg="GRAY",command=lambda: butto_click(5)).grid(row=2,column=1)
butto_6=Button(root,text="6",width=10,height=1,bg="GRAY",command=lambda: butto_click(6)).grid(row=2,column=2)

butto_7=Button(root,text="7",width=10,height=1,bg="GRAY",command=lambda: butto_click(7)).grid(row=3,column=0)
butto_8=Button(root,text="8",width=10,height=1,bg="GRAY",command=lambda: butto_click(8)).grid(row=3,column=1)
butto_9=Button(root,text="9",width=10,height=1,bg="GRAY",command=lambda: butto_click(9)).grid(row=3,column=2)
butto_0=Button(root,text="0",width=10,height=1,bg="GRAY",command=lambda: butto_click(0)).grid(row=4,column=1)

butto_clear=Button(root,text="CLR",width=10,height=1,bg="GRAY",command= clr_scr).grid(row=4,column=2)
butto_minus=Button(root,text="-",width=10,height=1,bg="GRAY",command=lambda: func_cal("-")).grid(row=4,column=0)
butto_add=Button(root,text="+",width=10,height=1,bg="GRAY",command=lambda: func_cal("+")).grid(row=5,column=1)
butto_multi=Button(root,text="x",width=10,height=1,bg="GRAY",command=lambda: func_cal("x")).grid(row=5,column=0)
butto_divide=Button(root,text="/",width=10,height=1,bg="GRAY",command=lambda: func_cal("/")).grid(row=5,column=2)
butto_equal=Button(root,text="=",width=25,height=1,bg="GRAY",command=lambda: func_cal("eq")).grid(row=6,column=0,columnspan=2)
butto_frac=Button(root,text=".",width=10,height=1,bg="GRAY",command=frac).grid(row=6,column=2)
root.resizable(height = 0, width = 0)
root.mainloop()

