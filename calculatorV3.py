#IMPORTING...........................
from tkinter import *

mtk = Tk()

mtk.iconbitmap('calcu_icon.ico')#setting icon

global expression
global result
expression = "" 

#TITLE...........................
mtk.title("CALCULATOR")

#DEFINING STRINGVAR...........................
var = StringVar()
var.set("")
v = IntVar()

#DETERMINING DIMENSION...........................
def window_seting(width, height):
    window_width = width
    window_height = height
    screen_width = mtk.winfo_screenwidth()
    screen_height = mtk.winfo_screenheight()
    x_co = (screen_width/2) - (window_width/2)
    y_co = (screen_height/2) - (window_height/2)
    mtk.geometry("%dx%d+%d+%d" % (window_width,window_height,x_co,y_co))
    mtk.resizable(width=False ,height=False)
    
window_seting(300,470)

# DEFINING A FEW FUNCTIONS...........................
def display_grid():
    open_bracket.grid(row = 0, column = 0)
    closed_bracket.grid(row = 0, column = 1)
    square.grid(row = 0, column = 2)
    square_root.grid(row = 0, column = 3)

    button_9.grid(row = 1, column = 0)
    button_8.grid(row = 1, column = 1)
    button_7.grid(row = 1, column = 2)
    addition.grid(row = 1, column = 3)

    button_6.grid(row = 2, column = 0)
    button_5.grid(row = 2, column = 1)
    button_4.grid(row = 2, column = 2)
    subtraction.grid(row = 2, column = 3)

    button_3.grid(row = 3, column = 0)
    button_2.grid(row = 3, column = 1)
    button_1.grid(row = 3, column = 2)
    multiplication.grid(row = 3, column = 3)

    button_0.grid(row = 4, column = 0)
    equat_button.grid(row = 4, column = 1)
    clear_button.grid(row = 4, column = 2)
    division.grid(row = 4, column = 3)

    del_button.grid(row = 5 , column = 0)

def en_dis(x):
    del_button.config(state = x)
    
    open_bracket.config(state = x)
    closed_bracket.config(state = x)
    square.config(state = x)
    square_root.config(state = x)

    button_9.config(state = x)
    button_8.config(state = x)
    button_7.config(state = x)
    addition.config(state = x)

    button_6.config(state = x)
    button_5.config(state = x)
    button_4.config(state = x)
    subtraction.config(state = x)

    button_3.config(state = x)
    button_2.config(state = x)
    button_1.config(state = x)
    multiplication.config(state = x)

    button_0.config(state = x)
    equat_button.config(state = x)
    clear_button.config(state = x)
    division.config(state = x)

def edit_num(exp):
    global expression
    expression += str(exp)
    var.set(expression)

def evalu(exp) :
    global expression
    global result
    if exp is '=':
        result = eval(expression)
        var.set(result)
        expression = ''
    if exp is 'c':
        expression = ''
        var.set(expression)
    if exp is '<':
        expression = expression[:-1]
        var.set(expression)
        
def calType():
    valuerad = v.get()
    if valuerad == 1:
        en_dis("normal")
    if valuerad == 2:
        en_dis("disabled")

# DEFINING LABLES...........................
frame_1 = LabelFrame(mtk,text = 'Calculator Type')

radio1 = Radiobutton(frame_1,
                     text ="Basic",
                     width = 17,
                     variable = v,
                     value = 1,
                     command = calType
                     ).grid(row = 0, column = 0)

radio2 = Radiobutton(frame_1,
                     text ="Scientific",
                     width = 17,
                     variable = v,
                     value = 2,
                     command = calType
                     ).grid(row = 0, column = 1)

label1 = Label(mtk,
               width = 40,
               height = 2,
               bd=10,
               relief="ridge",
               textvariable = var,
               font = "Times 10 bold italic",
               bg = 'lightgray',
               fg = "black",
               anchor = E
               )
num_pad = Frame(mtk)
# DEFINING BUTTONS...........................
del_button = Button(num_pad,
                      width = 3,
                      height = 1,
                      padx = 3,
                      pady = 3,
                      bd=5,
                      relief="ridge",
                      text = '<--',
                      font = "Times 20 bold italic",
                      command = lambda:evalu('<'),
                      )

equat_button = Button(num_pad,
                      width = 3,
                      height = 1,
                      padx = 3,
                      pady = 3,
                      bd=5,
                      relief="ridge",
                      text = '=',
                      font = "Times 20 bold italic",
                      command = lambda:evalu('='),
                      #
                      )
#_________________________________________
clear_button = Button(num_pad,
                      width = 3,
                      height = 1,
                      padx = 3,
                      pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "C",
                      font = "Times 20 bold italic",
                      command = lambda:evalu('c'),
                      #
                      )
#_________________________________________
button_0 = Button(num_pad,
                  width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                  bd=5,
                  relief="ridge",
                  text = "0",
                  font = "Times 20 bold italic",
                  command = lambda:edit_num(0),
                  #
                  )
#_________________________________________
button_1 = Button(num_pad,
                  width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                  bd=5,
                  relief="ridge",
                  text = "1",
                  font = "Times 20 bold italic",
                  command = lambda:edit_num(1),
                  #
                  )
#_________________________________________
button_2 = Button(num_pad,
                   width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "2",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num(2),
                  #
                      )
#_________________________________________
button_3 = Button(num_pad,
                   width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "3",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num(3),
                  #
                      )
#_________________________________________
button_4 = Button(num_pad,
                   width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "4",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num(4),
                  #
                      )
#_________________________________________
button_5 = Button(num_pad,
                   width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "5",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num(5),
                  #
                      )
#_________________________________________
button_6 = Button(num_pad,
                   width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "6",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num(6),
                  #
                      )
#_________________________________________
button_7 = Button(num_pad,
                   width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "7",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num(7),
                  #
                      )
#_________________________________________
button_8 = Button(num_pad,
                   width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "8",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num(8),
                  #
                      )
#_________________________________________
button_9 = Button(num_pad,
                  width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "9",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num(9),
                  #
                      )
#_________________________________________
addition = Button(num_pad,
                  width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "+",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num('+'),
                  #
                      )
#_________________________________________
subtraction = Button(num_pad,
                      width = 3,
                      height = 1,
                      padx = 3,
                      pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "-",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num('-'),
                     #
                      )
#_________________________________________
multiplication = Button(num_pad,
                      width = 5,
                        height = 2,
                      padx = 3,
                      pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "X",
                      font = "Times 13 bold italic",
                      command = lambda:edit_num('*'),
                    #
                      )
#_________________________________________
division = Button(num_pad,
                  width = 3,
                  height = 1,
                  padx = 3,
                  pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "/",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num('/'),
                  #
                      )
#_________________________________________
open_bracket = Button(num_pad,
                      width = 3,
                      height = 1,
                      padx = 3,
                      pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "(",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num('('),
                      #
                      )
#_________________________________________
closed_bracket = Button(num_pad,
                      width = 3,
                      height = 1,
                      padx = 3,
                      pady = 3,
                      bd=5,
                      relief="ridge",
                      text = ")",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num(')'),
                      #
                      )
#_________________________________________
square = Button(num_pad,
                      width = 3,
                      height = 1,
                      padx = 3,
                      pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "sq",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num('**2'),
                      #
                      )
#_________________________________________
square_root = Button(num_pad,
                      width = 3,
                      height = 1,
                      padx = 3,
                      pady = 3,
                      bd=5,
                      relief="ridge",
                      text = "sqrt",
                      font = "Times 20 bold italic",
                      command = lambda:edit_num('**(1/2)'),
                      #
                      )
#_________________________________________
#ARRANGING THE LISTS AND BUTTONS
frame_1.grid(row = 0 , column = 0)
label1.grid(row = 1, column = 0)
num_pad.grid(row = 2, column = 0)

display_grid()
en_dis("disabled")

#loop #end#  
mtk.mainloop()
