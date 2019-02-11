#rover.py
#   A program to determine how fast light travels from Mars to Earth
#by Ryan Straub

def main():
    Speed = eval(input("What is the speed of the object in miles per second?"))
    Distance = eval(input("What is the distance the object will travel in miles?"))
    Time = Distance / Speed
    print("The time it takes is", Time, "seconds.")

main()
    

    
