from tkinter import *
from operator import mul,add,sub
import tkinter.ttk as ttk

f_num = None
sign = None

icon_path='c:/Users/HP/Desktop/PracticePython/Calculator/Dtafalonso-Android-Lollipop-Calculator.ico"

root = Tk()
root.title("Simple Calculator")
root.iconbitmap(icon_path)


ent = Entry(root,width=30,borderwidth=10)
ent.grid(row=0,column=0,columnspan=3)

def click(num):
    current = ent.get()
    ent.delete(0,END)
    ent.insert(0, str(current) + str(num))

def act(what):
    first_num = ent.get()
    global f_num
    global sign
    sign = what
    f_num = int(first_num)
    ent.delete(0,END)

def equal():
    second_num = ent.get()
    ent.delete(0,END)
    if sign == "+":
        ent.insert(0 , add(f_num,int(second_num)))
    if sign == "-":
        ent.insert(0 , sub(f_num,int(second_num)))
    if sign == "*":
        ent.insert(0 , mul(f_num,int(second_num)))
    if sign == "=":
        ent.insert(0 , f_num + int(second_num))

def button(num,ro,colu):
    my_button = Button(root,text=num,padx=25,pady=15,font=("Times", 15, "bold"),borderwidth=5,command=lambda : click(num),background="#C2C2C2")
    my_button.grid(row=ro,column=colu)

button(7,1,0)
button(8,1,1)
button(9,1,2)

button(4,2,0)
button(5,2,1)
button(6,2,2)

button(1,3,0)
button(2,3,1)
button(3,3,2)

button(0,4,0)

#clear button 
clear_button = Button(root,text="Clear",padx=55,pady=20,borderwidth=5,font=(20),background="#46FD9F",command=lambda : ent.delete(0,END))
clear_button.grid(row=4,column=1,columnspan=2)
#add button
add_button = Button(root,text="+",padx=25,pady=15,borderwidth=5,font=(20),background="#FEB204",command=lambda:act("+"))
add_button.grid(row=5,column=0)
#sub button
add_button = Button(root,text="-",padx=25,pady=15,borderwidth=5,font=(20),background="#FEB204",command=lambda:act("-"))
add_button.grid(row=6,column=0)
#mul button
add_button = Button(root,text="*",padx=25,pady=15,borderwidth=5,font=(20),background="#FEB204",command=lambda:act("*"))
add_button.grid(row=6,column=1)
#Division button
add_button = Button(root,text="/",padx=25,pady=15,borderwidth=5,font=(20),background="#FEB204",command=lambda:act("/"))
add_button.grid(row=6,column=2)
#Equal button 
equal_button = Button(root,text="=",padx=60,pady=15,borderwidth=5,font=(20),background="#FEB204",command=equal)
equal_button.grid(row=5,column=1,columnspan=2)

root.mainloop()
