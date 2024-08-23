# Using function to find the greatest of three numbers 

def greatest(a,b,c):
    if (a>b) and (a>c):
        print("1st number is the greatest: ",a)
    elif (b>c):
        print("2nd number is the greatest: ",b)
    else:
        print("3rd number is the greatest: ",c)

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

greatest(a,b,c)