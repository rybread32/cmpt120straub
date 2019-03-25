#guessing-game

def main():
    while True:
        animal = "dog"
        answer = input("I'm thinking of an animal that is known as 'Man's best friend': ")
        if answer == animal:
            print("Correct!")
            break
        else:
            print("Thats not it. Try again!")


main()
    
