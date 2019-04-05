# CMPT 120 - Lab #6
# Ryan Straub
# 01-04-2019
###

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")


def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower()
        try:
            if cmd not in ["add" ,"mult", "sub", "div"]:
                print("Oops,Try Again!")
                doLoop()
            #Insert Numbers
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            try:
                frac = num1/num2 #will crash because of division
                if cmd == "add":
                    result = num1 + num2
                elif cmd == "sub":
                    result = num1 - num2
                elif cmd == "mult":
                    result = num1 * num2
                elif cmd == "div":
                    result = num1 // num2
                elif cmd == "quit":
                    break
            #If user tries to divide by zero
            except:
                print("Unable to divide by zero!")
                frac = 0
                doLoop()
        except:
                print("Not Valid Command")
                doLoop()
        #Prints answer that is valid
        print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()

main()
                 
