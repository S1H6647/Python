# Python program to check whether the string is or Palindrome

enteredString = input("Enter a string: ")
enteredString = enteredString.lower()

def isPalindrome(enteredString): 
    lengthString = len(enteredString)
    mid = lengthString // 2 # Prints exact half (no float values)
    if mid % 2 == 0:
        return enteredString[:mid] == enteredString[mid:]

if isPalindrome(enteredString):
    print("Is Palindrome")
else:
    print("Is not Palindrome")

