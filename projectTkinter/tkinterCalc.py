# Paul van Sittert 24.3.23
from tkinter import *

# Set up var
calculatorString = ""
answerNum=0
bracket=0 #How deep inside the brackets the user is


# Define functions

def addString(string):
    global calculatorString
    newString = calculatorString[:len(calculatorString)-bracket] + string + calculatorString[len(calculatorString)-bracket:]
    calculatorString = newString
    outputString()

def openBracket():
    global calculatorString
    global bracket
    addString("()")
    bracket +=1

def closeBracket():
    global bracket

    if bracket >0:
        bracket -=1

def backSpace():
    global calculatorString
    calculatorString = calculatorString[:-1]
    outputString()

def clearString():
    global calculatorString
    calculatorString = ""
    answerNum = 0
    outputString()


def calcInput():
    global calculatorString
    global answerNum
    try:
        answerNum = eval(calculatorString)
        calculatorString = calculatorString + " = " + str(answerNum)
        outputString()
    except:
        calculatorString = "Invalid Calculation"
        outputString()

    calculatorString = ""


def outputString():
    output_Label.config(text=calculatorString)


# Set up gui
root = Tk()
root.title("My calculator")
root.config(bg="grey")

# Set up frames
output_frame = Frame(root, width=100, height=50)
output_frame.grid(row=0, column=0, padx=10, pady=10)

output_Label = Label(output_frame, text="", width=100, anchor="e", justify=RIGHT, padx=10)
output_Label.pack()

button_Menu = Frame(root, width=100, height=400)
button_Menu.grid(row=1, column=0, padx=10, pady=10)

# Set up buttons
filler1_lable = Label(button_Menu, width=10)
filler1_lable.grid(row=0, column=0)

filler2_lable = Label(button_Menu, width=10)
filler2_lable.grid(row=0, column=6)

button1 = Button(button_Menu, text="   1   ", command=lambda arg1="1": addString(arg1))
button1.grid(row=3, column=1, padx=10, pady=10)

button2 = Button(button_Menu, text="   2   ", command=lambda arg1="2": addString(arg1))
button2.grid(row=3, column=2, padx=10, pady=10)

button3 = Button(button_Menu, text="   3   ", command=lambda arg1="3": addString(arg1))
button3.grid(row=3, column=3, padx=10, pady=10)

button4 = Button(button_Menu, text="   4   ", command=lambda arg1="4": addString(arg1))
button4.grid(row=2, column=1, padx=10, pady=10)

button5 = Button(button_Menu, text="   5   ", command=lambda arg1="5": addString(arg1))
button5.grid(row=2, column=2, padx=10, pady=10)

button6 = Button(button_Menu, text="   6   ", command=lambda arg1="6": addString(arg1))
button6.grid(row=2, column=3, padx=10, pady=10)

button7 = Button(button_Menu, text="   7   ", command=lambda arg1="7": addString(arg1))
button7.grid(row=1, column=1, padx=10, pady=10)

button8 = Button(button_Menu, text="   8   ", command=lambda arg1="8": addString(arg1))
button8.grid(row=1, column=2, padx=10, pady=10)

button9 = Button(button_Menu, text="   9   ", command=lambda arg1="9": addString(arg1))
button9.grid(row=1, column=3, padx=10, pady=10)

button0 = Button(button_Menu, text="   0   ", command=lambda arg1="0": addString(arg1))
button0.grid(row=4, column=1, padx=10, pady=10)

buttonDecimal = Button(button_Menu, text="   .   ", command=lambda arg1=".": addString(arg1))
buttonDecimal.grid(row=4, column=3, padx=10, pady=10)

buttonPlus = Button(button_Menu, text="   +   ", command=lambda arg1="+": addString(arg1))
buttonPlus.grid(row=4, column=4, padx=10, pady=10)

buttonMinus = Button(button_Menu, text="   -   ", command=lambda arg1="-": addString(arg1))
buttonMinus.grid(row=3, column=4, padx=10, pady=10)

buttonMult = Button(button_Menu, text="   *   ", command=lambda arg1="*": addString(arg1))
buttonMult.grid(row=2, column=4, padx=10, pady=10)

buttonDiv = Button(button_Menu, text="   /   ", command=lambda arg1="/": addString(arg1))
buttonDiv.grid(row=1, column=4, padx=10, pady=10)

buttonDiv = Button(button_Menu, text="   %   ", command=lambda arg1="%": addString(arg1))
buttonDiv.grid(row=1, column=5, padx=10, pady=10)

buttonDiv = Button(button_Menu, text="   ^   ", command=lambda arg1="**": addString(arg1))
buttonDiv.grid(row=2, column=5, padx=10, pady=10)

buttonAnswr = Button(button_Menu, text=" Ans ", command=lambda: addString(str(answerNum)))
buttonAnswr.grid(row=0, column=1, padx=10, pady=10)

buttonOpenBrack = Button(button_Menu, text="   (   ", command=lambda: openBracket())
buttonOpenBrack.grid(row=0, column=2, padx=10, pady=10)

buttonCloseBrack = Button(button_Menu, text="   )   ", command=lambda: closeBracket())
buttonCloseBrack.grid(row=0, column=3, padx=10, pady=10)

buttonBack = Button(button_Menu, text=" <== ", command=lambda: backSpace())
buttonBack.grid(row=0, column=4, padx=10, pady=10)

buttonClr = Button(button_Menu, text="   C   ", command=lambda: clearString())
buttonClr.grid(row=0, column=5, padx=10, pady=10)

buttonCalc = Button(button_Menu, text="   =   ", command=lambda: calcInput())
buttonCalc.grid(row=4, column=5, padx=10, pady=10)

root.mainloop()
