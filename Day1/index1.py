# Program to check whether a character is an alphabet, digit or special character

ch = int(input("Enter anything: "))

if ch >=0 or ch <=9:
    print("It is a digit")

elif str(ch.upper())>="a" or str(ch.upper())<="z":
    print("It is an alphabet")

else:
    print("it is a speical character")