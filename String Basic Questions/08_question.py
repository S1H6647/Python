# Python program to capitalize the first and last character of each word in a string

string = "hello world"

words = string.split(" ")
words[0] = words[0].capitalize()
words[-1] = words[-1].lower()
print(" ".join(words))

# firstWord = splitString[:-1] , splitString[1].upper()
# secondWord = splitString[1].capitalize() + splitString[1][:-1].upper() 

# finalWord = firstWord + secondWord

# words = string.split("") 
# words[0] = words[0].upper()
# words[-1] = words[-1].upper() 
# printf(" ".join(words))

