# Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter any number: "))

for num in range(1,11):
    print(f"{n} X {11 - num} = {n*(11 - num)}")

# 1 10
# 2 9
# 3 8
# 4 7
# 5 6
# 6 5
# 7 4
# 8 3
# 9 2
# 10 1
# sum of these numbers is 11 so 11 - i i.e = 1,2,3,...