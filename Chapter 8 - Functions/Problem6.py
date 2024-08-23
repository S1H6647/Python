# Program to convert inches to cms

def converter(inch):
    cm = inch * 2.54
    return cm

inch = float(input("Enter inch: "))
output = converter(inch)
print("Inputed inch into cm =", output)