# Python program to print even length words in a string

str = input("Enter any string:")

splitString = str.split(' ')
for word in splitString:
    if len(word) % 2 == 0:
        print(word)
