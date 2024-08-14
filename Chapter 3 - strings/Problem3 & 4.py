# Finding double space

str = "He  llo"
print(str.find("  "))

# Replaceing double space with single spaces

str = "He  llo"
print(str.replace("  "," ")) # Creates a new string then prints 
print(str) 
# Strings are immutables which means that you cannot cange them by running functions on them 