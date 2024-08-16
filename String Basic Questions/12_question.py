# Python program to count number of vowels using sets in given string
# Method 1:
# Changing a string to set then comparing it to the vowels set
def countVowels(str):
    vowels = set("aeiouAEIOU")
    setStr = set(str)
    return (len(setStr.intersection(vowels)))

str = input("Enter a string: ")

print("Number of vowels in the given string: ", countVowels(str))


