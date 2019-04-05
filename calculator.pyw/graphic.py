#graphics.py
#Graphical User Interface(GUI) for the calc_functions program
#Created by Ryan Straub
#4/5/19


from graphics import *

from calc_functions import *

def createCanvas():
    win = GraphWin("Calculator",400, 400)
    win.setBackground("Blue")
    return win

def createDisplay(win):
    rectangle =Rectangle(Point(350,25),Point(25,75)).draw(win)
    colorscreen = "white"
    rectangle.setFill(colorscreen)
    size = [100]
    text = Text(Point(250,50),"")
    text.draw(win)
    return text

#Sets Coordinates for buttons
def getCoords(i):
    coords = [[50,275],[200,335],[125,275],[50,215],[125,215],[200,215],[50,155],[125,155],[200,155],[50,95],
              [125,95],[200,95],[200,275],[275,215],[275,275],[275,155],[275,95],[275,335]]
    return coords[i][0], coords[i][1]
#Makes Labels
def getLabel(i):
     labels = ['+/-','Clear','0','1','2','3','4','5','6','7','8','9','.','+','-','*','/','=']
     return labels[i] 

def createButtons(win):
    color = ['white','white','orange','orange','orange','orange','orange','orange','orange','orange','orange','orange','white','white','white','white','white','white']
    size = [50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]

    for i in range(18):
        x, y = getCoords(i)
        button = Rectangle(Point(x,y),Point(x+size[i],y+size[i]))
        button.setFill(color[i])
        label = Text(Point(x+size[i]/2,y+size[i]/2),getLabel(i))
        button.draw(win)
        label.draw(win)

#Takes value of buttons and prints it into string
def evaluate(mouse, display):
    for i in range(18):
        x,y = getCoords(i)
        if x<mouse.x < x+50 and y< mouse.y < y+50:
            print(getLabel(i))
            display.setText(display.getText() + " " + getLabel(i))
            break
    return getLabel(i)

#Adds labels in string together
def addEquation(equation,label):
    if label in ['+','-','*','/']:
        return equation + " " + label + " "
#Makes number negative but you have to put first in equation then hit "="
    elif label in ['+/-']:
        return "-" 
        int(label)
        del label
    else:
        return equation + label

def main():
    win = createCanvas()
    display = createDisplay(win)
    equation = ""
    coords = createButtons(win)
    while True:
        mouse = win.getMouse()
        label = evaluate(mouse, display)
        #calculates answer
        if label == "=":
            result = pemdas(equation.split())
            display.setText(str(result))
        #Clears screen by making new calculator
        elif label == "Clear":
            main()
        else:
            equation = addEquation(equation, label)

main()
