# Python – Avoid Spaces in string length

str = input("Enter a string: ")

print(str)
originalLen = len(str)
print(f"Original length of the string = {originalLen} \n")

replace = str.replace(" ", "")
print(replace)
afterLen = len(replace)
print(f"After length of the string = {afterLen}")
