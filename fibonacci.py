#fibonacci.py
#   A program to show the fibonacci sequence.
#   by: Ryan Straub

def main():
    
    n = int(input("What sequence of the fibonacci sequence are you looking for: "))
    old,new = 0,1
    for i in range(0,n-1):
        new2 = old + new
        old = new
        new = new2
    print(new2, "is the", n, "th step in the sequence.")
main()

