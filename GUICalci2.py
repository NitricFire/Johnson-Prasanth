import tkinter as tk
import math as math
window =tk.Tk()
window.title("My calculator")
window.geometry("300x400")
entry = tk.Entry(window, width = 25, font =("Arial 13"))
entry.place(x=40, y =50)
operand1 = ''
operand2 = ''
operation = ''

def new_entry(number):
    new_value = entry.get()
    new_value += number
    entry.delete(0,'end')
    entry.insert(0,new_value)

def clear_display(): 
    global operation
    operation=""
    entry.set("")

def oper(op):
    global operand1,operation
    operand1 = entry.get()
    operation = op
    entry.delete(0, 'end')

def ans():
    global operand1,operand2,operation
    operand2 = entry.get()
    entry.delete(0,'end')
    if operation == '+':
        result = int(operand1) + int(operand2)
    if operation == '-':
        result = int(operand1) - int(operand2)
    if operation == '%':
        result = (int(operand1)*int(operand2))/100
    if operation == '*':
        result = int(operand1)*int(operand2)
    if operation == "C":
        result= clear_display()
    if operation == "√":
        result = math.sqrt(int(operand1))
    if operation == "x²":
        result = int(operand1)*int(operand1)
    if operation == "1/x":
        result = 1/int(operand1)
    if operation == "Sin":
        result = (math.sin(int(operand1)))
    if operation == "Cos":
        result = (math.cos(int(operand1)))
    if operation == "Tan":
        result = (math.tan(int(operand1)))
    if operation == "n!":
        result = (math.factorial(int(operand1)))
    if operation == "/":
        result = int(operand1)/int(operand2)
    entry.insert(0,result)


button1=tk.Button(window, text="7",foreground="black",command= lambda : new_entry("7"), background="light blue",width=2)
button1.place(x=40, y=150)

button2=tk.Button(window, text="8",foreground="black",command= lambda : new_entry("8"), background="light blue",width=2)
button2.place(x=90, y=150)

button3=tk.Button(window, text="9",foreground="black",command= lambda : new_entry("9"), background="light blue",width=2)
button3.place(x=140, y=150)

button4=tk.Button(window, text="+",foreground="black", command= lambda : oper('+'), background="light blue",width=2)
button4.place(x=190, y=150)

button5=tk.Button(window, text="%",foreground="black", command = lambda : oper('%'), background="light blue",width=2)
button5.place(x=40, y=100)

button6=tk.Button(window, text="4",foreground="black",command= lambda : new_entry("4"), background="light blue",width=2)
button6.place(x=40, y=200)

button7=tk.Button(window, text="5",foreground="black",command= lambda : new_entry("5"), background="light blue",width=2)
button7.place(x=90, y=200)

button8=tk.Button(window, text="6",foreground="black",command= lambda : new_entry("6"), background="light blue",width=2)
button8.place(x=140, y=200)

button9=tk.Button(window,text="n!",foreground="black",command=lambda:oper("n!"),background="light blue",width=2)
button9.place(x=190, y=200)

button10=tk.Button(window,text="/",foreground="black",command=lambda:oper("/"),background="light blue",width=2)
button10.place(x=90, y=100)

button11=tk.Button(window, text="1",foreground="black", command= lambda : new_entry("1"), background="light blue",width=2)
button11.place(x=40, y=250)

button12=tk.Button(window, text="2",foreground="black", command= lambda : new_entry("2"), background="light blue",width=2)
button12.place(x=90, y=250)

button13=tk.Button(window,text='1/x',foreground='black',command=lambda:oper("1/x"),background="light blue",width=2)
button13.place(x=140,y=100)

buttonP=tk.Button(window, text="3",foreground="black",command= lambda : new_entry("3"), background="light blue",width=2)
buttonP.place(x=140, y=250)

buttonS=tk.Button(window, text="-",foreground="black", command= lambda : oper('-'), background="light blue",width=2)
buttonS.place(x=190, y=250)

button14=tk.Button(window, text='*',foreground='black',command=lambda:oper('*'), background="light blue",width=2)
button14.place(x=40,y=300)

button15=tk.Button(window,text='0',foreground="black",command= lambda : new_entry("0"), background="light blue",width=2)
button15.place(x=90,y=300)

button16=tk.Button(window,text='√',foreground='black',command=lambda:oper("√"),background="light blue",width=2)
button16.place(x=140,y=300)

button17=tk.Button(window, text="=",foreground="black",command=ans, background="light blue",width=9)
button17.place(x=190,y=300)

button18=tk.Button(window,text='x²',foreground='black',command= lambda:oper("x²"),background="light blue",width=2)
button18.place(x=190,y=100)

button19=tk.Button(window,text="Sin",foreground='black',command=lambda:oper("Sin"),background="light blue",width=2)
button19.place(x=240,y=200)

button20=tk.Button(window,text="Cos",foreground="black",command=lambda:oper("Cos"),background="light blue",width=2)
button20.place(x=240,y=250)

button22=tk.Button(window,text="Tan",foreground="black",command=lambda:oper("Tan"),background="light blue",width=2)
button22.place(x=240,y=150)

button23=tk.Button(window, text="C",foreground="black",command= lambda : oper("C"), background="light blue",width=2)
button23.place(x=240,y=100)

window.mainloop()