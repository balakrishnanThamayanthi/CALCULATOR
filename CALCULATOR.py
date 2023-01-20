from tkinter import*
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    total= str(eval(expression))
    equation.set(total)
    expression= ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="black")
    gui.geometry("265x125")
    gui.resizable(width=False, height=False)
    equation = StringVar()
    expression_field=Entry(gui,textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    equation.set("Enter your expression")

    button7 =Button(gui, text="7",fg="black",command=lambda:press(7),height=1,width=7).grid(row=2, column=0)
    button8 =Button(gui, text="8",fg="black",command=lambda:press(8),height=1,width=7).grid(row=2, column=1)
    button9 =Button(gui, text="9",fg="black",command=lambda:press(9),height=1,width=7).grid(row=2, column=2)
    add =Button(gui, text="+",fg="black",command=lambda:press("+"),height=1,width=7).grid(row=2, column=3)

    button4 =Button(gui, text="4",fg="black",command=lambda:press(4),height=1,width=7).grid(row=3, column=0)
    button5 =Button(gui, text="5",fg="black",command=lambda:press(5),height=1,width=7).grid(row=3, column=1)
    button6 =Button(gui, text="6",fg="black",command=lambda:press(6),height=1,width=7).grid(row=3, column=2)
    sub =Button(gui, text="-",fg="black",command=lambda:press("-"),height=1,width=7).grid(row=3, column=3)

    button1 =Button(gui, text="1",fg="black",command=lambda:press(1),height=1,width=7).grid(row=4, column=0)
    button2 =Button(gui, text="2",fg="black",command=lambda:press(2),height=1,width=7).grid(row=4, column=1)
    button3 =Button(gui, text="3",fg="black",command=lambda:press(3),height=1,width=7).grid(row=4, column=2)
    mul =Button(gui, text="*",fg="black",command=lambda:press("*"),height=1,width=7).grid(row=4, column=3)

    button0 =Button(gui, text="0",fg="black",command=lambda:press(0),height=1,width=7).grid(row=5, column=0)
    equal =Button(gui, text="=",fg="black",command=equalpress,height=1,width=7).grid(row=5, column=1)
    div =Button(gui, text="/",fg="black",command=lambda:press("/"),height=1,width=7).grid(row=5, column=2)
    clear =Button(gui, text="C",fg="black",command=clear,height=1,width=7).grid(row=5, column=3)

gui.mainloop()
