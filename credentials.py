#CMPT 120 Intro to Programing
#Lab #5 - Working with Strings and Functions
#Author: Ryan Straub
#Created 2019 -03-01

def main():
    #get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    #concatenate first initial with 7 characters of last name
    uname = first[0] + '.' + last[:7]
    #output the username
    print ("Your usernameis:", uname)
    #ask user to create a new password
    passwd = input("Create a new password: ")
    while len(passwd)<8:
        print ("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one...")
    print("Account configured. Your new email adress is", uname + "@marist.edu")

main()
