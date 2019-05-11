#calculator_graphics.py
#The GUI used in my calculator but organized into classe

#Progammer's Note: I had a bit of trouble debugging my program because I found myself going in a loop trying to fix certain issues.
#However, I did as much as I could to try to implement the mechanics of the calculator even though I couldn't get the buttons to appear.
#This program was challenging, but I did try my hardest woti

#Created by Ryan Straub
#4/5/19

from graphics import *

from calc_functions import *

class Calculator:
    def __init__(self):
        self.win = self.createGraphics()
        self.display = Display(self.win)
        self.display.draw(self.win)
        self.keypad = Keypad()
        self.Keypad.draw(self.win)
        self.engine = CalculatorEngine()
    def createGraphics(self):
        win = GraphWin("Calculator",425, 400)
        win.setBackground("Blue")
        return win
    def run(self):
        while True:
            key = self.keypad.getKeyPressed()
            print(key)
            result = self.engine.addKeyPressed(key)
            if result == "quit":
                break
            self.display.setText(result)

#-----------------------------------------------------------------------------------------------------------------------------#
class CalculatorEngine:
    def __init__(self):
        self.memory = Memory()
        self.equation = ""
    def addEquation(self,label):
        if label in ["+", "-","*","/"]:
            self.equation= self.equation + " " + label + " "
        elif label in ['+/-']:
            return "-"
            int(label)
            del label
        else:
            self.equation= self.equation + label
    def addKeyPressed(self,key):
        if key in ["M+", "M-", "MR", "MC"]:
            self.memory.process(key,self.equation)
            return self.equation
        elif key == "=":
            return self.solve()
        elif key == "Clear":
            self.equation = ""
#----------------------------------------------------------------------------------------------------------------#
class Keypad:
    def __init__(self, win):
        self.keypadWin = win
        self.buttons = self.createButtons(win)
    def createButtons(self,win):
        coords = [[50,275],[200,335],[125,275],[50,215],[125,215],
                  [200,215],[50,155],[125,155],[200,155],[50,95],
                  [125,95],[200,95],[200,275],[275,215],
                  [275,275],[275,155],[275,95],[275,335],
                  [350,95],[350,155],[350,215],[350,275]]
        label = ['+/-','Clear','0','1','2','3','4','5','6','7',
                  '8','9','.','+','-','*','/','=','MC','MR','M+','M-']
        size = [50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]
        color = ['white','white','orange','orange','orange','orange','orange','orange','orange','orange',
                'orange','orange','white','white','white','white','white','white',
                'white','white','white', 'white', 'white']
        buttons = []
        for i in range(len(coords)):
            x, y = coords[i]
            button = Button(size[i], label[i], color[i], Point(x,y))
            buttons.append(button)
            button.draw(win)
        return buttons
    def getKeyPressed(self):
        p = self.keypadWin.getMouse()
        return self.checkKey(p)
    def checkKey(self, p):
        for b in self.buttons:
            if b.isPressed(p):
                return b.getLabel()
#----------------------------------------------------------------------------------------------------------------#

class Display:
    def __init__(self, win):
        rectangle =Rectangle(Point(350,25),Point(25,75)).draw(win)
        colorscreen = "white"
        self.win = win
        rectangle.setFill(colorscreen)
        size = [100]
        self.label= Text(Point(250,50),"") 
        self.label.draw(win)

    def setText(self, text):
        self.label.setText(text)
        
#-----------------------------------------------------------------------------------------------------------------------------#

class Button:
    def __init__(self, size, label, color, point):
        self.size = size
        self.label = label
        self.position = point
        self.color = color
        p = self.position
        point = self.position
        self.rectangle = Rectangle(p,Point(p.getX() + self.size, p.getY() + self.size)) 
        self.label = Text(Point(p.getX() + size/2, p.getY() + size(2)))
        set.rectangle.setBackground(self,color)
    def getLabel(self):
        return self.label
    def isclicked(self):
        if self.position.getX()<=point.getX()<=self.position.getX() + self.size and self.position.getY()<= point.getY()<=self.position.getY()-self.size:
            return True
        return False
    def setPosition(self, x, y):
        dx =  - self.position.getX()
        dy =  - self.position.getX()
        self.position.move (dx, dy)
        self.rectangle.move(dx, dy)
        self.label.move(dx,dy)
    def setColor(self, color):
        self.color = color #Double Check
        self.rectangle.setBackground(color)
    def draw(self, win): #DOUBLE CHECK
        self.rectangle.draw(win)
        self.label.draw(win)
        button1 = Button(30, "7")
        win = GraphWin()
        button1.draw(win)
        button1.setPosition(10,10)
        while True:
            p = win.getMouse()
            if button1 is clicked:
                label = button1.getLabel()
#-----------------------------------------------------------------------------------------------------------------#
class Memory:
    def __init__(self):
        self.value = 0
    def getValue(self):
        return self.value
    def add(self, value):
        self.value+=value
    def subtract(self, value):
        self.value==value
    def clear(self):
        self.value = 0
#-----------------------------------------------------------------------------------------------------------------#
            
def main():
    calc= Calculator()
    calc.run()

main()
