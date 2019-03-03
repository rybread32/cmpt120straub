#CMPT 120 Intro to Programing
#Lab #5 - Working with Strings and Functions
#Author: Ryan Straub
#Created 2019 -03-01

# JA: Where are the separate functions?
def main():
    #get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    #concatenate first initial with 7 characters of last name
    uname = first[0] + '.' + last[:7]
    #Make username all lowercase
    uname.lower()
    #output the username
    print ("Your username is:", uname.lower())
    #ask user to create a new password
    passwd = input("Create a new password: ")
    while len(passwd)<8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    #Make sure it is not all lowercase
    if passwd.lower()== passwd:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    #Make sure not all uppercase
    if passwd.upper()== passwd:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one...")
    print("Account configured. Your new email adress is", uname.lower() + "@marist.edu")
 
main()
