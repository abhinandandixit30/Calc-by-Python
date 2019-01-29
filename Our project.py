#Libraries used


import tkinter
from math import *
import math
from tkinter import *

#Code for input, output and operations performed


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)


    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "mul":
            self.total *= self.current
        if self.op == "div":
            self.total /= self.current
        if self.op == "pow":
            self.total = self.total ** self.current
        if self.op == "sqrt":
            self.total = self.total ** (1/self.current)
        if self.op == "fact":
            self.total=int(text_box.get())
            self.total=math.factorial(self.total)
        if self.op == "exp":
            self.total = math.exp(self.total)
        if self.op == "inv":
            self.total = 1/self.total
        if self.op == "abs":
            self.total = math.fabs(self.total)
        if self.op == "floor":
            self.total = math.floor(self.total)
        if self.op == "ceil":
            self.total = math.ceil(self.total)        
        self.new_num = True
        self.op_pending = False
        self.display(self.total)
        

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False
        
    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)
        
    def tau(self):
        self.result=False
        self.current=math.tau
        self.display(self.current)

    def sin(self):
         self.result=False
         self.current=math.sin(math.radians(float(text_box.get.get())))
         self.dispaly(self.current)                                  

    def cos(self):
         self.result=False
         self.current=math.cos(math.radians(float(text_box.get.get())))
         self.dispaly(self.current)

    def tan(self):
         self.result=False
         self.current=math.tan(math.radians(float(text_box.get())))
         self.dispaly(self.current)

    def asinh(self):
         self.result=False
         self.current=math.asinh(math.radians(float(text_box.get.get())))
         self.dispaly(self.current)                                  

    def acosh(self):
         self.result=False
         self.current=math.acosh(math.radians(float(text_box.get.get())))
         self.dispaly(self.current)

    def atanh(self):
         self.result=False
         self.current=math.atanh(math.radians(float(text_box.get())))
         self.dispaly(self.current)

    def log(self):
         self.result=False
         self.current=math.log(math.radians(float(text_box.get())))
         self.dispaly(self.current)

    def log10(self):
         self.result=False
         self.current=math.log10(math.radians(float(text_box.get())))
         self.dispaly(self.current)     

    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)
    
#Code for layout(G.U.I)

        
sum1=Calc()
calc=tkinter.Tk()
top=Frame(calc)
calc.title("Calculator")
top.grid()
text_box=tkinter.Entry(top,justify=RIGHT,width=30,font="Times 16 bold")
text_box.grid(row=1,column=1,columnspan=7,pady=10,padx=10)
text_box.insert(0,"0")
text_box.focus()


inv=tkinter.Button(top,text="inv",bg="red",padx=10,pady=10,width=7,height=2,)
inv["command"] = lambda:sum1.operation("inv")
inv.grid(row=2,column=1,padx=1, pady =1)


sin=tkinter.Button(top,text="sin",bg="red",padx=10,pady=10,width=7,height=2)
sin["command"] = lambda:sum1.sin()
sin.grid(row=3,column=1,padx=1, pady =1)


asin=tkinter.Button(top,text="asinh",bg="red",padx=10,pady=10,width=7,height=2)
asin["command"] = lambda:sum1.asinh()
asin.grid(row=4,column=1,padx=1, pady =1)


pow0=tkinter.Button(top,text="pow",bg="red",padx=10,pady=10,width=7,height=2)
pow0["command"] = lambda:sum1.operation("pow")
pow0.grid(row=5,column=1,padx=1, pady =1)


ceil0=tkinter.Button(top,text="ceil",bg="red",padx=10,pady=10,width=7,height=2)
ceil0["command"] = lambda:sum1.operation("ceil")
ceil0.grid(row=6,column=1,padx=1, pady =1)


log=tkinter.Button(top,text="Log10",bg="red",padx=10,pady=10,width=7,height=2)
log["command"] = lambda:sum1.log10()
log.grid(row=2,column=2,padx=1, pady =1)


cos=tkinter.Button(top,text="cos",bg="red",padx=10,pady=10,width=7,height=2)
cos["command"] = lambda:sum1.cos()
cos.grid(row=3,column=2,padx=1, pady =1)


acos=tkinter.Button(top,text="acosh",bg="red",padx=10,pady=10,width=7,height=2)
acos["command"] = lambda:sum1.acosh()
acos.grid(row=4,column=2,padx=1, pady =1)


exp=tkinter.Button(top,text="exp",bg="red",padx=10,pady=10,width=7,height=2)
exp["command"] = lambda:sum1.operation("exp")
exp.grid(row=5,column=2,padx=1, pady =1)


floor=tkinter.Button(top,text="floor",bg="red",padx=10,pady=10,width=7,height=2)
floor["command"] = lambda:sum1.operation("floor")
floor.grid(row=6,column=2,padx=1, pady =1)


b0=tkinter.Button(top,text="ln",bg="red",padx=10,pady=10,width=7,height=2)
b0["command"] = lambda:sum1.log()
b0.grid(row=2,column=3,padx=1, pady =1)


tan=tkinter.Button(top,text="tan",bg="red",padx=10,pady=10,width=7,height=2)
tan["command"] = lambda:sum1.tan()
tan.grid(row=3,column=3,padx=1, pady =1)


atan=tkinter.Button(top,text="atanh",bg="red",padx=10,pady=10,width=7,height=2)
atan["command"] = lambda:sum1.atanh()
atan.grid(row=4,column=3,padx=1, pady =1)


abs0=tkinter.Button(top,text="abs",bg="red",padx=10,pady=10,width=7,height=2)
abs0["command"] = lambda:sum1.operation("abs")
abs0.grid(row=5,column=3,padx=1, pady =1)


comma=tkinter.Button(top,text="sqrt",bg="red",padx=10,pady=10,width=7,height=2)
comma["command"] = lambda:sum1.operation("sqrt")
comma.grid(row=6,column=3,padx=1, pady =1)


_7  =tkinter.Button(top,text="7",bg="white",padx=10,pady=10,width=7,height=2)
_7["command"] = lambda:sum1.num_press(7)
_7.grid(row=3,column=4,padx=1, pady =1)


_4=tkinter.Button(top,text="4",bg="white",padx=10,pady=10,width=7,height=2)
_4["command"] = lambda:sum1.num_press(4)
_4.grid(row=4,column=4,padx=1, pady =1)


_1=tkinter.Button(top,text="1",bg="white",padx=10,pady=10,width=7,height=2)
_1["command"] = lambda:sum1.num_press(1)
_1.grid(row=5,column=4,padx=1, pady =1)


_0=tkinter.Button(top,text="0",bg="white",padx=10,pady=10,width=18,height=2)
_0["command"] = lambda:sum1.num_press(0)
_0.grid(row=6,column=4,padx=1, pady =1,columnspan=2)


fact=tkinter.Button(top,text="!",bg="yellow",padx=10,pady=10,width=7,height=2)
fact["command"] = lambda:sum1.operation("fact")
fact.grid(row=2,column=6,padx=1, pady =1)


clear=tkinter.Button(top,text="clear",bg="red",padx=10,pady=10,width=18,height=2)
clear["command"] = lambda:sum1.clear()
clear.grid(row=2,column=4,padx=1, pady =1,columnspan=2)


_8=tkinter.Button(top,text="8",bg="white",padx=10,pady=10,width=7,height=2)
_8["command"] = lambda:sum1.num_press(8)
_8.grid(row=3,column=5,padx=1, pady =1)


_5=tkinter.Button(top,text="5",bg="white",padx=10,pady=10,width=7,height=2)
_5["command"] = lambda:sum1.num_press(5)
_5.grid(row=4,column=5,padx=1, pady =1)


_2=tkinter.Button(top,text="2",bg="white",padx=10,pady=10,width=7,height=2)
_2["command"] = lambda:sum1.num_press(2)
_2.grid(row=5,column=5,padx=1, pady =1)


_9=tkinter.Button(top,text="9",bg="white",padx=10,pady=10,width=7,height=2)
_9["command"] = lambda:sum1.num_press(9)
_9.grid(row=3,column=6,padx=1, pady =1)


_6=tkinter.Button(top,text="6",bg="white",padx=10,pady=10,width=7,height=2)
_6["command"] = lambda:sum1.num_press(6)
_6.grid(row=4,column=6,padx=1, pady =1)


_3=tkinter.Button(top,text="3",bg="white",padx=10,pady=10,width=7,height=2)
_3["command"] = lambda:sum1.num_press(3)
_3.grid(row=5,column=6,padx=1, pady =1)


b2=tkinter.Button(top,text=".",bg="yellow",padx=10,pady=10,width=7,height=2)
b2["command"] = lambda:sum1.num_press(".")
b2.grid(row=6,column=6,padx=1, pady =1)


add=tkinter.Button(top,text="+",bg="yellow",padx=10,pady=10,width=7,height=2)
add["command"] = lambda:sum1.operation("add")
add.grid(row=2,column=7,padx=1, pady =1)


sub=tkinter.Button(top,text="-",bg="yellow",padx=10,pady=10,width=7,height=2)
sub["command"] = lambda:sum1.operation("sub")
sub.grid(row=3,column=7,padx=1, pady =1)


div=tkinter.Button(top,text="/",bg="yellow",padx=10,pady=10,width=7,height=2)
div["command"] = lambda:sum1.operation("div")
div.grid(row=4,column=7,padx=1, pady =1)


mul=tkinter.Button(top,text="*",bg="yellow",padx=10,pady=10,width=7,height=2)
mul["command"] = lambda:sum1.operation("mul")
mul.grid(row=5,column=7,padx=1, pady =1)


equal=tkinter.Button(top,text="=",bg="skyblue",padx=10,pady=10,width=18,height=2)
equal["command"]=lambda:sum1.calc_total()
equal.grid(row=6,column=7,padx=1, pady =1,columnspan=2)


ac=tkinter.Button(top,text="AC",bg="skyblue",padx=10,pady=10,width=7,height=2)
ac["command"] = lambda:sum1.all_clear()
ac.grid(row=2,column=8,padx=1, pady =1)


per=tkinter.Button(top,text="2pi",bg="yellow",padx=10,pady=10,width=7,height=2)
per["command"] = lambda:sum1.tau()
per.grid(row=3,column=8,padx=1, pady =1)


int_div=tkinter.Button(top,text="pi",bg="yellow",padx=10,pady=10,width=7,height=2)
int_div["command"] = lambda:sum1.pi()
int_div.grid(row=4,column=8,padx=1, pady =1)


d_mul=tkinter.Button(top,text="**",bg="yellow",padx=10,pady=10,width=7,height=2)
d_mul["command"] = lambda:sum1.operation("pow")
d_mul.grid(row=5,column=8,padx=1, pady =1)


top.mainloop()


    
    
