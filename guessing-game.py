#guessing-game

def main():
    while True:
        animal = "dog"
        answer = input("I'm thinking of an animal that is known as 'Man's best friend': ").lower()
        if answer == animal:
            opinion = input("Correct! Do you like this animal?(y/n) ").lower()
            if opinion == "y":
                print("Great!")
                break
            elif opinion == "n":
                print("Oh no!")
                break
        elif answer[0] == "q":
            break
        else:
            print("Thats not it. Try again!")
                
main()
