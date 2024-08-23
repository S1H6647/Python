# Program to print multiplicaton table of n number

def mulTable(n):
    for i in range(1,11):
        print(f"{n} X {i} = {i*n}")

n = int(input("Enter a number: "))
mulTable(n)