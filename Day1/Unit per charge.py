#Write a program to calculate the electricity bill (accpet number of unit from user) according to the following criteria:

#First unit no charge, Next 100 Rs.5, After 200 Rs.10

unit = int(input("Enter the number of units "))

if unit <=100:
    first = unit*0
    print("Charge = ",first)

elif unit<=200:
    second = 100*0+(unit-100)*5
    print("Charge = ",second)

else:
    third = 100*0+100*5+(unit-200)*10
    print("Charge = ",third)





