# Program to convert Celsius to Fahrenheit

def convert(C):
    F = (9/5 * C) + 32
    print("Temperature in Fahrenheit is ",F)

C = int(input("Enter temperature in Celsius: "))
convert(C)