#pi.py

def main():
    n = int(input("What placement of pi would you like to see?:"))
    sign = 1
    value = 0
    for i in range(1, n * 2, 2):
        value = value + (4/i * sign)
        sign = sign * -1
        print(value)
main()

