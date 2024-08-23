# Recursion to calculate the sum of first n natural numbers

def sum_of_numbers(n):
    if (n == 1):
        return 1
    elif (n == 0):
        return 0
    else:
        return n + sum_of_numbers(n - 1)
    
n = int(input("Enter any number: "))
output = sum_of_numbers(n)
print("Sum of n natural numbers = ",output)