# Recursion -> calls itself

# Factorial of n

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n * fact(n-1))

n = int(input("Enter any number: "))
output = fact(n)
print("The factorial of the inputed number is: ",output)