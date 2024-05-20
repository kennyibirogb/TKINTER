from tkinter import * #importing the entire tkinter module
root = Tk() #assigning the main app window to the root variable

import tkinter as tk

root = tk.Tk()
root.title('CALCULATOR')
root.geometry('600x400')

e1 = Entry(root, width = '35', borderwidth ='5', bg ='grey')
e1.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

def calculate(number):
    global current# defining the number buttons
    current = e1.get()
    e1.delete(0, tk.END)
    e1.insert(0,str(current) + str(number))

def clear_btn():
    e1.delete(0, )

def del_btn():
    e1.delete(0, tk.END)

def add_btn():
    first_number = e1.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e1.delete(0, END)

def equal_btn():
    second_number = e1.get()
    s_num =(second_number)
    e1.delete(0, END)
    if math == 'addition':
        e1.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        e1.insert(0, f_num - int(second_number))
    if math == 'divide':
        e1.insert(0, f_num / int(second_number))
    if math == 'multiply':
        e1.insert(0, f_num * int(second_number))
    if math == 'modulus':
        e1.insert(0, f_num % int(second_number))
    if math == 'caret':
        e1.insert(0, f_num ** int(second_number))

        
def minus_btn():
    first_number = e1.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e1.delete(0, END)

def divide_btn():
    first_number = e1.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e1.delete(0, END)

def caret_btn():
    first_number = e1.get()
    global f_num
    global math
    math = 'caret'
    f_num = int(first_number)
    e1.delete(0, END)

def multiply_btn():
    first_number = e1.get()
    global f_num
    global math
    math = 'multiply'
    f_num = int(first_number)
    e1.delete(0, END)

def modulus_btn():
    first_number = e1.get()
    global f_num
    global math
    math = 'modulus'
    f_num = int(first_number)
    e1.delete(0, END)


    
button1 = Button(root, text ='7', padx = 40, pady = 20, command = lambda: calculate(7))
button2 = Button(root, text ='8', padx = 40, pady = 20, command = lambda:calculate(8))
button3 = Button(root, text ='9', padx = 40, pady = 20, command = lambda:calculate(9))
button4 = Button(root, text ='4', padx = 40, pady = 20, command = lambda:calculate(4))
button5 = Button(root, text ='5', padx = 40, pady = 20, command = lambda:calculate(5))
button6 = Button(root, text ='6', padx = 40, pady = 20, command = lambda:calculate(6))
button7 = Button(root, text ='1', padx = 40, pady = 20, command = lambda:calculate(1))
button8 = Button(root, text ='2', padx = 40, pady = 20, command = lambda:calculate(2))
button9 = Button(root, text ='3', padx = 40, pady = 20, command = lambda:calculate(3))
button0 = Button(root, text ='0', padx = 40, pady = 20, command = lambda:calculate(0))
button_add = Button(root, text ='+', padx = 40, pady = 20, fg = 'black', bg ='grey', command =add_btn)
button_minus = Button(root, text ='-', padx = 40, pady = 20, fg = 'black', bg ='grey', command =minus_btn)
button_clear = Button(root, text ='AC', padx = 40, pady = 20, bg = 'red', fg = 'white', command =clear_btn)
button_delete = Button(root, text ='CE', padx = 40, pady = 20, bg ='red', fg = 'white', command = del_btn)
button_modulus = Button(root, text ='%', padx = 40, pady = 20, bg = 'green', fg = 'white', command =modulus_btn)
button_multiply = Button(root, text ='*', padx = 40, pady = 20, fg = 'black', bg ='grey', command =multiply_btn)
button_equal = Button(root, text ='=', padx = 40, pady = 20, fg = 'black', bg = 'grey', command =equal_btn)
button_caret = Button(root, text ='^', padx = 40, pady = 20, fg = 'black',bg ='grey', command =caret_btn)
button_divide = Button(root, text ='/', padx = 40, pady = 20, fg = 'black',bg ='grey', command =divide_btn)


button1.grid(row = 4, column = 0)
button2.grid(row = 4, column = 1)
button3.grid(row = 4, column = 2)

button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)

button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)
button0.grid(row = 5, column = 0)

button_add.grid(row = 4, column = 3) 
button_minus.grid(row = 3, column = 3) 
button_clear.grid(row = 1, column = 0) 
button_delete.grid(row = 1, column = 1)  
button_modulus.grid(row = 1, column = 2) 
button_multiply.grid(row = 2, column = 3) 
button_equal.grid(row = 5, column = 2) 
button_caret.grid(row = 5, column = 1) 
button_divide.grid(row = 1, column = 3) 


root.mainloop()
