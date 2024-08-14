# program to find whether a given year is a leap year or not. 
# Hint: if year%4==0; if year%100!==0 ; year%400==0

year = int(input("Enter any year: "))

if ((year%4==0) or (year%100!=0) or (year%400==0)):
    print("Leap year")

else:
    print("Not a leap year")