from tkinter import*
from tkinter import messagebox
import csv


def get_combo(combo):
    global combine
    combine= StringVar()
    combine.set(combo)
    print(combo)
    return combine #--> cant get this to next func
#working here
def to_csv(event):
    print(cet.get())
    print(combine.get())#<-- cant get it here

def value_enter(value): 
    coot=Tk()
    coot.title("Value Record")
    coot.geometry("300x250")
    fr_1=Frame(coot,height=10,width=300,bg="light blue")
    fr_1.grid(row=0)
    fr_2=Frame(coot,height=10,width=300,bg="light green")
    fr_2.grid()
    label_1=Label(fr_2,text="Fill "+str(value)+" cells",height=1,width=15, bg="light green")
    label_1.grid(row=0,column=0)
    global cet
    global vrb
    vrb=StringVar()
    vrb.set("-")
    cet=Entry(fr_2,textvariable=vrb,width=15,bg="white")
    cet.bind("<Return>",to_csv)
    cet.grid(row=0,column=1)
    #for i in range(0,value):
           
    coot.mainloop()


def clck(event):
    print(e.get())
    global value 
    value=e.get()    
    try:
        print(int(value)) 
        print(type(value))
        boot.destroy()
        if int(value)!= 0:
            value_enter(int(value))
        return int(value)
    except: ValueError
    messagebox.showerror("Value Error", "Value "+value+" is not valid number.")

def cell_slect():
    global boot
    boot=Tk()
    boot.title("No of cell Inquiry")
    boot.geometry("450x50")

    frme=Frame(boot,height=15,width=400,bg="light green")
    frme.grid(row=0,column=0)

    frme_2=Frame(boot,height=10,width=400,bg="yellow")
    frme_2.grid(row=1,column=0)

    num=IntVar()
    num.set("0")

    global e
    e=Entry(frme_2,width=50,textvariable=num)
    e.bind("<Return>",clck)
    e.grid(row=1,column=0)

    butto_1=Button(frme_2,text="send value",height=1,width=15)
    butto_1.bind("<Button-1>",clck)
    butto_1.grid(row=1,column=1)
    
    boot.mainloop()


if __name__=="__main__":
    from tkinter import*
    from tkinter import messagebox
    #cell_slect()
    get_combo("arsalan")
    print(combine)