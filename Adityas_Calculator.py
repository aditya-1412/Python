from tkinter import *
root=Tk()
root.title("Aditya's Calculator")
icon1= PhotoImage(file = "calculator.png")
root.iconphoto(False,icon1)

func=None
""" Functions Definition Part """
def ins(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,(current+number))
def clear():
    e.delete(0,END)
def add():
    global f1_num
    f1_num=float(e.get())
    e.delete(0,END)
    global func
    func=1
def sub():
    global f1_num
    f1_num=float(e.get())
    e.delete(0,END)
    global func
    func=2
    
def multiply():
    global f1_num
    f1_num=float(e.get())
    e.delete(0,END)
    global func
    func=3
def div():
    global f1_num
    f1_num=float(e.get())
    e.delete(0,END)
    global func
    func=4
def equal():
    if func==1:
        f2_num=float(e.get())
        e.delete(0,END)
        e.insert(0,(f1_num+f2_num))
    if func==2:
        f2_num=float(e.get())
        e.delete(0,END)
        e.insert(0,(f1_num-f2_num))
    if func==3:
        f2_num=float(e.get())
        e.delete(0,END)
        e.insert(0,(f1_num*f2_num))
    if func==4:
        f2_num=float(e.get())
        e.delete(0,END)
        e.insert(0,(f1_num/f2_num))
   
        

#################-----------SCREEN-------------#################################

e=Entry(root,font=("Arial", 20),width=100)
e.grid(row=1,column=1,columnspan=4)

################################################################################

##########################Clear And Equal-To Button##################################

butclear=Button(text="Clear",font=("Arial", 28),padx=43,pady=20,command=clear).grid(row=3,column=1,columnspan=2)
butequal=Button(text="=",padx=79,font=("Arial", 28),pady=20,command=equal).grid(row=3,column=3,columnspan=2)

#####################################################################################

######################Arethmetic Operator############################################

butmul=Button(text="*",font=("Arial", 25),padx=32,pady=20,command=multiply).grid(row=2,column=1)
butdiv=Button(text="/",font=("Arial", 25),padx=32,pady=20,command=div).grid(row=2,column=2)
butadd=Button(text="+",font=("Arial", 25),padx=32,pady=20,command=add).grid(row=2,column=3)
butsub=Button(text="-",font=("Arial", 25),padx=32,pady=20,command=sub).grid(row=2,column=4)

#######################################################################################

###############################Number Pad#############################################

but1=Button(text="1",font=("Arial", 20),padx=33,pady=20,command=lambda:ins("1")).grid(row=4,column=1)
but2=Button(text="2",font=("Arial", 20),padx=32,pady=20,command=lambda:ins("2")).grid(row=4,column=2)
but3=Button(text="3",font=("Arial", 20),padx=34,pady=20,command=lambda:ins("3")).grid(row=4,column=3)
but4=Button(text="4",font=("Arial", 20),padx=32,pady=20,command=lambda:ins("4")).grid(row=4,column=4)

but5=Button(text="5",font=("Arial", 20),padx=33,pady=20,command=lambda:ins("5")).grid(row=5,column=1)
but6=Button(text="6",font=("Arial", 20),padx=32,pady=20,command=lambda:ins("6")).grid(row=5,column=2)
but7=Button(text="7",font=("Arial", 20),padx=34,pady=20,command=lambda:ins("7")).grid(row=5,column=3)
but8=Button(text="8",font=("Arial", 20),padx=32,pady=20,command=lambda:ins("8")).grid(row=5,column=4)

but9=Button(text="9",font=("Arial", 20),padx=33,pady=20,command=lambda:ins("9")).grid(row=6,column=1)
but0=Button(text="0",font=("Arial", 20),padx=32,pady=20,command=lambda:ins("0")).grid(row=6,column=2)
butdec=Button(text=".",font=("Arial", 30),padx=83,pady=9,command=lambda:ins(".")).grid(row=6,column=3,columnspan=2)

########################################################################################
lb1=Label(text="Made With Love From Programmer's Hub",font=("Arial", 15)).grid(row=7,column=1,columnspan=4)
lb1=Label(text="Aditya Sinha",font=("Arial", 15)).grid(row=8,column=1,columnspan=4)
root.mainloop()
