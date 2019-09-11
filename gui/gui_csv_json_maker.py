import pathlib
from tkinter import*
import gui_mod_1 as b
root=Tk()
root.title("csv creater")
root.geometry("400x300") #created main window
#working on gui_mod_3 
f_2=Frame(root,height=10,width=300,bg="#186B6A")
f_2.grid(row=0)
f_1=Frame(root,height=50,width=300,bg="#D3D3D3")
f_1.grid(row=1,column=0)#frames created
global fst_lab
fst_lab=StringVar()
fst_lab.set("_")
global lab_1
lab_1=Label(f_1,textvariable=fst_lab)
lab_1.grid(row=2,columnspan=3) #label for 1st click value

lab_2=Label(f_1,text="Enter file name:",bg="#D3D3D3")
lab_2.grid(row=1)
e=Entry(f_1,width=30,borderwidth=5)
e.grid(row=1,column=1,columnspan=3) #get file name segment
# ent_button=Button(f_1,text="OK")
# ent_button.grid(row=1,column=4)

global snd_lab
snd_lab=StringVar()
snd_lab.set("File name:")

 
# global lab_4
# lab_4=Label(f_1,textvariable=snd_lab,bg="#D3D3D3")
# lab_4.grid(row=4,columnspan=3)

# thr_lab=StringVar()
# thr_lab.set("File created")
# lab_3=Label(f_1,textvariable=thr_lab,bg="#D3D3D3")
# lab_3.grid(row=4,column=3) #label that returns file name

create_button=Button(f_1,text="Create",height=1,width=5,bg="gray",command=lambda: b.click(1,fst_lab,snd_lab,e.get()))
create_button.grid(row=3,column=0)
append_button=Button(f_1,text="Edit",height=1,width=5,bg="gray",command=lambda: b.click(2,fst_lab,snd_lab,e.get()))
append_button.grid(row=3,column=1,padx=15)
viw_button=Button(f_1,text="View",height=1,width=5,bg="gray",command=lambda: b.click(3,fst_lab,snd_lab,e.get()))
viw_button.grid(row=3,column=2,padx=15)
#click is sent a number, two string variables and the value in entery bar

root.mainloop()