#func module for gui_scv_maker
from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
import csv
from datetime import date
from datetime import time
from datetime import datetime
import pathlib
from gui_mod_3 import cell_slect as b
from gui_mod_3 import get_combo as gt
#FIRST CALL CLICK , SECOND DIRECTPATH, THIRD FILECHEK, FORUTH CELLSELECT as b 
def click (nu,v,f,o):
    global s
    if nu==1:
        s="create"
        p="bitch"
        print ("create") #for terminal
        print (o)#file name from entery to print on terminal
        #v.set(s)
        direct_path(o)
        return v.set(s),f.set(p) #returned values of two variables sent back
    elif nu==2:
        s="edit"
        print("edit")
        #v.set(s)
        print (o)
        return v.set(s),f.set(o)
    elif nu==3:
        s="view"
        #v.set(s)
        print("view")
        print (o)
        return v.set(s),f.set(o)

def fle_chk(combo,o):
    path=pathlib.Path(combo)
    if path.exists() == True:
        print("path is valid")
        if path.is_file()== True:
            print("File is created")
            messagebox.showinfo("File status","File "+o+" created at "+combo)
            gt(combo)
            b()
    else:
        print("file mising")

def direct_path(o): #to create a excel file 
    #print("clicked")
    if o !="":
        directory=filedialog.askdirectory()
        global combo
        combo=directory+"/"+o+".csv"
        with open(combo,"w",newline="") as f:
            dt=date.today()
            dte="_"+str(dt)
            nme="File name: "+o
            file_handler=csv.writer (f,delimiter=",")
            file_handler.writerow([dte,nme])
        print(combo)
        fle_chk(combo,o)
        return combo
    else:
        messagebox.showerror("Invalid file name","Please Check file name.")


def cell_sel():
    top=Toplevel()
    top.title("data window")
    top.geometry("250x300")
    fr_1=Frame(top,height=10,width=250,bg="green")
    fr_1.grid(row=0)
    fr_2=Frame(top,height=300,width=250,bg="#D3D3D3")
    fr_2.grid(row=1,column=0)
    counter =IntVar()
    counter.set(0)
    def cell_confirm():
        top.destroy()
        print(counter.get())
        return counter.get()
    def clck_inc():
        counter.set(counter.get()+1)
        print(counter.get())
        
    def clck_dec():
        if counter.get() != 0:
            counter.set(counter.get()-1)
            print(counter.get())
            
        else:
            counter.set(0)
            print("min value")
            messagebox.showerror("Minimum Value Error","Minimum value reached.")
    

    inc_button=Button(fr_2,text="Increase columns",command=clck_inc)
    inc_button.grid(row=1,column=0)
    cnt_lab=Label(fr_2,textvariable=counter,bg="#D3D3D3")
    cnt_lab.grid(row=2,column=0)
    inc_button=Button(fr_2,text="Decrease columns",command=clck_dec)
    inc_button.grid(row=3,column=0)
    cell_confirm_button=Button(fr_2,text="Create",command=cell_confirm)
    cell_confirm_button.grid(row=2,column=1)
    top.mainloop()
if __name__=="__main__":
    cell_sel()