# Write a program which finds out whether a given name is present in a list or not.

list = ["Ram", "Harry", "Shyam", "Sita"]

def presentName(cap):
    if (cap in list):
        print("Your name is present in the list")
    else:
        print("Your name is not present in the list")

name = input("Enter your name: ")
cap = name.capitalize()
presentName(cap)