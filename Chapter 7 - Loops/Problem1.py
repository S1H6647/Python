# Multiple of a number entered by user


def multipleTable(num):
    for number in range(1,11):
        print(f"{num} x {number} = {num*number}")

    # i = 1
    # while (i<=10):
    #     print(num, "x", i, "=", num*i)
    #     i += 1

num = int(input("Enter the number you want to have multiplcation table of: "))
multipleTable(num)

