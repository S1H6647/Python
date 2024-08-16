# A program to input eight numbers from the user and display all the unique numbers(once)

set = set()

for number in range(8):
    num = int(input("Enter numbers: "))
    set.add(num)

print("Entered numbers are: ",set)