# Python program to capitalize the first and last character of each word in a string

string = "hello world"

splitString = string.split(" ")
print(splitString)

firstWord = splitString[:-1] , splitString[1].upper()
# secondWord = splitString[1].capitalize() + splitString[1][:-1].upper() 

# finalWord = firstWord + secondWord
print(firstWord)