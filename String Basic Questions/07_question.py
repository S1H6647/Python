# Python – Uppercase Half String

str = "bibi"

divideString = len(str) // 2 

halfUpper = str[divideString:] + str[:divideString].upper()
print(halfUpper)

