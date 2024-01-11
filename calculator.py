# Python program to create a simple GUI calculator using Tkinter 
# import everything from tkinter module 
from tkinter import *

# globally declare the expression variable 
exp = "" 

# Function to update expressiom 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global exp 
  
    # concatenation of string 
    exp = exp + str(num) 
  
    # update the expression by using set method 
    equation.set(exp) 
  
  
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(equation.get())) 
  
        equation.set(total) 
  
        # initialze the expression variable 
        # by empty string 
        exp = "" 
  
    # if error is generate then handle 
    # by the except block 
    except: 
  
        equation.set(" error ") 
        exp = "" 
  
  
# Function to clear the contents 
# of text entry box 
def clear(): 
    global exp
    exp = "" 
    equation.set("") 
  
  
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
  
    # set the background colour of GUI window 
    gui.configure(background="white") 
  
    # set the title of GUI window 
    gui.title("Simple Calculator") 
  
    # set the configuration of GUI window 
    # gui.geometry("265x125")
    gui.resizable(0, 0) 
   
  
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 
  
    # create the text entry box for 
    # showing the expression . 
    f2=Frame(gui, bg="silver")
    f2.grid()
    expression_field = Entry(f2, textvariable=equation, font=20) 
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=2, ipadx=114, pady=10, padx=10) 
    f1=Frame(gui, bg="grey")
    f1.grid()
  
     
  
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed .
    #frame the buttons
     
    button1 = Button(f1, text=' 1 ', font="15", fg='black', bg='grey',
                     command=lambda: press(1), height=3, width=10, relief=SUNKEN) 
    button1.grid(row=2, column=0, padx=3, pady=3) 
  
    button2 = Button(f1, text=' 2 ', font="15", fg='black', bg='grey', 
                     command=lambda: press(2), height=3, width=10, relief=SUNKEN) 
    button2.grid(row=2, column=1, padx=3, pady=3) 
  
    button3 = Button(f1, text=' 3 ', font="15", fg='black', bg='grey', 
                     command=lambda: press(3), height=3, width=10, relief=SUNKEN) 
    button3.grid(row=2, column=2, padx=3, pady=3) 
  
    button4 = Button(f1, text=' 4 ', font="15", fg='black', bg='grey', 
                     command=lambda: press(4), height=3, width=10, relief=SUNKEN) 
    button4.grid(row=3, column=0, padx=3, pady=3) 
  
    button5 = Button(f1, text=' 5 ', font="15", fg='black', bg='grey', 
                     command=lambda: press(5), height=3, width=10, relief=SUNKEN) 
    button5.grid(row=3, column=1, padx=3, pady=3) 
  
    button6 = Button(f1, text=' 6 ', font="15", fg='black', bg='grey', 
                     command=lambda: press(6), height=3, width=10, relief=SUNKEN) 
    button6.grid(row=3, column=2, padx=3, pady=3) 
  
    button7 = Button(f1, text=' 7 ', font="15", fg='black', bg='grey', 
                     command=lambda: press(7), height=3, width=10, relief=SUNKEN) 
    button7.grid(row=4, column=0, padx=3, pady=3) 
  
    button8 = Button(f1, text=' 8 ', font="15", fg='black', bg='grey', 
                     command=lambda: press(8), height=3, width=10, relief=SUNKEN) 
    button8.grid(row=4, column=1, padx=3, pady=3) 
  
    button9 = Button(f1, text=' 9 ', font="15", fg='black', bg='grey', 
                     command=lambda: press(9), height=3, width=10, relief=SUNKEN) 
    button9.grid(row=4, column=2, padx=3, pady=3) 
  
    button0 = Button(f1, text=' 0 ', font="15", fg='black', bg='grey', 
                     command=lambda: press(0), height=3, width=10, relief=SUNKEN) 
    button0.grid(row=5, column=0, padx=3, pady=3) 
  
    plus = Button(f1, text=' + ', font="15", fg='black', bg='grey', 
                  command=lambda: press("+"), height=3, width=7, relief=SUNKEN) 
    plus.grid(row=2, column=3, padx=3, pady=3) 
  
    minus = Button(f1, text=' - ', font="15", fg='black', bg='grey', 
                   command=lambda: press("-"), height=3, width=7, relief=SUNKEN) 
    minus.grid(row=3, column=3, padx=3, pady=3) 
  
    multiply = Button(f1, text=' * ', font="15", fg='black', bg='grey', 
                      command=lambda: press("*"), height=3, width=7, relief=SUNKEN) 
    multiply.grid(row=4, column=3, padx=3, pady=3) 
  
    divide = Button(f1, text=' / ', font="15", fg='black', bg='grey', 
                    command=lambda: press("/"), height=3, width=7, relief=SUNKEN) 
    divide.grid(row=5, column=3, padx=3, pady=3) 
  
    equal = Button(f1, text=' = ', font="15", fg='black', bg='grey', 
                   command=equalpress, height=3, width=10, relief=SUNKEN) 
    equal.grid(row=5, column=2, padx=3, pady=3) 
  
    clear = Button(f1, text='Clear', font="15", fg='black', bg='grey', 
                   command=clear, height=3, width=10, relief=SUNKEN) 
    clear.grid(row=5, column='1', padx=3, pady=3) 
  
    # start the GUI 
    gui.mainloop()