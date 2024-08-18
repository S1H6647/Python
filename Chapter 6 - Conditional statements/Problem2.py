# Write a program to find out whether a situation has passed or failed if it requies a total of 
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

def toCheck(num1, num2, num3):
    if num1 == num2 == num3 == 40 or num1 == num2 == num3 == 33:
        print("You've passed!")
    else:
        print("You've failed!")

num1 = int(input("Enter your 1st marks percentage: "))
num2 = int(input("Enter your 2nd marks percentage: "))
num3 = int(input("Enter your 3rd marks percentage: "))

toCheck(num1, num2, num3)