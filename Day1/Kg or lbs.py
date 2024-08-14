# 1kg = 2.205lbs

weight =  float(input("Enter your weight: "))
convert = input("(k)g or (L)bs: ")

if convert.upper() == "K":
    print("Weight in Kg = ",weight)

elif convert.upper() == "L":
    print("Weight in Lbs = ",weight*2.205)

else:
    print("Error input")
