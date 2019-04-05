#calculator.py
#Acts as a Working Calculator for basic arithmetic and PEMDAS
#Created by Ryan Straub
#3/5/19

#def main()
    #Where you insert a formula.
    #equation = input("Insert Problem: ").split(" ")
    #Is what you inserted just a number or not?
    #if len(equation)<=2:
        #print("This is not a formula.")
    #else:
        #print(pemdas(equation))
        
        
def hasPrdDv(equation):
    # Checks for addition and subtraction in list then puts them in a list.
    if "*" in equation or "/" in equation:
        return True
    return False

def process(equation,i):
    # Checks for addition and subtraction in list then puts them in a list.
    if equation[i]== '*':
        result = float(equation[i-1]) * float(equation[i+1])
    elif equation[i]== '/':
        result = float(equation[i-1]) / float(equation[i+1])
    elif equation[i]== '+':
        result = float(equation[i-1]) + float(equation[i+1])
    elif equation[i]== '-':
        result = float(equation[i-1]) - float(equation[i+1])
    del equation[i-1:i+2]
    equation.insert(i-1,str(result))
        
    #Prints Result
    #print(result)

def pemdas(equation):
    i = 0
    result=0;
    #Checks if there is division or multiplication.
    while hasPrdDv(equation):
        if equation[i]=='*' or equation[i] == '/':
            process(equation,i)
        else:
            i = i + 1
    i=0        
    #Checks if there is addition or subtraction.
    while len(equation)>1:
        if equation[i]=='+' or equation[i]== '-':
            process(equation, i)
        else:
            i = i + 1
    
    return float(equation[0])
   
          


