# Paul van Sittert 24.3.23
from tkinter import *
from math import sqrt, factorial, log

# Set up var
calculatorString = ""
answerNum=0
bracket=0 #How deep inside the brackets the user is
π = 3.141592
e = 2.718281

# Define functions

def addString(string):
    global calculatorString

    checkList = ["+", "-", "*", "/", "**", "%"]
    if(string in checkList):
        if (calculatorString == ""):
            addPrev()

    newString = calculatorString[:len(calculatorString)-bracket] + string + calculatorString[len(calculatorString)-bracket:]
    calculatorString = newString
    outputString()

def addPrev():
    global calculatorString
    calculatorString= str(answerNum)

def openBracket():
    global bracket
    addString("()")
    bracket +=1
    outputString()

def closeBracket():
    global bracket

    if bracket >0:
        bracket -=1

    outputString()

def openSqrt():
    addString("sqrt")
    openBracket()

def backSpace():
    global calculatorString
    global bracket

    if(len(calculatorString)>0):
        if (len(calculatorString) > 1 and calculatorString[len(calculatorString) - bracket - 2] == "t"):
            newString = calculatorString[:len(calculatorString) - bracket - 5] + calculatorString[len(calculatorString) - bracket+1:]
            calculatorString = newString
            bracket -= 1
        elif(calculatorString[len(calculatorString)-bracket-1] == "("):
            newString = calculatorString[:len(calculatorString) - bracket-1] + calculatorString[len(calculatorString) - bracket +1:]
            calculatorString = newString
            bracket -= 1
        else:
            newString = calculatorString[:len(calculatorString) - bracket - 1] + calculatorString[len(calculatorString) - bracket:]
            calculatorString = newString

    outputString()

def factorialButton():
    global calculatorString

    if (calculatorString == ""):
        addPrev()

    newString = "factorial("+calculatorString +")"
    calculatorString = newString
    calcInput()

def logButton(logNum):
    global calculatorString

    if(calculatorString == ""):
        addPrev()

    if(logNum == "e"):
        newString = "log(" + calculatorString + ", e)"
    else:
        newString = "log(" + calculatorString + ", "+str(logNum)+")"
    calculatorString = newString
    calcInput()

def clearString():
    global calculatorString
    global answerNum
    global bracket

    calculatorString = ""
    answerNum = 0
    bracket = 0
    outputString()


def calcInput():
    global calculatorString
    global answerNum
    global bracket

    try:
        answerNum = eval(calculatorString)
        calculatorString = calculatorString + " = " + str(answerNum)
    except:
        calculatorString = "Invalid Calculation"

    bracket = 0
    outputString()
    calculatorString = ""


def outputString():
    newString = calculatorString[:len(calculatorString)-bracket] + " >" + calculatorString[len(calculatorString)-bracket:]
    output_Label.config(text=newString)


# Set up gui
root = Tk()
root.title("My calculator")
root.config(bg="#1E20CB")
root.resizable(False, False)

# Set up frames
output_frame = Frame(root, width=100, height=50)
output_frame.grid(row=0, column=0, padx=10, pady=10)

output_Label = Label(output_frame, bg="#6EB3F7", text="", width=60, font=("Times",20), anchor="e", justify=RIGHT, padx=10)
output_Label.pack()

button_Menu = Frame(root, width=100, height=400, bg="#1E76CB")
button_Menu.grid(row=1, column=0, padx=10, pady=10)

# Set up buttons
filler1_lable = Label(button_Menu, width=25, bg="#1E76CB")
filler1_lable.grid(row=0, column=0)

filler2_lable = Label(button_Menu, width=25, bg="#1E76CB")
filler2_lable.grid(row=7, column=7)

#Number Buttons
button1 = Button(button_Menu, bg="#6EB3F7", text="   1   ", font=("Times",18), command=lambda arg1="1": addString(arg1))
button1.grid(row=4, column=2, padx=10, pady=10)

button2 = Button(button_Menu, bg="#6EB3F7", text="   2   ", font=("Times",18), command=lambda arg1="2": addString(arg1))
button2.grid(row=4, column=3, padx=10, pady=10)

button3 = Button(button_Menu, bg="#6EB3F7", text="   3   ", font=("Times",18), command=lambda arg1="3": addString(arg1))
button3.grid(row=4, column=4, padx=10, pady=10)

button4 = Button(button_Menu, bg="#6EB3F7", text="   4   ", font=("Times",18), command=lambda arg1="4": addString(arg1))
button4.grid(row=3, column=2, padx=10, pady=10)

button5 = Button(button_Menu, bg="#6EB3F7", text="   5   ", font=("Times",18), command=lambda arg1="5": addString(arg1))
button5.grid(row=3, column=3, padx=10, pady=10)

button6 = Button(button_Menu, bg="#6EB3F7", text="   6   ", font=("Times",18), command=lambda arg1="6": addString(arg1))
button6.grid(row=3, column=4, padx=10, pady=10)

button7 = Button(button_Menu, bg="#6EB3F7", text="   7   ", font=("Times",18), command=lambda arg1="7": addString(arg1))
button7.grid(row=2, column=2, padx=10, pady=10)

button8 = Button(button_Menu, bg="#6EB3F7", text="   8   ", font=("Times",18), command=lambda arg1="8": addString(arg1))
button8.grid(row=2, column=3, padx=10, pady=10)

button9 = Button(button_Menu, bg="#6EB3F7", text="   9   ", font=("Times",18), command=lambda arg1="9": addString(arg1))
button9.grid(row=2, column=4, padx=10, pady=10)

button0 = Button(button_Menu, bg="#6EB3F7", text="           0           ", font=("Times",18), command=lambda arg1="0": addString(arg1))
button0.grid(row=5, column=2, columnspan=2, padx=10, pady=10)

#Operator buttons
buttonDecimal = Button(button_Menu, bg="#6EB3F7", text="   .   ", font=("Times",18), command=lambda arg1=".": addString(arg1))
buttonDecimal.grid(row=5, column=4, padx=10, pady=10)

buttonPlus = Button(button_Menu, bg="#6EB3F7", text="   +   ", font=("Times",18), command=lambda arg1="+": addString(arg1))
buttonPlus.grid(row=5, column=5, padx=10, pady=10)

buttonMinus = Button(button_Menu, bg="#6EB3F7", text="   -   ", font=("Times",18), command=lambda arg1="-": addString(arg1))
buttonMinus.grid(row=4, column=5, padx=10, pady=10)

buttonMult = Button(button_Menu, bg="#6EB3F7", text="   *   ", font=("Times",18), command=lambda arg1="*": addString(arg1))
buttonMult.grid(row=3, column=5, padx=10, pady=10)

buttonDiv = Button(button_Menu, bg="#6EB3F7", text="   /   ", font=("Times",18), command=lambda arg1="/": addString(arg1))
buttonDiv.grid(row=2, column=5, padx=10, pady=10)

buttonMod = Button(button_Menu, bg="#6EB3F7", text="   %   ", font=("Times",18), command=lambda arg1="%": addString(arg1))
buttonMod.grid(row=2, column=6, padx=10, pady=10)

buttonPow = Button(button_Menu, bg="#6EB3F7", text="   ^   ", font=("Times",18), command=lambda arg1="**": addString(arg1))
buttonPow.grid(row=3, column=6, padx=10, pady=10)

buttonSqrt = Button(button_Menu, bg="#6EB3F7", text="   √   ", font=("Times",18), command=lambda : openSqrt())
buttonSqrt.grid(row=4, column=6, padx=10, pady=10)

buttonAnswr = Button(button_Menu, bg="#6EB3F7", text=" Ans ", font=("Times",18), command=lambda: addString(str(answerNum)))
buttonAnswr.grid(row=1, column=2, padx=10, pady=10)

buttonOpenBrack = Button(button_Menu, bg="#6EB3F7", text="   (   ", font=("Times",18), command=lambda: openBracket())
buttonOpenBrack.grid(row=1, column=3, padx=10, pady=10)

buttonCloseBrack = Button(button_Menu, bg="#6EB3F7", text="   )   ", font=("Times",18), command=lambda: closeBracket())
buttonCloseBrack.grid(row=1, column=4, padx=10, pady=10)

buttonBack = Button(button_Menu, bg="#6EB3F7", text=" <== ", font=("Times",18), command=lambda: backSpace())
buttonBack.grid(row=1, column=5, padx=10, pady=10)

buttonClr = Button(button_Menu, bg="#6EB3F7", text="   C   ", font=("Times",18), command=lambda: clearString())
buttonClr.grid(row=1, column=6, padx=10, pady=10)

buttonCalc = Button(button_Menu, bg="#6EB3F7", text="   =   ", font=("Times",18), command=lambda: calcInput())
buttonCalc.grid(row=5, column=6, padx=10, pady=10)

buttonPi = Button(button_Menu, bg="#6EB3F7", text="   π   ", font=("Times",18), command=lambda arg1="π": addString(arg1))
buttonPi.grid(row=1, column=1, padx=10, pady=10)

buttonEuler = Button(button_Menu, bg="#6EB3F7", text="   e   ", font=("Times",18), command=lambda arg1="e": addString(arg1))
buttonEuler.grid(row=2, column=1, padx=10, pady=10)

buttonFact = Button(button_Menu, bg="#6EB3F7", text="   !   ", font=("Times",18), command=lambda : factorialButton())
buttonFact.grid(row=3, column=1, padx=10, pady=10)

buttonLog = Button(button_Menu, bg="#6EB3F7", text="  Log  ", font=("Times",18), command=lambda arg1="10": logButton(arg1))
buttonLog.grid(row=4, column=1, padx=10, pady=10)

buttonln = Button(button_Menu, bg="#6EB3F7", text="  ln   ", font=("Times",18), command=lambda arg1="e": logButton(arg1))
buttonln.grid(row=5, column=1, padx=10, pady=10)

outputString()
root.mainloop()
