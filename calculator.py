from tkinter import *

root=Tk()

#--------------------------- Defining title of the projecct ---------------------
root.title("Calculator")
A=0
value =""
operator=""
calin=StringVar()

# ---------------------------Display for the text--------------------------------
d = Entry(root,font=("arial",20, "bold"),textvariable=calin, bd=30, insertwidth=5,
                  bg="light yellow", justify ="right")
d.grid(columnspan=5)

#-------------------------- Defining function of button -------------------------------
def but_click(no):
    global value
    value= value + str(no)
    calin.set(value)

def but_clear():
    global value
    value=""
    d.delete(0,END)

def but_add():
    global value
    global A
    global operator
    A = int(value)
    operator ="+"
    value = value + "+"
    calin.set(value)

def but_sub():
    global value
    global operator
    global A
    A = int(value)
    operator ="-"
    value = value + "-"
    calin.set(value)

def but_div():
    global value
    global operator
    global A
    A = int(value)
    operator ="/"
    value = value + "/"
    calin.set(value)

def but_mul():
    global value
    global operator
    global A
    A = int(value)
    operator ="*"
    value = value + "*"
    calin.set(value)

def but_equal():
    global operator
    global value
    global A
    value2 =value
    if operator == "+":
        ta = int((value2.split("+")[1]))
        save = A + ta
        calin.set(save)
        value = str(save)

    elif operator =="-":
        t = int((value2.split("-")[1]))
        save = A - t
        calin.set(save)
        value = str(save)

    elif operator =="*":
        t = int((value2.split("*")[1]))
        save = A * t
        calin.set(save)
        value = str(save)

    elif operator =="/":
        t = int((value2.split("/")[1]))
        save = A / t
        calin.set(save)
        value = str(save)


#-------------------Button of calulator-------------------------------

btn7 =Button(root,padx=16,pady=16,bd =8 ,fg="black",font=("arial",20,"bold")
             ,text="7",bg="light yellow", command=lambda:but_click(7)).grid(row=1,column=0)

btn8 =Button(root,padx=16 ,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="8",bg="light yellow", command=lambda:but_click(8)).grid(row=1,column=1)

btn9 =Button(root,padx=16 ,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="9",bg="light yellow", command=lambda:but_click(9)).grid(row=1,column=2)

btn4 =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="4",bg="light yellow", command=lambda:but_click(4)).grid(row=2,column=0)

btn5 =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="5",bg="light yellow", command=lambda:but_click(5)).grid(row=2,column=1)

btn6 =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="6",bg="light yellow", command=lambda:but_click(6)).grid(row=2,column=2)

btn1 =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="1",bg="light yellow", command=lambda:but_click(1)).grid(row=3,column=0)

btn2 =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="2",bg="light yellow", command=lambda:but_click(2)).grid(row=3,column=1)

btn3 =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="3",bg="light yellow", command=lambda:but_click(3)).grid(row=3,column=2)

btn0 =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="0",bg="light yellow", command=lambda:but_click(0)).grid(row=4,column=0)

add =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="+",bg="light yellow", command=but_add).grid(row=4,column=1)

sub =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="-",bg="light yellow", command=but_sub).grid(row=4,column=2)

div = Button(root,padx=16,pady=16,bd =8 ,fg="black",font=("arial",20,"bold")
             ,text="÷",bg="light yellow", command=but_div).grid(row=2,column=4)

mul =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="x",bg="light yellow", command=but_mul).grid(row=3,column=4)

equal =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold")
             ,text="=",bg="light yellow",command=but_equal).grid(row=4,column=4)

clear =Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",22,"bold")
             ,text="c",bg="light yellow", command=but_clear).grid(row=1,column=4)

root.mainloop()