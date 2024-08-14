#Write a program to check whether the last digit of a number is divisible by 3 or not.

num = int(input("Enter any number: "))

last = num % 10
if last % 3 == 0:
    print("Last digit is divisible by 3")

else:
    print("Not divisible by 3")