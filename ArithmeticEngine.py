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
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
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
        except:
            print("Not Valid Command")
            doLoop()
            
        print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()

main()
                 
