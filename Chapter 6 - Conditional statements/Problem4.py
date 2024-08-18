# Write a program to find whether a given username contains less than 10 chars or not..

def num_of_chars(string):
    word = len(string)
    if word<10:
        print("The string contains less than 10 characters")
    else:
        print("The string contains more than 10 characters")

string = input("Enter anything: ")
num_of_chars(string)